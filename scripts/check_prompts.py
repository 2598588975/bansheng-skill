"""Validate and render the Bansheng prompt contract using only the standard library."""
from pathlib import Path
from decimal import Decimal, InvalidOperation
import argparse
import json
import re
import sys

IMAGE_FIELDS = ("frame", "shot", "subject", "composition", "scene", "lighting", "photography", "material", "parameters")
VIDEO_LABELS = ("主体", "场景", "拍摄风格", "光影构图", "情节", "否定控制")
VIDEO_FIELDS = {"status", "image_id", "image_observed", "duration", "主体", "场景", "拍摄风格", "光影构图", "情节", "声音", "否定控制"}


class ContractError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise ContractError(message)


def single_line(value, label):
    require(isinstance(value, str) and bool(value.strip()), f"{label}必须是非空文字")
    require(len(value.splitlines()) == 1, f"{label}不能分段")
    require("[" not in value and "]" not in value and "{" not in value and "}" not in value, f"{label}有未替换变量")
    return value.strip()


def clause(value):
    return value.rstrip("。；; .")


def render_image(image):
    require(isinstance(image, dict), "image必须是字段对象")
    require(set(image) == set(IMAGE_FIELDS), "图片字段必须完整且只有规定的九个键（画幅与景别共同构成第一项）")
    values = {key: single_line(image[key], key) for key in IMAGE_FIELDS}
    ratio = re.search(r"(?<!\d)(\d+:\d+)(?!\d)", values["frame"])
    require(ratio is not None, "frame缺少数字画幅")
    require(all(int(part) > 0 for part in ratio.group(1).split(':')), "画幅比例必须为正数")
    parameters = values["parameters"]
    param_ratio = re.search(r"(?:^|\s)--ar\s+(\d+:\d+)(?=\s|$)", parameters)
    require(param_ratio is not None and param_ratio.group(1) == ratio.group(1), "正文画幅与--ar不一致")
    require(parameters.startswith("--"), "MJ参数必须独立位于末尾")
    require(not re.search(r"[\u4e00-\u9fff。；]", parameters), "参数尾部不能混入中文说明")
    require(len(re.findall(r"(?:^|\s)--ar\s", parameters)) == 1, "--ar不能重复")
    if re.search(r"--v\s+8(?:\.\d+)?(?=\s|$)", parameters):
        require(not re.search(r"(?:^|\s)--(?:q|quality|oref|cref)(?:\s|$)", parameters) and "::" not in parameters, "V8提示词混入旧版本参数")
    prose = clause(values['frame']) + "，" + clause(values['shot']) + "。" + "。".join(clause(values[key]) for key in IMAGE_FIELDS[2:-1]) + "。"
    require("--" not in prose, "图片正文中不能插入MJ参数")
    require(not re.search(r"(?:\d+(?:\.\d+)?秒|转场|Dolly|Tracking|摄影机(?:缓慢)?(?:推进|后退|环绕)|镜头(?:缓慢)?(?:推进|推入|环绕))", prose, re.I), "图片静帧包含时间轴、运镜或转场")
    require("真人" in values["photography"] and "电影" in values["photography"], "photography必须明确真人电影媒介")
    return prose + " " + parameters


def seconds(value, label):
    require(not isinstance(value, bool), f"{label}不能是布尔值")
    try:
        result = Decimal(str(value))
    except (InvalidOperation, ValueError):
        raise ContractError(f"{label}不是有效秒数")
    require(result.is_finite(), f"{label}必须是有限秒数")
    return result


def render_video(video):
    require(isinstance(video, dict), "video必须是字段对象")
    require(set(video) == VIDEO_FIELDS, "视频字段缺失或增加了第七段/未规定字段")
    require(video["status"] in {"provisional", "final"}, "status必须为provisional或final")
    require(type(video["image_observed"]) is bool, "image_observed必须是布尔值")
    if video["status"] == "final":
        require(video["image_observed"], "未实际观察图片，不能交付最终匹配版")
        single_line(video["image_id"], "image_id")
    duration = seconds(video["duration"], "duration")
    require(duration > 0, "总时长必须大于0")
    text = {key: single_line(video[key], key) for key in ("主体", "场景", "拍摄风格", "光影构图", "声音", "否定控制")}
    declaration = re.search(r"(?<!\d)(\d+(?:\.\d+)?)秒单镜头", text["拍摄风格"])
    require(declaration is not None and seconds(declaration.group(1), "拍摄风格时长") == duration, "拍摄风格时长与duration不一致，或缺少单镜头声明")
    timeline = video["情节"]
    require(isinstance(timeline, list) and bool(timeline), "情节必须有时间段")
    cursor = Decimal("0.00")
    beats = []
    for beat in timeline:
        require(isinstance(beat, dict) and set(beat) == {"start", "end", "action"}, "时间段字段必须为start/end/action")
        for key in ("start", "end"):
            require(isinstance(beat[key], str) and re.fullmatch(r"\d+\.\d{2}", beat[key]), "时间点必须为两位小数字符串")
        start, end = seconds(beat["start"], "start"), seconds(beat["end"], "end")
        require(start == cursor, "时间轴必须从0连续，不能重叠或留空档")
        require(end > start, "时间段必须具有正时长")
        action = single_line(beat["action"], "action")
        beats.append(f"{beat['start']}–{beat['end']}秒：{clause(action)}")
        cursor = end
    require(cursor == duration, "时间轴终点与总时长不一致")
    text["情节"] = "；".join(beats) + "。声音：" + text["声音"]
    return "\n\n".join(label + "：" + text[label] for label in VIDEO_LABELS)


def render_packet(packet):
    require(isinstance(packet, dict) and set(packet) == {"stage", "shots"}, "顶层字段必须是stage/shots")
    stage = packet["stage"]
    require(stage in {"images", "videos", "both"}, "stage必须为images/videos/both")
    shots = packet["shots"]
    require(isinstance(shots, list) and bool(shots), "shots不能为空")
    seen = set()
    blocks = []
    for shot in shots:
        required = {"id"} | ({"image"} if stage == "images" else {"video"} if stage == "videos" else {"image", "video"})
        require(isinstance(shot, dict) and set(shot) == required, "镜头字段与stage不对应")
        shot_id = single_line(shot["id"], "镜号")
        require(re.fullmatch(r"S\d{2,}", shot_id) is not None and shot_id not in seen, "镜号必须为唯一S01格式")
        seen.add(shot_id)
        if stage in {"images", "both"}:
            blocks.append(f"### {shot_id} · MJ图片提示词\n\n```text\n{render_image(shot['image'])}\n```\n")
        if stage in {"videos", "both"}:
            video = shot["video"]
            prompt = render_video(video)
            status = "最终匹配版" if video["status"] == "final" else "预案，待成图校准"
            blocks.append(f"### {shot_id} · Kling O3视频提示词（{status}）\n\n```text\n{prompt}\n```\n")
    return "\n".join(blocks)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--render", type=Path)
    args = parser.parse_args()
    try:
        packet = json.loads(args.input.read_text(encoding="utf-8-sig"))
        rendered = render_packet(packet)
        if args.render:
            require(not args.render.exists(), "输出已存在，选择新路径，避免覆盖")
            args.render.parent.mkdir(parents=True, exist_ok=True)
            args.render.write_text(rendered, encoding="utf-8")
        print(f"格式检查通过：{len(packet['shots'])}镜，阶段{packet['stage']}。仍需人工核对历史、图像锚点与动作可行性。")
    except (ContractError, json.JSONDecodeError, OSError) as error:
        print(f"格式检查失败：{error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

from pathlib import Path
import copy
import hashlib
import importlib.util
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT
spec = importlib.util.spec_from_file_location("contract", SKILL / "scripts" / "check_prompts.py")
contract = importlib.util.module_from_spec(spec)
spec.loader.exec_module(contract)

IMAGE = {
    "frame": "16:9横画幅",
    "shot": "平视近景",
    "subject": "一位花白须发的老人，手中托着旧信囊，垂目不语",
    "composition": "人物位于右侧，信囊在胸前完整可见，左侧保留雨中木门",
    "scene": "架空古代村口，细雨，朴素的木门和土路",
    "lighting": "左上方冷青灰天光照脸，门内一点暖灯，暗部可读",
    "photography": "真人实拍质感的中国古代历史电影剧照，浅景深",
    "material": "自然皱纹、湿麻布织纹与旧木纹，克制胶片颗粒",
    "parameters": "--ar 16:9 --v 8.2 --raw --s 50 --chaos 0",
}
VIDEO = {
    "status": "provisional",
    "image_id": "",
    "image_observed": False,
    "duration": 5,
    "主体": "老人手持旧信囊，身体稳定，主动作是抬眼并露出微笑",
    "场景": "雨中木村门，细雨向右下，背景结构保持稳定",
    "拍摄风格": "5秒单镜头，真人历史电影，极缓微推，焦点在眼睛",
    "光影构图": "左上方冷天光与背景暖灯，脸和信囊完整可见",
    "情节": [
        {"start": "0.00", "end": "0.50", "action": "建立首帧状态"},
        {"start": "0.50", "end": "2.50", "action": "缓慢抬眼"},
        {"start": "2.50", "end": "4.00", "action": "露出微笑"},
        {"start": "4.00", "end": "5.00", "action": "安静停住，保留尾帧"},
    ],
    "声音": "细雨与轻微呼吸，人物不说话",
    "否定控制": "无换脸、手指融合和道具形变；无字幕、无Logo和水印，不生成BGM",
}
IMAGE_SETTINGS = {"stylize": 50, "weird": 0, "chaos": 0}


class ContractTests(unittest.TestCase):
    def test_render_order_and_exact_six_sections(self):
        rendered = contract.render_image(IMAGE)
        values = [IMAGE[k] for k in contract.IMAGE_FIELDS]
        positions = [rendered.index(v) for v in values]
        self.assertEqual(positions, sorted(positions))
        self.assertNotIn("\n", rendered)
        self.assertTrue(rendered.endswith(IMAGE["parameters"]))
        video = contract.render_video(VIDEO)
        self.assertEqual([p.split("：", 1)[0] for p in video.split("\n\n")], list(contract.VIDEO_LABELS))
        self.assertIn("声音：", video.split("\n\n")[4])

    def test_missing_image_component_rejected(self):
        bad = copy.deepcopy(IMAGE)
        del bad["lighting"]
        with self.assertRaises(contract.ContractError):
            contract.render_image(bad)

    def test_image_multiline_rejected(self):
        bad = copy.deepcopy(IMAGE)
        bad["subject"] += "\n第二段"
        with self.assertRaises(contract.ContractError):
            contract.render_image(bad)

    def test_image_motion_rejected(self):
        bad = copy.deepcopy(IMAGE)
        bad["subject"] += "，2秒后完成遮挡转场"
        with self.assertRaises(contract.ContractError):
            contract.render_image(bad)

    def test_parameter_in_prose_rejected(self):
        bad = copy.deepcopy(IMAGE)
        bad["subject"] += " --ar 16:9"
        with self.assertRaises(contract.ContractError):
            contract.render_image(bad)

    def test_ratio_mismatch_rejected(self):
        bad = copy.deepcopy(IMAGE)
        bad["parameters"] = bad["parameters"].replace("16:9", "3:4")
        with self.assertRaises(contract.ContractError):
            contract.render_image(bad)

    def test_incompatible_mj_version_rejected(self):
        bad = copy.deepcopy(IMAGE)
        bad["parameters"] += " --oref example.png"
        with self.assertRaises(contract.ContractError):
            contract.render_image(bad)

    def test_video_extra_section_rejected(self):
        bad = copy.deepcopy(VIDEO)
        bad["音频设计"] = "雨声"
        with self.assertRaises(contract.ContractError):
            contract.render_video(bad)

    def test_timeline_gap_rejected(self):
        bad = copy.deepcopy(VIDEO)
        bad["情节"][1]["start"] = "0.60"
        with self.assertRaises(contract.ContractError):
            contract.render_video(bad)

    def test_timeline_overlap_rejected(self):
        bad = copy.deepcopy(VIDEO)
        bad["情节"][1]["start"] = "0.40"
        with self.assertRaises(contract.ContractError):
            contract.render_video(bad)

    def test_timeline_duration_mismatch_rejected(self):
        bad = copy.deepcopy(VIDEO)
        bad["情节"][-1]["end"] = "4.90"
        with self.assertRaises(contract.ContractError):
            contract.render_video(bad)

    def test_declared_duration_mismatch_rejected(self):
        bad = copy.deepcopy(VIDEO)
        bad["拍摄风格"] = bad["拍摄风格"].replace("5秒", "6秒")
        with self.assertRaises(contract.ContractError):
            contract.render_video(bad)

    def test_imprecise_timestamp_rejected(self):
        bad = copy.deepcopy(VIDEO)
        bad["情节"][0]["start"] = "0"
        with self.assertRaises(contract.ContractError):
            contract.render_video(bad)

    def test_unseen_image_cannot_be_final(self):
        bad = copy.deepcopy(VIDEO)
        bad["status"] = "final"
        bad["image_id"] = "S01-selected.png"
        with self.assertRaises(contract.ContractError):
            contract.render_video(bad)
        bad["image_observed"] = True
        self.assertEqual(len(contract.render_video(bad).split("\n\n")), 6)

    def test_duplicate_shots_rejected(self):
        packet = {"stage": "images", "shots": [{"id": "S01", "image": IMAGE, "image_settings": IMAGE_SETTINGS}, {"id": "S01", "image": IMAGE, "image_settings": IMAGE_SETTINGS}]}
        with self.assertRaises(contract.ContractError):
            contract.render_packet(packet)

    def test_each_image_has_five_explicit_settings(self):
        packet = {"stage": "images", "shots": [{"id": shot, "image": IMAGE, "image_settings": IMAGE_SETTINGS} for shot in ("S01", "S02")]}
        rendered = contract.render_packet(packet)
        for label, value in (("画幅", "16:9"), ("版本", "V8.2"), ("风格化程度", 50), ("怪异度", 0), ("多样性（随机性）", 0)):
            self.assertEqual(rendered.count(f"| {label} | {value} |"), 2)

    def test_missing_settings_rejected(self):
        with self.assertRaises(contract.ContractError):
            contract.render_packet({"stage": "images", "shots": [{"id": "S01", "image": IMAGE}]})
        bad = dict(IMAGE_SETTINGS)
        del bad["weird"]
        with self.assertRaises(contract.ContractError):
            contract.render_image_settings(bad, IMAGE)

    def test_settings_must_match_all_present_suffixes(self):
        for parameters in ("--ar 16:9 --v 8.2 --s 200 --chaos 0", "--ar 16:9 --v 8.2 --s 50 --chaos 5", "--ar 16:9 --v 8.2 --s 50 --chaos 0 --w 50"):
            with self.subTest(parameters=parameters), self.assertRaises(contract.ContractError):
                contract.render_image_settings(IMAGE_SETTINGS, {**IMAGE, "parameters": parameters})

    def test_settings_ranges_and_integer_types(self):
        for key, value in (("stylize", 1001), ("weird", 3001), ("chaos", 101), ("weird", -1), ("chaos", True), ("stylize", 50.5)):
            with self.subTest(key=key, value=value), self.assertRaises(contract.ContractError):
                contract.render_image_settings({**IMAGE_SETTINGS, key: value}, IMAGE)

    def test_duplicate_alias_and_missing_suffix_value_rejected(self):
        for suffix in (" --stylize 50", " --s"):
            with self.subTest(suffix=suffix), self.assertRaises(contract.ContractError):
                contract.render_image_settings(IMAGE_SETTINGS, {**IMAGE, "parameters": IMAGE["parameters"] + suffix})

    def test_settings_table_requires_one_version(self):
        for parameters in ("--ar 16:9 --s 50 --chaos 0", IMAGE["parameters"] + " --v 8.1"):
            with self.subTest(parameters=parameters), self.assertRaises(contract.ContractError):
                contract.render_image_settings(IMAGE_SETTINGS, {**IMAGE, "parameters": parameters})

    def test_video_only_packet_does_not_require_image_settings(self):
        rendered = contract.render_packet({"stage": "videos", "shots": [{"id": "S01", "video": VIDEO}]})
        self.assertIn("预案，待成图校准", rendered)
        self.assertNotIn("本镜生图设置", rendered)


class ArchiveTests(unittest.TestCase):
    def test_palace_archive_hashes_and_verbatim_contents(self):
        base = SKILL / "references"
        manifest = json.loads((base / "palace-offline-manifest.json").read_text(encoding="utf-8"))
        for item in manifest["files"]:
            blob = (base / item["path"]).read_bytes()
            self.assertEqual(len(blob), item["bytes"])
            self.assertEqual(hashlib.sha256(blob).hexdigest(), item["sha256"])
        corpus = json.loads((base / "palace-source-corpus.json").read_text(encoding="utf-8"))
        records = corpus["records"]
        self.assertEqual(len(records), 77)
        self.assertEqual(len({r["id"] for r in records}), 77)
        self.assertEqual(sum(r["kind"] == "image-prompt" for r in records), 50)
        self.assertEqual(sum(r["kind"] == "video-prompt" for r in records), 17)
        self.assertEqual(sum(r["kind"] == "no-independent-prompt" for r in records), 9)
        for filename, kinds, count in (("palace-source-prompts.md", {"image-prompt", "video-prompt"}, 67), ("palace-source-context.md", {"context"}, 1)):
            extracted = re.findall(r"^````text\n(.*?)\n````$", (base / filename).read_text(encoding="utf-8"), re.M | re.S)
            expected = [r["prompt"] for r in records if r["kind"] in kinds]
            self.assertEqual(extracted, expected)
            self.assertEqual(len(extracted), count)

    def test_offline_hashes_and_coverage(self):
        base = SKILL / "references"
        manifest = json.loads((base / "offline-manifest.json").read_text(encoding="utf-8"))
        for item in manifest["files"]:
            self.assertEqual(hashlib.sha256((base / item["path"]).read_bytes()).hexdigest(), item["sha256"])
        corpus = json.loads((base / "source-corpus.json").read_text(encoding="utf-8"))
        self.assertEqual(len(corpus["records"]), 150)
        self.assertEqual(len({r["id"] for r in corpus["records"]}), 150)
        source_md = (base / "source-prompts.md").read_text(encoding="utf-8")
        extracted = re.findall(r"^````text\n(.*?)\n````$", source_md, re.M | re.S)
        expected = [r["prompt"] for r in corpus["records"] if r["kind"] in {"image-prompt", "video-prompt", "image-node-prompt"}]
        self.assertCountEqual(extracted, expected)
        self.assertEqual(len(extracted), 81)

    def test_relative_skill_links_resolve(self):
        for doc in [SKILL / "SKILL.md", *list((SKILL / "references").glob("*.md"))]:
            for target in re.findall(r"\]\(([^)]+)\)", doc.read_text(encoding="utf-8")):
                if target.startswith(("https://", "http://")):
                    continue
                self.assertTrue((doc.parent / target).exists(), f"missing reference: {doc}: {target}")


if __name__ == "__main__":
    unittest.main(verbosity=2)

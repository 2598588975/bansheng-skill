# 半生 · Bansheng

面向古风历史感真人电影的 Codex Skill。先做角色锚点、分镜与 MJ 图片提示词，选图后可走 Kling O3 单镜头或 Seedance 2.5 多镜头连续段。

## 制作流程

1. 给出大致剧情、人物经历、诗词或创意。
2. 获得分镜表与逐镜 MJ 图片提示词，每镜另附五项设置表。
3. 按操作指导在 MJ 生图，选定后回传完整单图与镜头编号。
4. Skill 实际查看图片，单镜头按 Kling O3 格式编写，多镜头连续段按 [Seedance 2.5 分支](references/seedance-25.md)编写。
5. 按操作指导完成图生视频，回传结果后可继续修正。

技能只负责提示词、选图判断和操作说明。素材生成与额度使用由使用者在对应平台完成。

## 格式硬规则

图片提示词采用一个代码块中的单段中文，固定顺序为：

**画幅与景别/机位 → 主体与静态瞬间 → 构图 → 场景 → 光影色调 → 真人电影拍摄质感 → 实体材质/颗粒 → MJ 参数。**

每个图片代码块外另列 **画幅、版本、风格化程度、怪异度、多样性（随机性）**，逐镜填写建议值，不能只写“同上”。后三项是LibTV的三个额外数值设置；后缀与表格保持一致。使用LibTV独立设置时，粘贴中文正文，再按表填画幅、版本和三个滑杆。

Kling O3 视频提示词采用一个代码块中的六段，段间空一行，标签与顺序固定：

**主体 → 场景 → 拍摄风格 → 光影构图 → 情节 → 否定控制。**

情节时间点统一两位小数，从 `0.00` 连续覆盖至总时长。声音说明放在情节段内。尚未看到成图时，视频内容标为“待成图校准”的预案，预案也遵守同一格式。

完整约束见 [格式硬规则](references/format-contract.md)。

## 安装与使用

将仓库内容放在 Codex 的技能目录中的 `bansheng` 文件夹，保证路径结构为 `bansheng/SKILL.md`。可克隆此仓库，或下载 [完整技能压缩包](bansheng-skill.zip)，解压后将其中的 `bansheng` 文件夹放入技能目录。

在 Codex 中调用：

```text
使用 $bansheng，根据以下大致剧情先给分镜和 MJ 图片提示词：……
```

选图后继续：

```text
使用 $bansheng，这是 S01 的选定图片，请按六段硬格式给出匹配首帧的 Kling O3 视频提示词及操作步骤。
```

## 离线原文底版

底版来自《半生》｜诗里白头，一眼半生的 LibTV 项目，保存日期为 **2026-09-30**。逐一核对 145 个独立节点，加上 5 个分组，共 150 个节点；保存 81 条提示词原文：

| 内容 | 数量 |
| --- | ---: |
| 图片分镜提示词 | 24 |
| 视频分镜提示词 | 32 |
| 图片节点生成/编辑提示词 | 25 |
| 另存人物资料 | 4 |

原文保留重复、拼写、翻译腔和矛盾句；分析、模板和新格式约束单独存放。日常使用可读取本地底版，无需重新访问原项目。媒体以溯源地址记录，底版保存的是提示词文本。

- [全部提示词原文](references/source-prompts.md)
- [人物资料原文](references/source-context.md)
- [节点索引与覆盖范围](references/source-index.md)
- [完整结构数据：150 个节点与 94 条可见连线](references/source-corpus.json)
- [底版 SHA-256 清单](references/offline-manifest.json)
- [视觉写法分析](references/visual-dna.md)
- [组织模板与示例](references/templates.md)
- [手动生成操作](references/manual-steps.md)

## 《奉天靖难》宫阙美学与原文库

2026-10-08新增三千问Atelier的[《奉天靖难丨朱墙古松中式宫阙美学》](https://www.liblib.tv/detail/8ad216d218f04758b6224936ba680f7e)参考分支。已逐一读取画布77个独立节点：50条图片提示词、17条视频提示词、1条教学说明，9个节点无可见独立正文。两条金川门图片提示词同文，归档保留重复记录。

- [67条提示词原文](references/palace-source-prompts.md)
- [制作教学原文](references/palace-source-context.md)
- [节点索引与阅读范围](references/palace-source-index.md)
- [完整结构数据](references/palace-source-corpus.json)
- [原文SHA-256清单](references/palace-offline-manifest.json)
- [宫阙尺度、构图、色光、角色参考与声画叙事的提炼](references/palace-aesthetics.md)

可先按节点名或ID找原文，再借鉴写法。归档保留读取到的字符、旧参数、矛盾与混合语言，不把原文改成半生模板；DOM textContent可能压平编辑器段落边界。部分媒体加载失败，此处不声称验证过成片。来源文本中的风格化200/多样性5与界面当时的100/50/5分别记录，不认定其中一组就是历史有效生成参数。

这一分支按题材使用；原有《半生》人生叙事底版、单镜头六段视频格式与手动生成边界继续保留。

## 本地检查

其他已收录的入口包括[角色锚点](references/role-anchor-card.md)、[逐镜查库与项目缓存](references/scene-cache.md)、[场景库索引](references/scene-library-index.md)和[成片反馈记录](references/generation-feedback.md)。

运行时只需要 Python 标准库。

```text
python -m unittest discover -s tests -v
python scripts/check_prompts.py --input 本次草稿.json --render 本次提示词.md
```

检查覆盖字段、画幅、时序、六段格式、实际看图门槛、逐镜五项设置、后缀数值一致性，以及两套原文库的数量、字符与校验值。图片草稿还需在`image`同级提供`image_settings`，例如`{"stylize":50,"weird":0,"chaos":0}`，详见格式硬规则。历史考据、首帧的真实观察、动作可行性及实际生成效果仍需人工判断。

MJ与Kling原操作说明为2026-09-30能力快照；LibTV图片五项设置说明于2026-10-08补充核对。使用其他版本时，按实际界面和已核验的官方说明适配。

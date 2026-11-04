# 《中式美学丨古风胶片》来源与覆盖

- 来源：[用户提供的画布副本](https://www.liblib.tv/canvas?projectId=e0f245338b3b41d0812c967bd5d963b4&spaceId=11187652&forceAgent=1)，页面标题《中式美学丨古风胶片- 副本》。读取日期：2026-10-12。未另行核实作者与公开发布版本。
- 界面共70节点：4分组＋66独立节点。逐一选中66个不同ID，核对选中名称及编辑区；包含43图片、19视频、4文本。可见连线19条。
- 41个图片节点有非空独立提示词，其中40个当前面板为Style Image（38个V8.2、2个V8.1），1个为Lib Image；19个视频节点均有正文，当前面板为Kling 3.0。合计60条节点提示词，按原始textContent精确去重为59条；不删除重复来源记录。
- 两个图片素材节点 i-nSfBvpIxoX、i-70PGPR5tYr 没有可见独立提示词。前者为“中式美学-东方胶片”工具卡截图，图内文字单独转录在source-context中，不是参数截图，也不能据此调用图中工具；后者为带字封面。4个文本节点只有“可以用这个”“图生视频”“测试丨确定组”“测试丨废片组”标记，没有独立的长篇教程。
- 原文完整保存于 [portrait-source-prompts.md](portrait-source-prompts.md)，短文本在 [portrait-source-context.md](portrait-source-context.md)；逐节点原始文本、渲染文本、引用标签、当前面板值、连线在 [portrait-source-corpus.json](portrait-source-corpus.json)。校验值在 [portrait-offline-manifest.json](portrait-offline-manifest.json)。这些是离线底版，后续新作不能改写它们。
- 新归纳在 [portrait-mj.md](portrait-mj.md)，新写示例在 [portrait-templates.md](portrait-templates.md)。不把分析冒充原作者明示规则。

## 分组决定证据的用途

| 页面分组 | 内部文字标记 | 内容 | 迁移权重 |
| --- | --- | --- | --- |
| g-YcWDyNhYLH / 2节点 | 可以用这个 | 1文本＋1图片素材 | 只有简短说明，不能据此推导参数 |
| g-vdXbSEuICT / 20节点 | 图生视频 | 19视频提示词＋1文本 | 用于检查首帧延续和克制动作；不改半生默认Kling O3交付约定 |
| g-O4pLmcOQx6 / 21节点 | 测试丨确定组 | 20个Style Image V8.2图片提示词＋1文本 | 新分支的主要证据；“确定”是来源标记，不等于逐项正确或正式成片全部采用 |
| g-6h1gQSJOaO / 22节点 | 测试丨废片组 | 20个Style Image图片提示词、1个Lib Image提示词＋1文本 | 原样归档，用于变体与风险对照；不能推断每个废弃原因，也不能因其中出现某个词就判定该词无效 |
| 未分组 | 无 | 1带字图片素材 | 没有独立提示词 |

## 核心证据定位

| 可复用判断 | 来源节点 |
| --- | --- |
| 主体、手势、机位、框中框要明确；正面版比早期版本更具体 | i-bGEaeYKpvt（确定组）、i-rGTJ3k0y2Z（废片组） |
| 眼睛与近处剑锋分出清晰层级，遮挡不等于无规则盖脸 | i-4oJob4bBnL、i-9CEYmOhAFW、i-QbgIWtEAqJ |
| 斗笠遮眼是特定悬念构图，不是人物版人人露眼的例外漏洞 | i-PZZspKIPu2；与透光纱笠 i-Ykk78InhCT 分开 |
| 冷环境＋小范围暖光应落到人物脸与手 | i-WkOY2ZAkDx、i-qKOuS0q75F |
| 双人关系通过触点、目光与动作分工表达 | i-sTYtLffLL3、i-SYpT9cQbES、i-G9RHAJSHYd |
| 动物是关系主体，必须说明接触与体型关系 | i-udVnLFcpSu、i-XGRrzIiEi3 |
| 人物优先仍可以三分之二身或中远景 | i-IbtCYruTOC、i-Ykk78InhCT |
| 白昼、暖暮光都在确定组，不能一律午夜青绿 | i-bGEaeYKpvt、i-G9RHAJSHYd、i-IbtCYruTOC |
| 民国属于来源支线，不混入古代服饰 | i-HSOWZed2EH：旗袍、针织开衫、茶室 |
| 重雾、蒙雾老镜头、欠曝、低微反差叠加属于探索变体 | i-5imseQo6Zr、i-7EAXiW7mBs、i-nW8UzRo8ts、i-vQpmizcfg9、i-Zr2kFxi8UB |
| 风格串可以独立存在，但不是完整的人物提示词 | i-lAD6is3gTE、i-60WaxTBItS、i-WxuWRqg3Gv、i-XpKJUWBb93 |

## 当前参数与历史不能混为一谈

确定组大量正文末尾为 `--chaos 25 --ar 16:9 --raw --stylize 400`，未写版本。读到的面板显示Style Image V8.2、16:9、自适应、4张；高级设置现值为风格化100、怪异度50、多样性5。保存这两组事实，不能确定当时提交生效值或平台后缀/滑杆优先级。

i-lAD6is3gTE 与 i-WxuWRqg3Gv 的原文含 `——混乱25-ar 16:9-raw——sref 4029852131-sv 4--styleze 400`。这不是可靠可直接执行的MJ参数串。原文照存；新作按正确英文参数重写。这个sref只出现在废片组的损坏文本中，未验证其风格，不能将它认定为确定组成图的共同秘密配方。

i-5imseQo6Zr、i-WxuWRqg3Gv 当前面板V8.1；i-nW8UzRo8ts 为Lib Image。不能把它们全部记作已验证的MJ V8.2生成记录。i-yAclC8k65u 与 i-x917RpYHdA 为精确同文，分别属于确定组与废片组；分组评价不应替代对具体任务的判断。

## 观察边界与图文错配

实际查看的是画布当前选中的缩略/预览画面：i-bGEaeYKpvt（窗后）、i-WkOY2ZAkDx（荷叶灯影）、i-sTYtLffLL3（簪发）、i-nW8UzRo8ts（废片组吹笛）、i-70PGPR5tYr（封面）及i-nSfBvpIxoX（工具卡截图）。人物样图支持柔化边缘、前景层次与人物优先的观察，不足以证明每个词的独立作用。未逐张展开4张候选、未检查所有生成历史、未完整观看视频、未重跑生成或做参数对照实验。归纳不是实测配方。

连线也不保证当前两端文本同一版本：i-yAclC8k65u 当前图片正文为持铜镜，关联 v-k9gfs7n3z6k2 却写月下持荷叶，页面还显示输入已更新；i-G9RHAJSHYd 写女子骑马、男子站在马前扶臂，关联视频写两人共乘。i-S1Kr2bllSA 图片写浅青衣、提灯，视频写白衣及右侧灯笼。不得直接拼接成“严格继承首帧”。新视频必须重新看实际选图。

本次仅做读取与本地整理，没有修改画布原文或提交生图/生视频。


## 全节点检索表

| 节点ID | 分组标记 | 检索名（整理者补充） | 类型/正文 |
| --- | --- | --- | --- |
| t-3oHukMSai7 | 可以用这个 | 文本节点 1 - 副本 | text / group-label |
| i-nSfBvpIxoX | 可以用这个 | 东方胶片工具卡截图 | image / no-visible-independent-prompt |
| v-Fq9cFuHyDb | 图生视频 | 视频节点 1 | video / video-prompt |
| v-OPZ8GioB2E | 图生视频 | 视频节点 2 | video / video-prompt |
| v-6tucu8qhrtyx | 图生视频 | 图片01｜窗后凝望 | video / video-prompt |
| v-hkpjf2yne829 | 图生视频 | 图片01｜廊下微光 | video / video-prompt |
| v-ayzuxk5aqcyq | 图生视频 | 图片02｜白虎听雨 | video / video-prompt |
| v-k9gfs7n3z6k2 | 图生视频 | 图片02｜月下持叶 | video / video-prompt |
| v-dxwpzk4nsrw2 | 图生视频 | 图片03｜亭中对弈 | video / video-prompt |
| v-q2xn8a5jk6rg | 图生视频 | 图片03｜戏台逼剑 | video / video-prompt |
| v-c57qg9r3tmz2 | 图生视频 | 图片04｜林间藏锋 | video / video-prompt |
| v-hhf2dkepzf86 | 图生视频 | 图片04｜雪庭回望 | video / video-prompt |
| v-r723mhh3rc6k | 图生视频 | 图片05｜白衣剑指 | video / video-prompt |
| v-khey5w49f6bz | 图生视频 | 图片05｜荷叶灯影 | video / video-prompt |
| v-ms7dqw5vpdw8 | 图生视频 | 图片06｜怀中白狐 | video / video-prompt |
| v-g94qgx24457r | 图生视频 | 图片07｜窗边翻页 | video / video-prompt |
| v-3xnkmd92yvzk | 图生视频 | 图片07｜共乘疾行 | video / video-prompt |
| v-vbskd77evaqm | 图生视频 | 图片08｜风起斗笠 | video / video-prompt |
| v-s3ru8penzv5f | 图生视频 | 图片08｜簪发密语 | video / video-prompt |
| v-6rafbfryxpu7 | 图生视频 | 图片09｜苇海执扇 | video / video-prompt |
| v-vky5y5vwcf75 | 图生视频 | 图片09｜倚柱吹笛 | video / video-prompt |
| t-sgflaAnguC | 图生视频 | 文本节点 1 - 副本 | text / group-label |
| i-3hv4jfutYM | 测试丨确定组 | 戏台剑姿 | image / mj-labeled-image-prompt |
| i-4oJob4bBnL | 测试丨确定组 | 白衣剑指 | image / mj-labeled-image-prompt |
| i-9CEYmOhAFW | 测试丨确定组 | 林间藏锋 | image / mj-labeled-image-prompt |
| i-bGEaeYKpvt | 测试丨确定组 | 窗后凝望·正面明确版 | image / mj-labeled-image-prompt |
| i-G9RHAJSHYd | 测试丨确定组 | 骑马扶臂·人物关系 | image / mj-labeled-image-prompt |
| i-HSOWZed2EH | 测试丨确定组 | 窗边读书·民国支线 | image / mj-labeled-image-prompt |
| i-IbtCYruTOC | 测试丨确定组 | 苇海执扇 | image / mj-labeled-image-prompt |
| i-ipmJZU4EQD | 测试丨确定组 | 雪庭回望 | image / mj-labeled-image-prompt |
| i-PZZspKIPu2 | 测试丨确定组 | 斗笠遮眼 | image / mj-labeled-image-prompt |
| i-QbgIWtEAqJ | 测试丨确定组 | 横剑近景 | image / mj-labeled-image-prompt |
| i-qKOuS0q75F | 测试丨确定组 | 廊下护烛 | image / mj-labeled-image-prompt |
| i-S1Kr2bllSA | 测试丨确定组 | 雨廊伞灯 | image / mj-labeled-image-prompt |
| i-sTYtLffLL3 | 测试丨确定组 | 簪发密语 | image / mj-labeled-image-prompt |
| i-SYpT9cQbES | 测试丨确定组 | 亭中对弈 | image / mj-labeled-image-prompt |
| i-udVnLFcpSu | 测试丨确定组 | 怀中白狐 | image / mj-labeled-image-prompt |
| i-WkOY2ZAkDx | 测试丨确定组 | 荷叶灯影 | image / mj-labeled-image-prompt |
| i-XGRrzIiEi3 | 测试丨确定组 | 白虎听雨 | image / mj-labeled-image-prompt |
| i-yAclC8k65u | 测试丨确定组 | 持镜·短提示词 | image / mj-labeled-image-prompt |
| i-Ykk78InhCT | 测试丨确定组 | 风起斗笠 | image / mj-labeled-image-prompt |
| i-z3ac03zzU8 | 测试丨确定组 | 倚柱吹笛 | image / mj-labeled-image-prompt |
| t-RmQRJSGSk5 | 测试丨确定组 | 文本节点 1 - 副本 | text / group-label |
| i-lAD6is3gTE | 测试丨废片组 | 中文风格串·损坏后缀 | image / mj-labeled-image-prompt |
| i-1ND8HEg0EI | 测试丨废片组 | 庭院照镜 | image / mj-labeled-image-prompt |
| i-5imseQo6Zr | 测试丨废片组 | 港式志怪·纯风格串 | image / mj-labeled-image-prompt |
| i-60WaxTBItS | 测试丨废片组 | 中文风格串·无参数 | image / mj-labeled-image-prompt |
| i-6o8f91Ql5r | 测试丨废片组 | 石窟献莲·尺度实验 | image / mj-labeled-image-prompt |
| i-7EAXiW7mBs | 测试丨废片组 | 溪边吹笛·重柔化 | image / mj-labeled-image-prompt |
| i-BS94AHfAdY | 测试丨废片组 | 黑衣剑客·涉水 | image / mj-labeled-image-prompt |
| i-cVwQ0BBuLo | 测试丨废片组 | 溪边吹笛·材质叠加 | image / mj-labeled-image-prompt |
| i-DEmDr8gcNj | 测试丨废片组 | 双人交剑 | image / mj-labeled-image-prompt |
| i-fQMhirmwm6 | 测试丨废片组 | 药庐包扎 | image / mj-labeled-image-prompt |
| i-jVbZfHyLCA | 测试丨废片组 | 雨廊携手 | image / mj-labeled-image-prompt |
| i-nuMWAytjBb | 测试丨废片组 | 竹林红伞·短提示词 | image / mj-labeled-image-prompt |
| i-nW8UzRo8ts | 测试丨废片组 | 芦苇吹笛·Lib Image | image / other-model-image-prompt |
| i-RgOh2jYfFB | 测试丨废片组 | 倚柱吹笛·无后缀 | image / mj-labeled-image-prompt |
| i-rGTJ3k0y2Z | 测试丨废片组 | 窗后凝望·早期版 | image / mj-labeled-image-prompt |
| i-rnDfODAGsM | 测试丨废片组 | 芦苇吹笛·八十年代幻想 | image / mj-labeled-image-prompt |
| i-vQpmizcfg9 | 测试丨废片组 | 寺阶剑客·旧镜头 | image / mj-labeled-image-prompt |
| i-WxuWRqg3Gv | 测试丨废片组 | 中文风格串·第二条损坏后缀 | image / mj-labeled-image-prompt |
| i-x917RpYHdA | 测试丨废片组 | 持镜·短提示词同文 | image / mj-labeled-image-prompt |
| i-XpKJUWBb93 | 测试丨废片组 | 英文纯风格串 | image / mj-labeled-image-prompt |
| i-Zr2kFxi8UB | 测试丨废片组 | 桥上提灯·旧镜头 | image / mj-labeled-image-prompt |
| t-ycnE17FIrg | 测试丨废片组 | 文本节点 1 | text / group-label |
| i-70PGPR5tYr | 未分组 | 带字封面素材 | image / no-visible-independent-prompt |
| g-YcWDyNhYLH | 可以用这个 | 分组 2 个节点 | group |
| g-vdXbSEuICT | 图生视频 | 分组 20 个节点 | group |
| g-O4pLmcOQx6 | 测试丨确定组 | 分组 21 个节点 | group |
| g-6h1gQSJOaO | 测试丨废片组 | 分组 22 个节点 | group |

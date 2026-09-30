# 项目原文索引与覆盖范围

项目：[《半生》｜诗里白头，一眼半生- 副本](https://www.liblib.tv/canvas?projectId=ea3601395fc44d7eb962b3f75270b247&spaceId=10244732)；保存日期2026-09-30。

## 已完成的核对

150个节点＝5个分组＋145个独立节点；逐一访问145个独立节点并核对唯一节点ID。所有60个文本节点有完整正文；25个图片节点有独立生成/编辑提示词。81条提示词完整保留，另存4条人物资料。

| 节点类型 | 数量 | 正文处理 |
| --- | ---: | --- |
| text | 60 | 56条提示词＋4条人物资料，完整保留 |
| image | 46 | 25个有独立提示词，其余为无独立提示词的素材节点 |
| video | 34 | 检查选中节点编辑区；未发现独立非空提示词，保留关联输入与UI信息 |
| audio | 2 | 人物声音素材，无独立提示词正文 |
| material-style | 3 | 3项样式图片引用，仅见名称与图片，无展开的提示词正文 |
| group | 5 | 保留分组名称 |

空字段并非遗漏，不凭空补齐。视频往往使用连接的文本提示词节点；具体关系见source-corpus.json中的incomingNodeIds和edges。UI快照不包含平台隐藏提示词和旧版本历史。

## 分组与写法

| 分组 | 图片分镜 | 视频分镜 | 图片节点提示词 | 人物资料 |
| --- | ---: | ---: | ---: | ---: |
| 封面设计 | 0 | 0 | 19 | 0 |
| 柳宗元 | 6 | 7 | 4 | 1 |
| 陆游 | 6 | 8 | 1 | 1 |
| 苏轼 | 6 | 8 | 1 | 1 |
| 辛弃疾 | 6 | 9 | 0 | 1 |

分类用于检索：包含主体、拍摄风格和情节段落的分镜文本归为视频提示词；其余分镜文本归为图片提示词。这是归档标签，不改正文。

检索词：

- 柳宗元：长街、朝堂、红衣、孤舟、蓑笠、寒江雪。
- 陆游：边关、骑兵、拉弓、老将、病榻、示儿。
- 苏轼：春宴、酒杯、灯笼、竹林、雨路、释然。
- 辛弃疾：夜营、白马、银枪、火星、老者、挑灯看剑。
- 共通：首帧、单镜头、眼神、冷青、暖金、负空间、遮挡转场。

## 来源与派生内容分开

- source-prompts.md：81条提示词原文，包括重复记录。
- source-context.md：4条人物资料原文。
- source-corpus.json：150个节点、可见连线、提示词、UI文本和媒体溯源地址。
- offline-manifest.json：原文底版的SHA-256，便于确认没有被改写。
- visual-dna.md：从原文和少量观察画面提炼的视觉判断。
- templates.md：新写的组织模板、虚构案例与条件视频示例。
- manual-steps.md：给用户的手动生图/生视频操作，本地保存平台能力快照。

素材与影片没有下载进技能，运行不依赖这些媒体链接。要匹配新视频首帧，需实际查看用户回传的选定图片。

## 全节点查阅索引

| 节点ID | 分组 | 名称 | 类型/分类 |
| --- | --- | --- | --- |
| t-2hHJG3W1Ij | 柳宗元 | 提示词 | text / video-prompt |
| t-AXhwC45P9x | 柳宗元 | 提示词 | text / image-prompt |
| t-bO3405c6tq | 柳宗元 | 提示词 | text / video-prompt |
| t-CexjUXFJZP | 柳宗元 | 提示词 | text / video-prompt |
| t-EEv230uKic | 柳宗元 | 提示词 | text / image-prompt |
| t-ErC9mbY9Jw | 柳宗元 | 提示词 | text / image-prompt |
| t-nmnrlPD0NN | 柳宗元 | 提示词 | text / video-prompt |
| t-QPv2Tknf4S | 柳宗元 | 提示词 | text / image-prompt |
| t-RTL7BKEhEF | 柳宗元 | 提示词 | text / image-prompt |
| t-SAp4VqjvZb | 柳宗元 | 提示词 | text / video-prompt |
| t-SOng1dNhOc | 柳宗元 | 提示词 | text / image-prompt |
| t-t6JxAG032a | 柳宗元 | 提示词 | text / video-prompt |
| t-UJvdJs8g0e | 柳宗元 | 提示词 | text / video-prompt |
| t-5RfMaR6An6 | 陆游 | 提示词 | text / image-prompt |
| t-86vvD0bbfR | 陆游 | 提示词 | text / image-prompt |
| t-c0rdY35UC6 | 陆游 | 提示词 | text / video-prompt |
| t-dLzD5ROaW0 | 陆游 | 提示词 | text / image-prompt |
| t-E4OB4REddr | 陆游 | 提示词 | text / video-prompt |
| t-F5OKlzdazP | 陆游 | 提示词 | text / video-prompt |
| t-G71vuNgrnX | 陆游 | 提示词 | text / image-prompt |
| t-kLJ8VPUbpR | 陆游 | 提示词 | text / video-prompt |
| t-oRECtQrRwj | 陆游 | 提示词 | text / image-prompt |
| t-pYdGhhWyGT | 陆游 | 提示词 | text / video-prompt |
| t-qo3FutBeWM | 陆游 | 提示词 | text / video-prompt |
| t-RvQUyQ5Jro | 陆游 | 提示词 | text / video-prompt |
| t-sgIyZjGGTk | 陆游 | 提示词 | text / image-prompt |
| t-tSz0mX1vED | 陆游 | 提示词 | text / video-prompt |
| t-4uTNfzP2DV | 苏轼 | 提示词 | text / video-prompt |
| t-87I2cLsQ3K | 苏轼 | 提示词 | text / video-prompt |
| t-8Hriu290zj | 苏轼 | 提示词 | text / image-prompt |
| t-fEEbn20FVM | 苏轼 | 提示词 | text / image-prompt |
| t-KScTxKWmf0 | 苏轼 | 提示词 | text / image-prompt |
| t-OSV6W8D7np | 苏轼 | 提示词 | text / image-prompt |
| t-qIan56GpDb | 苏轼 | 提示词 | text / video-prompt |
| t-QNZArWtGDV | 苏轼 | 提示词 | text / image-prompt |
| t-sANga8iULI | 苏轼 | 提示词 | text / video-prompt |
| t-SWcAUXnwWP | 苏轼 | 提示词 | text / image-prompt |
| t-uSWIDzTh9v | 苏轼 | 提示词 | text / video-prompt |
| t-WV8ftwo4jZ | 苏轼 | 提示词 | text / video-prompt |
| t-x6vORXDIEW | 苏轼 | 提示词 | text / video-prompt |
| t-yNwqkWcDhn | 苏轼 | 提示词 | text / video-prompt |
| t-023eocyALT | 辛弃疾 | 提示词 | text / video-prompt |
| t-0GMAJ5kdl0 | 辛弃疾 | 提示词 | text / video-prompt |
| t-17ymGQl5ME | 辛弃疾 | 提示词 | text / image-prompt |
| t-2lpAtjpNKV | 辛弃疾 | 提示词 | text / image-prompt |
| t-FcTTTxCCoE | 辛弃疾 | 提示词 | text / video-prompt |
| t-fXmqsaU3lA | 辛弃疾 | 提示词 | text / image-prompt |
| t-kMgmMybhD1 | 辛弃疾 | 提示词 | text / image-prompt |
| t-l2oth8nQdt | 辛弃疾 | 提示词 | text / image-prompt |
| t-lc5jKzIdlk | 辛弃疾 | 提示词 | text / image-prompt |
| t-rY8rPjjd5D | 辛弃疾 | 提示词 | text / video-prompt |
| t-s49UWE71TO | 辛弃疾 | 提示词 | text / video-prompt |
| t-t5AArCHRw3 | 辛弃疾 | 提示词 | text / video-prompt |
| t-VZFPDwAZbb | 辛弃疾 | 提示词 | text / video-prompt |
| t-YCwUbH5u0o | 辛弃疾 | 提示词 | text / video-prompt |
| t-z87q3qzmZl | 辛弃疾 | 提示词 | text / video-prompt |
| i-5tSXUptDZh | 封面设计 | 封面 | image / image-node-prompt |
| i-8Q8UiCeNta | 封面设计 | 封面 | image / image-node-prompt |
| i-8vgdoUB6Vs | 封面设计 | 封面 | image / image-node-prompt |
| i-AaSznxZIN7 | 封面设计 | 封面 | image / image-node-prompt |
| i-BizHUASU5r | 封面设计 | 封面 | image / no-independent-prompt |
| i-BObjqszvYd | 封面设计 | 封面 | image / image-node-prompt |
| i-bvwZlFqo9g | 封面设计 | 封面 | image / image-node-prompt |
| i-iqDHOML5Sz | 封面设计 | 封面 | image / image-node-prompt |
| i-K1DprXYMFl | 封面设计 | 封面 | image / no-independent-prompt |
| i-oDoSENYzAp | 封面设计 | 封面 | image / image-node-prompt |
| i-pS8z4FdBwu | 封面设计 | 封面 | image / image-node-prompt |
| i-VtdETbj4OC | 封面设计 | 封面 | image / image-node-prompt |
| i-wSyxp0lWEk | 封面设计 | 封面 | image / image-node-prompt |
| i-wV8svSrTWG | 封面设计 | 封面 | image / image-node-prompt |
| i-6V5yJvW8cT | 封面设计 | 封面-标题设计 | image / image-node-prompt |
| i-SO6WREP0uG | 封面设计 | 封面-标题设计 | image / image-node-prompt |
| i-znF6NqUj7D | 封面设计 | 封面-标题设计v2 | image / image-node-prompt |
| i-TnEr0PtjZW | 封面设计 | 人物印章设计 | image / image-node-prompt |
| i-Hw58ojIX2L | 封面设计 | 人物印章设计v2 | image / image-node-prompt |
| i-wE9EXEDnjO | 封面设计 | 人物印章设计v3 | image / image-node-prompt |
| m-Qpk2a9wmSq | 封面设计 | 素材-风格-一键｜国风书法印章封面 | material-style / no-independent-prompt |
| m-s4T1qGNpM6 | 封面设计 | 素材-风格-一键｜手书印章生成器 - 副本 | material-style / no-independent-prompt |
| m-CLvKSwE5JV | 封面设计 | 素材-风格-一键｜手写艺术字｜标题｜封面 - 副本 | material-style / no-independent-prompt |
| i-VSzaFZwHRQ | 封面设计 | 图片节点 30 | image / image-node-prompt |
| i-6KX92iGEwi | 封面设计 | image | image / no-independent-prompt |
| v-aoyev3qdtH | 柳宗元 | 生成视频 | video / no-independent-prompt |
| v-awCt970EWj | 柳宗元 | 生成视频 | video / no-independent-prompt |
| v-CXy9vPp2vo | 柳宗元 | 生成视频 | video / no-independent-prompt |
| v-LRzIteGtcj | 柳宗元 | 生成视频 | video / no-independent-prompt |
| v-n9BSeMeWC9 | 柳宗元 | 生成视频 | video / no-independent-prompt |
| v-UmhgHD0jYQ | 柳宗元 | 生成视频 | video / no-independent-prompt |
| v-UOBT69Tztz | 柳宗元 | 生成视频 | video / no-independent-prompt |
| i-a7uT2HGqg1 | 柳宗元 | image | image / image-node-prompt |
| i-F0lofWOHOE | 柳宗元 | image | image / no-independent-prompt |
| i-HBa4Gggf2P | 柳宗元 | image | image / image-node-prompt |
| i-viH5XM5oLW | 柳宗元 | image | image / image-node-prompt |
| i-WbHjAtkjxN | 柳宗元 | image | image / image-node-prompt |
| i-ZbxfP02BjM | 柳宗元 | image | image / no-independent-prompt |
| t-7uIKjCz5nE | 柳宗元 | 柳宗元 | text / context |
| v-19528fYIlo | 陆游 | 生成视频 | video / no-independent-prompt |
| v-eF7IhouZf3 | 陆游 | 生成视频 | video / no-independent-prompt |
| v-H8mlnkfVGO | 陆游 | 生成视频 | video / no-independent-prompt |
| v-iYHn7Xk4wK | 陆游 | 生成视频 | video / no-independent-prompt |
| v-kkno64iJFB | 陆游 | 生成视频 | video / no-independent-prompt |
| v-MWcCL6fnjo | 陆游 | 生成视频 | video / no-independent-prompt |
| v-PWEn3XJ0w9 | 陆游 | 生成视频 | video / no-independent-prompt |
| v-UX8gpJiKqs | 陆游 | 生成视频 | video / no-independent-prompt |
| a-aDAVjJEg12 | 陆游 | 生成视频_人声 | audio / no-independent-prompt |
| a-s5gqaVHLcS | 陆游 | 生成视频_人声 | audio / no-independent-prompt |
| v-NkAa9CZWIU | 陆游 | 生成视频_无声 | video / no-independent-prompt |
| v-OtNxH3hQcu | 陆游 | 生成视频_无声 | video / no-independent-prompt |
| i-hWgIkQYPV6 | 陆游 | 图片节点 4 - 副本 | image / image-node-prompt |
| i-RGYMPcg9un | 陆游 | g_jason_jason_Wide_horizontal_dynamic_action_medium_shot_in_1_e40d1a9b-3ecc-46af-88c2-b7bf6813c8cc_1 - 副本 | image / no-independent-prompt |
| i-9rnL7tguTF | 陆游 | image | image / no-independent-prompt |
| i-eaAFltmw1k | 陆游 | image | image / no-independent-prompt |
| i-puJZHyAc9j | 陆游 | image | image / no-independent-prompt |
| i-SRyF6U6A40 | 陆游 | image | image / no-independent-prompt |
| t-9lBMvvCl4j | 陆游 | 陆游 | text / context |
| v-4J0FdoHLh8 | 苏轼 | 生成视频 | video / no-independent-prompt |
| v-4UnJiaAjEh | 苏轼 | 生成视频 | video / no-independent-prompt |
| v-8VQGjpqbGw | 苏轼 | 生成视频 | video / no-independent-prompt |
| v-CesN7mffM4 | 苏轼 | 生成视频 | video / no-independent-prompt |
| v-E0w0SgaSi1 | 苏轼 | 生成视频 | video / no-independent-prompt |
| v-EJbbXafeFq | 苏轼 | 生成视频 | video / no-independent-prompt |
| v-JifpoZI3lp | 苏轼 | 生成视频 | video / no-independent-prompt |
| v-urKgvJcEOw | 苏轼 | 生成视频 | video / no-independent-prompt |
| i-at8rGfuHho | 苏轼 | image | image / no-independent-prompt |
| i-B4iqfbE50r | 苏轼 | image | image / no-independent-prompt |
| i-JCyNoJnXn0 | 苏轼 | image | image / no-independent-prompt |
| i-kYdzhSwNm8 | 苏轼 | image | image / image-node-prompt |
| i-trCaQhXFuq | 苏轼 | image | image / no-independent-prompt |
| i-YVwLS6DC02 | 苏轼 | image | image / no-independent-prompt |
| t-A8goSWlyY9 | 苏轼 | 苏轼 | text / context |
| v-0SDC2opNN9 | 辛弃疾 | 生成视频 | video / no-independent-prompt |
| v-2xbE4iiDsB | 辛弃疾 | 生成视频 | video / no-independent-prompt |
| v-av2lH6tWi5 | 辛弃疾 | 生成视频 | video / no-independent-prompt |
| v-BFc6cnweQE | 辛弃疾 | 生成视频 | video / no-independent-prompt |
| v-iT85WbrKQO | 辛弃疾 | 生成视频 | video / no-independent-prompt |
| v-Jfw5iXduxj | 辛弃疾 | 生成视频 | video / no-independent-prompt |
| v-PHET1jPgiT | 辛弃疾 | 生成视频 | video / no-independent-prompt |
| v-ZFxg9G7lO5 | 辛弃疾 | 生成视频 | video / no-independent-prompt |
| v-wFGT3VDe9u | 辛弃疾 | 生成视频v2 | video / no-independent-prompt |
| i-4tnfIOEXJc | 辛弃疾 | image | image / no-independent-prompt |
| i-7FSa77nVEG | 辛弃疾 | image | image / no-independent-prompt |
| i-CX3CFHuWqf | 辛弃疾 | image | image / no-independent-prompt |
| i-ffQZ7JUm3E | 辛弃疾 | image | image / no-independent-prompt |
| i-GLPsBujOWd | 辛弃疾 | image | image / no-independent-prompt |
| i-lo9CaYONEO | 辛弃疾 | image | image / no-independent-prompt |
| t-WdO0NYxx0Z | 辛弃疾 | 辛弃疾 | text / context |
| g-HGBdyNWw05 | 封面设计 | 封面设计 | group / group |
| g-5bax1j8Qa0 | 柳宗元 | 柳宗元 | group / group |
| g-XndjKOC7P0 | 陆游 | 陆游 | group / group |
| g-joxpV1Njqv | 苏轼 | 苏轼 | group / group |
| g-RxSqcbxDlI | 辛弃疾 | 辛弃疾 | group / group |

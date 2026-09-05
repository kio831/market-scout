# V3 Evidence Layer — 市场证据层（v3.0.0 新增）

> V2 已经有三类搜索（Problem/Solution/Payment）与证据链五段式；
> V3 在其上增加"证据三态归一化"，让每个结论都能一眼看出它到底有多少依据。
> 本文件是 V3 主流程第 4 步 EVIDENCE 的方法定义，方法基础全部复用 `evidence-chain.md` 与 `market-research.md` §0。

## 1. 证据三态（Evidence / Inference / Unknown）

V3 报告中，每个关键结论必须标注三态之一：

| 状态 | 含义 | 判定 |
|---|---|---|
| **Evidence** | 实际找到的公开信息，可引用来源 | 有链接/原文/截图/官方页面/访谈记录/现实观察 |
| **Inference** | AI 根据证据推导出的判断 | 有证据支撑，但结论超出证据字面（合理延伸） |
| **Unknown** | 目前没有足够信息确认 | 搜不到、用户没提供、无法核实 |

示例：

```text
Evidence:   多个用户在公开社区讨论同一个问题（3 个独立来源，附链接）。
Inference:  该问题可能存在持续需求（推断：多个独立来源指向同类问题）。
Unknown:    目前无法确认这些用户是否愿意付费（未找到在售服务/报价/成交）。
```

## 2. 与 V2 证据链/证据等级的映射（复用，不另起炉灶）

| V2 概念 | V3 三态 | 关系 |
|---|---|---|
| 证据链"事实（Observation）" | Evidence | 一一对应 |
| 证据链"推断（Inference）" | Inference | 一一对应 |
| 证据链"假设（Hypothesis）" | Inference（标注"假设"） | 假设 = 未验证推断，不得当 Evidence |
| 证据等级 A/B/C | 与三态正交 | A/B/C 描述"需求验证程度"，三态描述"单条结论的依据类型" |
| 【证据不足】 | Unknown | 一一对应 |

规则：

- 没有来源的模型记忆 → Unknown，禁止写成 Evidence。
- 单条证据的字面含义 = Evidence；任何延伸解读 = Inference。
- "搜索不到"只能写 Unknown / 未找到公开证据，不能写成"不存在"。
- 证据升级必须有新增真实证据（新来源、新付费迹象），沿用 `problem-framework.md` §3 禁止规则。

## 3. 证据充分度（Evidence Sufficiency）

对一次 V3 决策，按关键问题逐个评估依据后汇总三级：

| 级别 | 判定 |
|---|---|
| **Sufficient 充分** | 关键结论以 Evidence 为主；至少同时满足：问题真实（≥2 个独立来源）+ 现有方案已查证 + 付费信号（至少 Inference 且有明确验证路径） |
| **Partial 部分** | 关键结论部分是 Inference/Unknown；缺 1-2 类关键证据（最常见：缺付费证据） |
| **Insufficient 不足** | 连"问题是否真实存在"都无法确认，或关键结论几乎全部 Unknown |

**Insufficient 是熔断信号**：不评分、不编造，输出 Evidence Insufficient 横幅 + 缺什么 + 去哪补（对应三类搜索之一），Decision 按 `v3-decision.md` §4 处理。

## 4. 证据看板（Evidence Board）

把本次决策用到的关键结论整理成看板，每个结论一行（`templates/v3-evidence-board.md`）：

| 结论 | 状态 | 来源 | 置信度 | 证明什么 / 不能证明什么 |
|---|---|---|---|---|
| ... | Evidence/Inference/Unknown | ... | 高/中/低 | ... |

- 三态数量一目了然；Evidence 太少 → 充分度下调。
- 看板中每条 Evidence 必须能追溯到 Evidence Card（`templates/evidence-card.md`）或注明来源链接。
- 置信度口径沿用 `evidence-chain.md` §4（高=一手可复核 / 中=二手清晰 / 低=来源不明）。

## 5. 评分中的三态处理

- 每个子信号分必须标注三态（`v3-scoring.md` §2.4）。
- Unknown 子信号 → 按 0 计（保守），并显式说明"因证据不足按 0 计，本维度被低估，补齐证据后重算"。
- Inference 子信号 → 最高 7/10（未验证的推断不得满分）。
- Evidence 子信号 → 无上限。
- 不得为了让分数好看把 Unknown 悄悄升级成 Inference。

## 6. 不编造铁律（P0）

- 禁止虚构用户、价格、成交、数据、评论、来源。
- 禁止"市场很大""前景广阔"等无证据结论。
- 证据不足就写 Unknown / 【证据不足】，宁可结论保守。
- 搜索能力不可用时，声明【当前无法进行实时市场验证，以下属于假设分析】，全部结论标 Unknown 或 Inference（假设），沿用 V1.1 铁律 2。

## 7. 输出

- 使用 `templates/v3-evidence-board.md`：关键结论看板 + 三态统计 + 缺失证据清单（去哪补）。
- 看板是 SCORING/DECISION 的直接依据：评分与决策引用的每条证据都能在看板中找到。

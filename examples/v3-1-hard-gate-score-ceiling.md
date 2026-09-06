# 示例：高总分被 Score Ceiling 拦下（v3.1.0）

> ⚠️ 演示数据：仅展示方法。
> 本示例对应 SOP Case D 与矩阵"Payment Missing"：总分 81，Monetization 维度分正常，
> 但**付费证据覆盖不足**，按规则最高只能 POTENTIAL——总分不能掩盖关键证据缺口。

## 用户输入

"我想做一个 AI 宠物寄养商家的一键订房/预约工具。我查到很多商家都在用微信接单，感觉需求很大。"

## 1. Score

| 维度 | 分 | 简述 |
|---|---|---|
| Demand | 88 | 商家吐槽多（Evidence 示意） |
| Pain | 84 | 接单乱、漏单（Evidence 示意） |
| Competition | 80 | 现有工具不垂直（Inference） |
| Monetization | 68 | 听到商家"愿意按月付"（Inference，无价格证据） |
| Buildability | 90 | L2 轻开发即可 |
| Distribution | 78 | 商家群可触达（Evidence 示意） |
| AI Advantage | 82 | 消息解析是 AI 成熟区（Evidence 示意） |

```text
Score = 88×.15+84×.15+80×.15+68×.20+90×.15+78×.10+82×.10
     = 13.2+12.6+12.0+13.6+13.5+7.8+8.2 = 80.9 → 81/100
```

## 2. Evidence Coverage

| 维度 | 覆盖分 | status |
|---|---|---|
| Problem | 85 | covered |
| Solution | 70 | covered |
| **Payment** | **25** | **insufficient** |
| Competition | 80 | covered |
| Distribution | 60 | partial |
| Buildability | 80 | covered |

overall = round((85+70+25+80+60+80)/6) = **67/100**
critical_gaps：**payment evidence**（关键维度缺口，不因整体 67 分被忽略）

## 3. Confidence

```text
U = 2/26 ≈ 0.08；CC = min(25, 85) = 25
Confidence Score = 0.30×67 + 0.20×0.92×100 + 0.35×25 + 0.15×100
                 = 20.1 + 18.4 + 8.75 + 15 = 62.25 → 62
Level: Medium(62)；覆盖规则 O1（Payment 25 < 30）→ ≤ Medium → Medium
```

**Confidence = Medium**（限制因素：payment 覆盖不足）。

## 4. Hard Gates（命中的不是门槛，是天花板）

| Gate | 结果 | 原因 |
|---|---|---|
| G1-G5 | 全部 PASS | Monetization 68 ≥ 45，其余维度均过线 |
| **C1 Payment** | **CEILING** | Payment 覆盖 25 < 30（"愿意付"是 Inference，无价格/成交） |
| Red Flags | R1-R7 未命中 | — |

```yaml
hard_gates:
  checks:
    - {name: G1_Demand, status: PASS, reason: "Demand 88 ≥ 45"}
    - {name: G3_Monetization, status: PASS, reason: "Monetization 68 ≥ 45（维度分过线≠付费证据充分）"}
    - {name: C1_Payment, status: CEILING, reason: "payment coverage 25 < 30；付费意愿为 Inference，无价格锚"}
  triggered: [C1]
  score_ceiling: POTENTIAL
```

## 5. Decision

> **🟡 POTENTIAL 有机会但需先验证（Score Ceiling）**｜机会评分 **81/100**｜Confidence **Medium**｜Coverage **67%**｜Opportunity **MS-202**

Why：
1. 需求/竞争/开发三方面证据较充分（Evidence）。
2. Monetization 维度分 68 过门槛，但那是"愿意付"的推断——**没有价格、没有成交、没有替代付费证据**。
3. 命中 C1：无论总分 81，Decision 最高只能 POTENTIAL（先验证付费，再谈全力做）。

**教学点**：这就是"Score Ceiling 可解释"——不是规则不讲理，而是差的那一块证据恰好是项目生死的变量。

## 6. 下一步（前两步 = 补付费证据，不开发产品）

1. 访谈 8-10 家寄养商家：一个月花多少时间接单、现在为工具付过什么钱、最多愿意付多少 → 成功标准：≥3 家给出明确金额区间。
2. 用"纸质登记表数字化代做 + 99 元/月预售"验证付费 → 成功标准：≥1 家真实付款。
3. 达标后再进入 MVP；不达标 → 修改定价/人群，不进入开发。


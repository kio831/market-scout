# 示例：Re-evaluation 重新评估（v4.0.0）

> ⚠️ 演示数据。展示按 v4-validation.md §9 规则（R1-R5）重算 Score / Confidence / Coverage / Decision，全部可复算。
> 输入为本系列示例：MS-301 验证结果（20/8/3/2，¥398，7 天）。

## Before（验证前，来自 V3.1）

| 项 | 值 |
|---|---|
| Score | 73/100（Monetization 55，因 M1-M4 Unknown） |
| Confidence | Low（公式见下） |
| Coverage | 68%（payment 20） |
| Decision | POTENTIAL（C1 Payment CEILING） |
| State | MARKET_CONFIRMED |

## Validation Observed（仅事实）

```text
20 样本 / 8 兴趣 / 3 试用 / 2 付款（¥398），7 天，现金成本 0
```

## R1-R5 重算（规则固定，可复算）

```text
R1 分级：paid=2 → 付费维度 Evidence；其余仍 Inference/Unknown。
R2 覆盖度更新（只动 payment）：
   paid(2)/sample(20) = 10% ≥ 预设成功线 → Payment 覆盖：20 → 75
   新 Coverage = (85+75+75+75+65+85)/6 = 77
R3 分数更新（维度级校准兜底）：
   paid_rate = 10% → Monetization 维度分：55 → 80
R4 Confidence 重算：
   U = 0（M1-M4 已获证据）；CC = min(Payment 75, Problem 85) = 75；coverage 77
   = 0.30×77 + 0.20×1.00×100 + 0.35×75 + 0.15×100
   = 23.1 + 20 + 26.25 + 15 = 84.35 → 84 → High
R5 Decision 重判：
   Score = 80×.15+77×.15+70×.15+80×.20+88×.15+70×.10+78×.10 = 78/100
   Demand 80≥70 ✓，Pain 77≥60 ✓，Monetization 80≥60 ✓，无红旗、无 Ceiling
   → RECOMMENDED
```

## After（验证后）

| 项 | Before | After |
|---|---|---|
| Score | 73 | **78/100** |
| Confidence | Low（59） | **High（84）** |
| Coverage | 68% | **77%**（payment 20 → 75） |
| Decision | POTENTIAL | **RECOMMENDED** |
| State | MARKET_CONFIRMED | **VALIDATED → CUSTOMER_FOUND** |

```text
Reality note：以上重算"基于真实验证证据"；规模化获客、续费仍为 Unknown，不因本次成功而宣称已验证。
```

## Next Action（Continue）

1. 收款并交付 2 家首月内容（先收钱再交付）→ 标准：2 家 7 天内交付完成
2. 交付后要反馈与转介绍 → 标准：≥1 家愿转介绍
3. 用相同流程扩展第二个品类 10 家 → 标准：判断可复制性（对应 Unknown）

**教学点**：重算只动了被验证的维度；其余维度、公式、门槛全部复用 V3.1 —— **Reality > Prediction，但零伪造**。


# 示例：高分 + 低置信 → 为什么仍然 POTENTIAL（v3.1.0）

> ⚠️ 演示数据：仅展示方法。真实运行必须 Search First 并标注 Evidence/Inference/Unknown。
> 本示例对应 SOP Case C 与 §29 矩阵"High Score / Low Confidence"：

```text
Opportunity Score: 86/100
Decision Confidence: Low
Evidence Coverage: 50%
Decision: POTENTIAL
```

> 这表示：如果当前假设成立，这个机会很好；但目前证据不足以高度确认——结论只能是"先验证"。

## 用户输入

"我想做一个 AI 帮留子（留学生）写英文课程作业润色/论文语法纠正的小工具，值不值得做？"

## 1. Evidence -> Rubric -> Score（节选，含档位）

| 子信号 | 分 | 档位 | 证据状态 | 为什么 |
|---|---|---|---|---|
| D1 需求真实性 | 9 | 9-10 | Evidence | 多个留学论坛/小红书持续出现"论文润色贵"求助（示意） |
| D2 发生频率 | 9 | 9-10 | Evidence | 每学期固定多次（示意） |
| M2 客单价/预算 | 0 | Unknown 按 0 计 | Unknown | 未抓到真实预算证据 |
| M4 复购/订阅 | 0 | Unknown 按 0 计 | Unknown | 未验证是否连续订阅 |
| P3 现有方案不满 | 8 | 7-8 | Inference | 学校写作中心免费但难约（推断） |

维度分：Demand 90 / Pain 85 / Competition 75 / Monetization 88 / Buildability 92 / Distribution 80 / AI 90

```text
Score = 90×.15+85×.15+75×.15+88×.20+92×.15+80×.10+90×.10
     = 13.5+12.75+11.25+17.6+13.8+8+9 = 85.9 → 86/100
```

## 2. Evidence Coverage

| 维度 | 覆盖分 | status |
|---|---|---|
| Problem | 55 | partial |
| Solution | 55 | partial |
| Payment | 22 | insufficient |
| Competition | 55 | partial |
| Distribution | 55 | partial |
| Buildability | 55 | partial |

overall = round((55×5+22)/6) = **50/100**；critical_gaps：**payment evidence**

## 3. Confidence（公式可复算）

```text
U = 8/26 ≈ 0.31（Unknown 子信号：M2/M3/M4/P3/C4/D4/B2/A3）
CC = min(Payment 22, Problem 55) = 22
Confidence Score = 0.30×50 + 0.20×(1−0.31)×100 + 0.35×22 + 0.15×100
                 = 15 + 13.8 + 7.7 + 15 = 51.5 → 52
Level: Medium(52)；覆盖规则 O1（Payment<30）→ ≤Medium，O2（Payment<25）→ Low
```

**Confidence = Low**（限制因素：payment 与多条付费/渠道子信号为 Unknown）。

## 4. Hard Gates

| Gate | 结果 | 原因 |
|---|---|---|
| G1-G5 | 全部 PASS | Demand 90 / Pain 85 / Monetization 88 / Distribution 80 / Buildability 92 均过线 |
| C1 Payment | **CEILING** | Payment 覆盖 22 < 30 且 M2/M3/M4 为 Unknown |
| C2-C4 | 未命中 | — |
| Red Flags | R1-R7 未命中 | — |

score_ceiling = **POTENTIAL**

## 5. Decision

> **🟡 POTENTIAL 有机会但需先验证**｜机会评分 **86/100**｜Confidence **Low**｜Coverage **50%**｜Opportunity **MS-201**

Why：
1. 需求与痛点证据较强（Evidence，多个独立来源，示意）。
2. 机会本身按当前假设测算达 86 分（Score=机会有多好）。
3. 但付费假设未验证（Payment 覆盖 22，M2/M3/M4 Unknown）——命中 C1，最高只能 POTENTIAL。
4. 若假设成立则很好，但今天不能据此推荐全力投入（Confidence Low ≠ Score Low）。

**教学点**：高分不能直接推荐；Score / Confidence / Coverage 三者分开展示，缺一不可。

## 6. 下一步（验证优先）

1. 用"免费润色样品 + 49 元单次报价"接触 10 个目标留学生 → 成功标准：≥3 个有效回复且 ≥1 个真实付款。
2. 若无人付款 → 修改 Offer（改按学期打包），不开发产品。


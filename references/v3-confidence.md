# V3.1 Confidence Layer — 决策置信度（v3.1.0 新增）

> 把 **Opportunity Score（机会本身有多好）** 与 **Decision Confidence（我们有多确定）** 彻底分离。
> **Score = 84/100 且 Confidence = Low 是完全合法的状态**：如果假设成立机会很好，但当前证据不足以确认。
> Confidence 由固定规则计算，可手工复算，不允许 LLM 随意修改。

## 1. 输入（全部来自上游结构化字段，不新增主观输入）

| 输入 | 来源 | 含义 |
|---|---|---|
| coverage (0-100) | v3-evidence-coverage overall | 六维平均覆盖度 |
| U (0-1) | v3-scoring 子信号统计 | Unknown 子信号数 ÷ 参与评分子信号数（排除未启动的） |
| CC (0-100) | v3-evidence-coverage | Critical_Coverage = min(Payment, Problem) 覆盖分（Problem 覆盖代表需求侧证据） |
| independent_ok (0/1) | v3-evidence 看板 | 去重后：Problem ≥2 个独立来源 且 Payment ≥1 个独立来源 → 1，否则 0 |

## 2. 公式（固定，可复算）

```text
Confidence Score = round(
    0.30 × coverage
  + 0.20 × (1 − U) × 100
  + 0.35 × CC
  + 0.15 × independent_ok × 100
)
Level: High ≥ 70  |  Medium 40-69  |  Low < 40
```

## 3. 覆盖规则（公式之外，固定不变，优先级最高）

| 规则 | 条件 | 结果 |
|---|---|---|
| O1 | Payment 覆盖 < 30 或 Problem 覆盖 < 40 | Level ≤ Medium |
| O2 | Payment 覆盖 < 25 或 Problem 覆盖 < 30 | Level = Low |
| O3 | 证据充分度 = Insufficient（v3-evidence §3） | Level = Low |

规则保证（对应 SOP Case D）：Coverage 80 但 Payment 覆盖 20 → CC=20 → 公式 ≈ 24 + 19 + 7 + 15 = 65；
命中 O1（<30）与 O2（<25）→ 强制 **Low**。Coverage 高 ≠ Confidence 高。

## 4. 输出

```yaml
confidence:
  level: Medium            # High | Medium | Low
  score: 61                # 0-100，可复算
  rationale: "coverage 66；U=0.23；CC=min(90,30)=30；独立来源达标"
  limiting_factors: []
```

## 5. 与 Decision 的配合

- Confidence 不直接决定 Decision，但通过两个通道影响：
  1. **Hard Gates**：Payment/Demand 覆盖不足会触发 Score Ceiling（v3-hard-gates C1/C2）→ 最高 POTENTIAL。
  2. **Why 列表**：低置信必须在 Decision Why 中列为首要原因之一。
- 合法组合示例：

```text
Score = 85 | Confidence = Low | Decision = POTENTIAL   ✓（Case C）
Score = 74 | Confidence = High | Decision = POTENTIAL  ✓（分数区间）
Score = 48 | Confidence = High | Decision = NOT_RECOMMENDED ✓（分数区间 < 55）
```

## 6. Unknown 与 Low 的分离（P0）

- **Unknown** 描述证据状态（信息不足）；**Low Confidence** 描述结论可靠性（由 Unknown 等折算）。
- 禁止把"大量 Unknown"直接表述为"此机会很差"——正确表述：
  "Score 受证据缺失影响（Unknown 按 0 计），Confidence Low，Coverage Low；先补关键证据再重评分。"
- 禁止为隐藏 Unknown 而把它升级为 Inference；禁止为提 Confidence 而重复计来源。

## 7. 修订规则

- 公式、权重、阈值只随版本变更（CHANGELOG），不得在单个机会分析中修改。
- 每次输出附 `rationale`（各输入值），保证可复算、可复核。


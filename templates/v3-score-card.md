# Opportunity Score Card 机会评分卡（v3.1.0）

> 方法见 `references/v3-scoring.md` + `references/v3-scoring-rubric.md`。每分子信号六要素（分/档位/理由/证据/状态/置信度）；计算式必须可复算。

**Opportunity ID**：<MS-###>

## 一、七维评分（0-100）

| 维度 | 权重 | 维度分 | 子信号（1-10：分 / 理由 / 证据徽标 / 不确定性） |
|---|---|---|---|
| Demand 需求强度 | 15% | <0-100> | D1 <分>（档 <1-2/3-4/5-6/7-8/9-10>）：<理由>（<Evidence/Inference/Unknown>，conf <高/中/低>，<不确定性>）｜D2…｜D3…｜D4… |
| Pain 痛点强度 | 15% | | P1…｜P2…｜P3… |
| Competition 竞争与切入空间 | 15% | | C1…｜C2…｜C3…｜C4… |
| Monetization 变现潜力 | 20% | | M1…｜M2…｜M3…｜M4… |
| Buildability 开发可行性 | 15% | | B1…｜B2…｜B3…｜B4… |
| Distribution 获客难度 | 10% | | D1…｜D2…｜D3…｜D4… |
| AI Advantage AI 优势 | 10% | | A1…｜A2…｜A3…｜A4… |

> 规则：Unknown 子信号按 0 计并显式标注；Inference 最高 7/10；维度内 Unknown 过半标"低可信"。
> 权重调整：<未调整 / 调整了什么+为什么>

## 二、计算式（可复算）

```text
= <维度分>×<权重> + ... = <合计> → <NN>/100
```

## 三、百分条（20 格，每格 5 分）

```
需求强度      ████████████████░░░░ 80/100
痛点强度      ██████████████████░░ 90/100
竞争与切入    ████████████░░░░░░░░ 60/100
变现潜力      ████████████████░░░░ 82/100
开发可行性    ███████████████████░ 94/100
获客难度      ████████████░░░░░░░░ 61/100
AI 优势       ██████████████████░░ 89/100
─────────────────────────────
Opportunity Score    <NN>/100
```

## 四、最强两项 / 最弱两项

- 最强：<维度> <分> —— <为什么成立>
- 最弱：<维度> <分> —— <可能死在哪里>

## 五、竞争与切入空间（四问，Competition 维度必答）

1. 用户有没有真实需求？<VALIDATE 结论>
2. 竞品有没有把问题解决到位？<Solution 证据>
3. 用户是否仍在抱怨？<未满足证据>
4. 有没有可守的差异化切入点？<切入点 + 复制难度>

## 六、致命红旗检查（v3-scoring §4）

- R1-R7：<逐条 命中/未命中；命中即 NOT_RECOMMENDED>

## 七、低可信标注

- <哪些维度低可信、为什么、如何补证据重算>

## 八、Evidence Coverage（v3.1）

| 维度 | 覆盖分 | status | 独立来源（去重后） | 缺口 |
|---|---|---|---|---|
| Problem / Solution / Payment / Competition / Distribution / Buildability | <0-100> | covered / partial / insufficient | <N> | <缺什么子问题> |

- overall：<round(六维均值)>（计算式：<...>）
- critical_gaps：<如 payment evidence>

## 九、Confidence（v3.1）

```yaml
confidence:
  level: Medium
  score: 61
  rationale: "coverage 66；U=0.23；CC=min(90,30)=30；independent_ok=1"
  limiting_factors: []
```

（公式与覆盖规则见 `references/v3-confidence.md`；分数必须可复算）

## 十、Hard Gates（v3.1）

| Gate | 维度/条件 | 结果 |
|---|---|---|
| G1-G5 | <维度分> | PASS / FAIL（任一 FAIL → NOT_RECOMMENDED） |
| C1-C4 | <证据条件> | 未命中 / 命中（命中 → score_ceiling: POTENTIAL） |
| Red Flags | R1-R7 | 未命中 / 命中 R<#> |

```text
Reason: <一句话为什么>
```

**👉 下一步**：把本卡交给 DECISION 阶段生成 `templates/v3-decision-card.md`，得出三档决策与 Why。

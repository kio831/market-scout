# V3.1 Hard Gates — 硬门槛与分数天花板（v3.1.0 新增）

> 防止"总分掩盖致命短板"（SOP §9-12）：允许 `Demand=30, Monetization=25, 总分 75` 却被判
> RECOMMENDED 的情况发生。三层机制：**Hard Gate**（核心维度低于最低标准 → NOT_RECOMMENDED）、
> **Score Ceiling**（关键证据条件不满足 → 最高 POTENTIAL）、**Red Flag**（既有致命红旗 → NOT_RECOMMENDED）。

## 1. 三层区别（不混淆）

| 层级 | 含义 | 处置 | 来源 |
|---|---|---|---|
| Hard Gate | 核心维度分低于最低标准 | **NOT_RECOMMENDED**（无条件） | 本文件 §2，由 V3 Decision 门槛推导 |
| Score Ceiling | 核心证据条件不满足 | **最高 POTENTIAL**（无论总分） | 本文件 §3 |
| Red Flag R1-R7 | 明确致命风险 | **NOT_RECOMMENDED**（无论总分） | `v3-scoring.md` §4（复用，不重写） |

## 2. Hard Gates（核心维度最低标准，→ NOT_RECOMMENDED）

> 阈值推导依据（不凭空设计）：V3 Decision 规则（`v3-decision.md` §2）中
> RECOMMENDED 要求 Demand ≥ 70、Pain ≥ 60、Monetization ≥ 60；NOT_RECOMMENDED 门槛是
> 总分 < 55 或基础证据缺失。本层把"单维致命短板"单独拦下，防止被其他维度补足。

| Gate | 维度 | 最低标准 | 判据说明 |
|---|---|---|---|
| G1 | Demand 需求强度 | < 45 → FAIL | 需求真实性存疑（≈子信号均分 < 4.5），对应"连问题是否真实存在都没有证据"的 NOT_RECOMMENDED 判据 |
| G2 | Pain 痛点强度 | < 40 → FAIL | 低分画像"只是有点不方便"，不值得投入 |
| G3 | Monetization 变现潜力 | < 45 → FAIL | 付费证据与付费可能都很弱；R2 红旗的分数层前置 |
| G4 | Distribution 获客难度 | < 35 → FAIL | 触达不到客户 = 致命；R4 红旗的分数层前置 |
| G5 | Buildability 开发可行性 | < 30 → FAIL | 个人做不出最小可售物 |

任意 Gate FAIL → **Decision = NOT_RECOMMENDED**，跳过 MVP 与常规 Action（输出停止三要素）。

## 3. Score Ceilings（关键证据条件不满足，→ 最高 POTENTIAL）

| Ceiling | 触发条件 | 效果 |
|---|---|---|
| C1 Payment | Payment 维度含任一 Unknown 子信号，或 Payment 覆盖 < 30 | 最高 POTENTIAL（付费未验证） |
| C2 Demand | Demand 维度 Unknown 子信号 ≥ 2，或 Problem 覆盖 < 40（需求侧证据） | 最高 POTENTIAL（需求未验证） |
| C3 Distribution | 获客渠道为 Unknown 且无替代假设 | 最高 POTENTIAL（触达路径未知） |
| C4 Competition | Competition ≤ 40，或切入空间四问全部仅 Inference | 最高 POTENTIAL（切入空间未证实） |

- C1/C2 与 `v3-decision.md` §2 POTENTIAL 判据"关键假设未验证"一致，本层只做显式化。
- 多个 Ceiling 同时触发 → 全部列出；score_ceiling 统一为 `POTENTIAL`。

## 4. 检查顺序（固定）

```text
1. Red Flags（v3-scoring §4）→ 命中任一 → NOT_RECOMMENDED
2. Hard Gates G1-G5 → 任一 FAIL → NOT_RECOMMENDED
3. Score Ceilings C1-C4 → 命中 → Decision ≤ POTENTIAL
4. 否则按 v3-decision §2 正常判定
```

## 5. 输出格式（必须可解释）

```text
Hard Gates

Demand       PASS
Pain         PASS
Monetization CEILING
Distribution PASS
Buildability PASS
Red Flags    R1-R7 均未命中

Reason:
Monetization 当前缺乏直接付费证据（Payment 覆盖 25 < 30，命中 C1），
因此即使总分达到阈值，Decision 最高只能为 POTENTIAL。
```

```yaml
hard_gates:
  checks:
    - {name: G1_Demand, status: PASS, reason: "Demand 82 ≥ 45"}
    - {name: G3_Monetization, status: CEILING, reason: "Payment coverage 25 < 30 (C1)"}
  triggered: [C1]
  score_ceiling: POTENTIAL
```

## 6. 与 Confidence / Coverage 的关系

- Hard Gate 用**维度分**（SCORING 输出）与**覆盖度**（COVERAGE 输出）两类输入，不新增概念。
- Coverage 不足触发 Ceiling；Confidence 低只影响解释（Why 首位），不直接翻 Decision；
  但当 Confidence=Low 且 Score ≥ 75 时，必须检查是否命中 C1-C4（通常都会命中）。

## 7. 防调规则

- 阈值与触发条件随版本变更（CHANGELOG）；单个机会分析中禁止调整。
- 禁止为了 SKIP ceiling 而把 Unknown 改写为 Inference（SOP §30）。


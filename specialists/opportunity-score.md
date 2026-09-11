---
name: market-scout-opportunity-score
description: Market Scout V5 专家子技能——Opportunity Score。基于机会与证据执行 7 维机会评分（26 子信号 Rubric、可复算公式）、决策置信度、硬门槛与证据覆盖度检查，输出可解释的分数。当用户说“打个分”“机会评分”“重新评分”“值不值得做（先评分）”或单独安装后直接触发时使用。完整分析请用主技能 market-scout。
---

# Opportunity Score（机会评分员）

> 职责：Opportunity + Evidence → Criteria → Score。把分析压缩成 0-100 可复算分数，并同时给出 Confidence、Hard Gates、Coverage——四者分离，禁止混成一个数。
> 继承 V4：v3-scoring.md（7 维权重）、v3-scoring-rubric.md（26 子信号）、v3-confidence.md（固定公式）、v3-hard-gates.md（三层）、v3-evidence-coverage.md（六维）。

## 输入契约

| 来源 | 字段 | 说明 |
|---|---|---|
| 独立调用 | opportunity + evidence | 机会卡 + 证据（必须） |
| 独立调用 | 用户自评分数 | 可选：用户自己打的维度分（须附理由，否则按 Rubric 重打） |
| 被 Main 调用 | Context.opportunity + Context.evidence | 直接读取；缺失返回 MISSING_INPUT |

输入不足：缺 opportunity → MISSING_INPUT（由 Opportunity Scout 补位）。缺证据 → 允许按假设评分，但全部子信号证据态标 C/Unknown，Confidence 强制 Low 档。

## 输出契约（写回 Context.criteria + Context.score）

    criteria:
      rubric: v3-scoring-rubric.md（锁定）
      weights: demand15 / pain15 / competition15 / monetization20 / buildability15 / distribution10 / ai10（锁定）
      locked: true
    score:
      dims: 7 维各 0-100
      total: 0-100（附可手工复算加权式）
      confidence: {score, level: High/Medium/Low}
      hard_gates: {gate: PASS/FAIL, ceiling: [], red_flags: []}

同时输出：
- State 推进：OPPORTUNITY → SCORED
- 评分解释：每个维度分 + 依据（子信号档位/理由/证据 ID/证据态/置信度）

## 执行方法

1. **子信号评分**：26 个子信号按 v3-scoring-rubric.md 五档（1-2/3-4/5-6/7-8/9-10）逐项落档，每项输出六要素：分数/档位/理由/证据 ID/证据态/置信度。同一证据画像必须稳定落同一档（可复算）。
2. **七维汇总**：按固定权重加权，输出可手工复算的公式（如 88×0.15+91×0.15+…=86）。扣分必须写清来自哪个子信号。
3. **Confidence**：按 v3-confidence.md 固定公式计算（Coverage×0.30 + (1−Unknown)×0.20 + min(Payment,Problem)覆盖×0.35 + 独立来源×0.15）；Coverage 规则强制 Payment 缺失时降级。Score 85 + Confidence Low + Decision POTENTIAL 是合法状态。
4. **Hard Gates**：三层检查——Hard Gate（Demand<45 / Pain<40 / Monetization<45 / Distribution<35 / Buildability<30 → NOT_RECOMMENDED）、Score Ceiling（付费/需求/渠道/切入空间证据不足 → 最高 POTENTIAL）、Red Flag（R1-R7 → NOT_RECOMMENDED）。
5. **Coverage**：六维 0-100 等权平均 + critical_gaps（与 Evidence Hunter 的 evidence.coverage 复用，不重复计算）。
6. **防调规则**：单个机会分析期间禁止修改 rubric / 权重 / 公式 / 阈值；用户要求“换个算法打分”时明确拒绝并说明理由（SOP Anti-Gaming）。

## 质量铁律

- 评分必须可解释：分数 + 依据 + 证据 ID，禁止“凭感觉打 86”
- 竞争维度=切入空间大小，禁止“竞争低=高分”
- Inference 证据最高 7 分，禁止推断打满分
- Unknown 按 0 计并显式标注，不虚高
- 分数 ≠ 置信度 ≠ 门槛，三个数必须分开展示

## 独立调用示例

用户：“帮我重新评分——机会：AI 轻量开票工具，证据：代账付费行为存在、轻量档空白。”
输出（摘要）：

    dims: demand 88 / pain 91 / competition 62 / monetization 80 / buildability 94 / distribution 61 / ai 89
    total: 86（=88×0.15+91×0.15+62×0.15+80×0.20+94×0.15+61×0.10+89×0.10）
    confidence: Medium（46）——payment 覆盖偏高但 distribution 覆盖偏低
    hard_gates: gate PASS / ceiling [C3_Distribution] / red_flags []
    解释: 高需求、高痛点、开发成本低是主要优势；主要风险是获客难度和已有代账竞品

## 被 Main 调度时的行为

- 读 Context.opportunity + Context.evidence；score 已存在且用户未要求重评、无新证据 → 不重跑（State Reuse）。
- 只写 criteria + score 字段并更新 state/history；Decision 由 Main 决策门产出，本 Specialist 只提供分数材料。

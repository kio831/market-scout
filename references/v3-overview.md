# V3 决策层总览 — 从"分析"到"决定"（v3.0.0 新增）

> 本文件定义 V3 新增的**决策层**如何叠加在 V2 五阶段流水线之上。
> V2 负责把机会分析清楚（Find → Validate → Evaluate → Blueprint → Monetize）；
> V3 负责把分析压缩成一个用户 10 秒能看懂、且能照着行动的结论：
> **Evidence 证据 → Score 评分 → Decision 决策 → MVP 方案 → Action 行动**。
> V3 不重写 V2：V2 的五阶段方法、三种模式、铁律、停止机制、第一笔钱清单全部保留，V3 只在其上新增一层编排与统一口径。

## 0. V3 要解决的问题

用户拿到 V2 的五张卡之后，仍会卡在三个问题上：

1. **到底值不值得做？**（V2 已有 GO/VALIDATE_FIRST/NO_GO，但用户还想要更直觉的 0-100 综合分 + 明确三档结论。）
2. **为什么是这个结论？**（每个分数必须可解释、可复算，每个结论必须标注依据。）
3. **现在第一步做什么？**（需要一个按机会类型动态生成的行动计划。）

V3 的对应回答：

- 值不值得做 → **Opportunity Score（0-100）+ Decision（Recommended / Potential / Not Recommended）**
- 为什么 → **证据三态（Evidence / Inference / Unknown）+ 每分绑定证据 + 可复算计算式**
- 现在做什么 → **MVP Blueprint（9 字段）+ 动态 Action Plan**

## 1. V3 主流程（9 步）

```
INPUT        用户输入一个想法 / 问题 / 机会
  ↓
DISCOVERY    发现用户与痛点            （复用 V2 FIND）
  ↓
VALIDATION   验证需求与市场            （复用 V2 VALIDATE）
  ↓
EVIDENCE     证据归一化                （v3-evidence.md：Evidence/Inference/Unknown + 充分度）
  ↓
COMPETITION  竞品与市场空缺            （复用 V2 竞争分析 + v3-scoring.md §3 切入空间判定）
  ↓
SCORING      计算 Opportunity Score    （v3-scoring.md：7 维 0-100 可复算）
  ↓
DECISION     判断值不值得做            （v3-decision.md：Recommended/Potential/Not Recommended）
  ↓
MVP          若值得：生成 MVP Blueprint（v3-mvp.md：9 字段，复用 V2 BLUEPRINT）
  ↓
ACTION       生成下一步行动计划        （v3-action-plan.md：按机会类型动态生成）
```

## 2. V2 → V3 映射（复用优先，禁止重写）

| V3 步骤 | 复用 V2 的能力 | V3 新增 |
|---|---|---|
| INPUT | Quick Mode 默认入口、Opportunity ID（`opportunity-state-machine.md`） | V3Input 输入契约（§3） |
| DISCOVERY | FIND：三类搜索、Problem Card、Evidence Card、证据链、证据等级 A/B/C | —（完全复用） |
| VALIDATION | VALIDATE：需求强度 6 信号、三层用户、替代成本、付费理由链 JTBD | —（完全复用） |
| EVIDENCE | 证据链五段式、证据 7 属性、证据等级 A/B/C | 证据三态标签 Evidence/Inference/Unknown、证据充分度三级、Unknown 计分规则 |
| COMPETITION | `market-research.md` §4 竞争与付费、`project-evaluation.md` §3 竞争格局与差异化 | 切入空间四问强制判定、"竞争低≠高分"禁令 |
| SCORING | 评分绑定证据四要素、分数条、可复算原则 | 统一 7 维 0-100 Opportunity Score（v3-scoring） |
| DECISION | `project-evaluation.md` §2 三档判定、停止机制三要素 | 统一三档 Decision + 强制 Why 列表 + 与 V2 Verdict 的映射 |
| MVP | BLUEPRINT：产品形态 Level 1-5、MoSCoW、MVP 五项、技术方向、最小验证 | 9 字段统一输出（v3-mvp）+ 单人最快验证铁律 |
| ACTION | MONETIZE：首批 10 客户、GTM 三阶段、无产品验证、第一笔钱清单 | 按机会类型动态生成的步骤模板（v3-action-plan） |

V2 的五阶段方法文档（demand-validation / project-evaluation / project-blueprint / monetization-gtm / pipeline-and-runtime）**全部保留、全部可用**；V3 不修改其中任何一篇。

## 3. 输入契约（V3Input）

```yaml
V3Input:
  idea: string                    # 用户的想法/问题/现象（必填，尽量保留原话）
  context: string                 # 用户补充的背景（目标人群/地域/资源，可空）
  constraints:                    # 用户自身约束（可空，缺则按保守默认）
    weekly_time: string           # 每周可投入时间
    cash_budget: string           # 可承受现金投入
    channels_access: [string]     # 用户本人能触达的渠道
  existing:                       # 可空：续研已有机会时使用
    opportunity_id: MS-###        # 沿用状态机 ID，不新建
    cards: {problem, demand_validation, project_evaluation, project_blueprint, monetization_gtm}
```

缺字段显式标注【缺失】，并按保守默认处理，不靠上下文猜测（沿用 `pipeline-and-runtime.md` §2）。

## 4. 输出契约（V3Output）

```yaml
V3Output:
  opportunity_id: MS-###
  evidence_board:                 # v3-evidence.md
    items: [{claim, status: Evidence|Inference|Unknown, source, confidence}]
    sufficiency: Sufficient|Partial|Insufficient
    missing: [string]             # 缺什么证据、去哪补
  opportunity_score:              # v3-scoring.md
    dimensions: {demand, pain, competition, monetization, buildability, distribution, ai_advantage}
    per_dimension: {score, weight, subscores, rationale, evidence_tag}
    formula: string               # 可复算计算式
    total: 0-100
    red_flags: [string]           # 逐条 命中/未命中
  decision:                       # v3-decision.md
    code: RECOMMENDED|POTENTIAL|NOT_RECOMMENDED
    why: [string]                 # 编号理由，每条绑定证据三态
    next_commitment: string
  mvp_blueprint:                  # 可空：RECOMMENDED 或（POTENTIAL 且 score≥65）必填
    product, target_user, core_problem, core_value,
    must_have: [string], nice_to_have: [string], do_not_build: [string],
    build_difficulty: string, recommended_stack: string,
    validation_experiment: {hypothesis, method, success_rule, fail_rule}
  action_plan:                    # v3-action-plan.md
    opportunity_type: B2B_TOOL|CONSUMER_TOOL|AI_AGENT|LOCAL_SERVICE|DIGITAL_PRODUCT
    steps: [{n, goal, do, success, fallback}]
    today: [string]               # 今天就能做的 1-3 个动作
  confidence: string              # 本次结论整体置信度（高/中/低）
  open_questions: [string]
```

## 5. 四套"代码"正交（防混淆扩展）

| 代码 | 含义 | 例子 |
|---|---|---|
| 证据等级 A/B/C | 需求验证程度（v1.1 保留） | B |
| Opportunity State | 真实交付状态（v1.1 保留） | DEMAND_CONFIRMED |
| Pipeline Stage | V2 分析流水线位置 | EVALUATE |
| **Decision Code（v3 新增）** | **最终机会决策** | **RECOMMENDED / POTENTIAL / NOT_RECOMMENDED** |

四者互不替代。同一张报告可以同时是 `Pipeline=SCORING / State=DEMAND_CONFIRMED / 证据等级=B / Decision=POTENTIAL`，完全合法。禁止用一套字母表达多个含义（沿用 `pipeline-and-runtime.md` §1.1）。

## 6. 与三种工作模式的关系

| 场景 | V3 行为 | 出口 |
|---|---|---|
| Quick Mode（随手抛一个想法） | 轻量 DISCOVERY → SCORING（标证据不足项）→ DECISION → 1-2 条今天行动 | `templates/v3-report.md`（精简版） |
| Research Mode（要求深挖/全面验证） | 完整 V2 五阶段 + V3 完整决策链 | `templates/v3-report.md`（完整版） |
| Execution Mode（"我准备做/帮我拿第一单"） | 跳过 SCORING；已有结论的用 v3-mvp + v3-action-plan 执行步骤 + 第一笔钱清单 | `templates/v3-action-plan-card.md` |
| 显式 V3 决策请求（"打个分/值不值得做/帮我决策"） | 直接进入 V3 决策层，从第一个缺卡的步骤开始 | `templates/v3-report.md` |

V3 触发词见 `SKILL.md` §模式路由。

## 7. 熔断与降级

- **证据不足熔断**：连"问题是否真实存在"都没有证据时，不评分、不编造；输出 Evidence Insufficient 横幅 + 缺什么 + 去哪补，Decision 按 `v3-decision.md` §4 处理。
- **红旗熔断**：触发任一致命红旗（`v3-scoring.md` §4）→ Decision=NOT_RECOMMENDED，跳过 MVP，Action Plan 输出停止三要素。
- **Unknown 降级**：Unknown 子信号按 0 计并在报告中显式标注（`v3-scoring.md` §2.4）；维度内 Unknown 过半时该维度标"低可信"。
- **断点续跑**：从第一张缺失的 V3 卡片恢复；已有 Opportunity ID 的续研先读旧卡，不重复搜索（`opportunity-state-machine.md` §5）。
- **外部调用健壮性**：超时、有限重试、失败降级一律遵守 `pipeline-and-runtime.md` §3。

## 8. 输出渲染（沿用 ui-rendering-spec.md，V3 新增约定）

- 顶部结论带（每份 V3 输出必有）：
  `> **🟢 RECOMMENDED 值得继续做** | 机会评分 **86/100** | 需求 **88** | Opportunity **MS-###**` + 一句话结论。
- 百分条统一 20 格（每格 5 分）：`需求强度 ████████████████░░░░ 82/100`。
- 证据三态徽标：`[Evidence]` `[Inference]` `[Unknown]`，每条关键结论、每个分数都带。
- 结论先行、阶段进度条、四种运行状态、移动端窄屏键值列表、双语标签、代码块语言标注等规则不变（`ui-rendering-spec.md` §4-§12）。

## 9. 交付前验收清单（V3 一次完整运行的最终自检）

- [ ] Score 有可复算计算式；7 维每维有子信号分 + 理由 + 证据徽标？
- [ ] Decision 有编号 Why 列表（每条绑定证据/标注 Unknown）？
- [ ] 证据三态出现在每个关键结论旁；无来源的结论标 Unknown，无编造？
- [ ] 竞争维度的"切入空间"回答四问；没有"竞争低=高分"的错误逻辑？
- [ ] RECOMMENDED /（POTENTIAL 且 score≥65）有 9 字段 MVP Blueprint？
- [ ] Action Plan 按机会类型生成，每步 5 要素，结尾有"今天做什么"？
- [ ] 未破坏 V2：五张 V2 卡、12 篇方法论文档、10 张模板、4 个示例全部保留可用？

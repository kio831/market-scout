# State Machine 统一状态机（v5.0.0 新增）

> 统一 State 让 Main Skill 随时能回答：**用户目前在哪里、已经完成什么、缺少什么、下一步应该是什么**。
> 九态与 V4 的既有产物一一对应，**不新增 V4 概念**，只是把产物状态化。

## 1. 九个状态

    IDEA → OBSERVATION → PROBLEM → EVIDENCE → OPPORTUNITY → SCORED → VALIDATION → DECISION → ACTION

| State | 含义（何时算达成） | 生产方 | 对应 V4 产物 |
|---|---|---|---|
| IDEA | 用户给出原始想法/现象 | （入口） | 用户原话 |
| OBSERVATION | 已拆出谁/什么问题/频率/当前方案/付费信号/AI 杠杆 | Idea Observer | 观察信号 |
| PROBLEM | Problem Card 已填（目标用户/场景/证据等级） | Problem Scout | templates/problem-card.md |
| EVIDENCE | 三类搜索完成，证据链与 Coverage 已建立 | Evidence Hunter | Evidence Card、v3-evidence-board.md、coverage |
| OPPORTUNITY | 需求验证 + 竞争切入空间结论已出，Opportunity Card 已建 | Opportunity Scout | templates/opportunity-card.md、demand-validation-card.md |
| SCORED | 7 维评分 + Confidence + Hard Gates 已产出（可复算） | Opportunity Score | templates/v3-score-card.md |
| VALIDATION | 验证计划已设计，或实验结果已回填 | Validation Scout | templates/v4-validation-card.md |
| DECISION | 三档决策 + 动作裁决已给出（带 Why） | Main | templates/v3-decision-card.md |
| ACTION | 行动计划 + 今天做什么已给出 | Main | templates/v3-action-plan-card.md、v3-action-plan.md |

## 2. 转移规则

- 允许前进跳步（前进跳步合法）：IDEA → EVIDENCE（用户自带资料）；PROBLEM → SCORED（已有评分输入）；任意 N → N+k，k>0。跳步必须由输入事实支撑，并在 Context.history 中记录跳跃原因。
- 允许**受控回退**（仅两类）：
  1. VALIDATION 结果回填后 → DECISION / SCORED 按 v4-validation.md 的 R1-R5 规则重算（Reality > Prediction，合法回退）。
  2. 用户显式要求“重新评分 / 重新验证 / 全部重来”。
- 禁止无依据回退：没有新证据、没有用户要求时，不得把已完成的 State 打回重做。
- 每个 State 转移时更新：state、history（追加）、produced_by（哪个 Specialist）、updated_at。

## 3. 状态查询表（Main 每次路由前必查）

    〉当前 State      〉已完成              〉缺失              〉下一步
    IDEA              idea                 后续全部             Idea Observer
    OBSERVATION       idea→observation     后续全部             Problem Scout
    PROBLEM           ～problem            证据及以后           Evidence Hunter
    EVIDENCE          ～evidence           机会及以后           Opportunity Scout
    OPPORTUNITY       ～opportunity        评分及以后           Opportunity Score
    SCORED            ～score              验证/决策/行动       Main 决策门（→ Validation Scout 或 Action）
    VALIDATION        ～validation         决策/行动           Main 读结果重判（v4 规则 R1-R5）
    DECISION          ～decision           行动                Main Action
    ACTION            全部                 无                  （闭环完成，输出自检）

## 4. Opportunity State（真实世界状态）不混淆

- 本文件九个 State 是**分析流水线状态**；V4 的 Opportunity State（HYPOTHESIS → … → PRODUCTIZED）是**真实世界交付状态**。两者正交、并存：
  例：Pipeline State=SCORED 且 Opportunity State=DEMAND_CONFIRMED 完全合法。
- 证据等级 A/B/C、Pipeline State、Opportunity State、Decision Code（RECOMMENDED/POTENTIAL/NOT_RECOMMENDED）四套代码继续互不混淆，规则不变。

## 5. State Recovery（上下文缺失/跨会话续跑）

- 会话中断或用户换新对话：先从用户可提供的材料 + 历史卡片重建 Context 字段，能重建多少字段就标记多少 State；无法确认的字段一律标 Unknown，不猜测已完成。
- 重建完成后执行路由流水线（orchestrator/routing.md 第 1 节），从最高已确认 State 的下一缺失阶段续跑。
- 若用户只记得结论（如“上次说 86 分”）而材料丢失：按 DECISION/SCORED 存在处理，但要求用户补充关键证据文件后再继续，避免无源续跑。

## 6. 边界条件处理

| 情况 | 规则 |
|---|---|
| 阶段已完成又收到同样输入 | 不重跑；提示已有结果，询问是否需要基于新信息重算 |
| Validation 无法进行（无触达用户渠道） | 输出 PARK 与重启条件，State 停在 VALIDATION 的"planned but blocked" |
| 搜索无结果 | EVIDENCE 仍达成（Coverage 记 0 + 原因），决策自动受 Score Ceiling 约束 |
| 证据冲突 | State 不推进，先解决冲突（标记 TO VERIFY），解决后继续 |
| 用户要求跳过某阶段 | 允许跳步但记录原因；决策时必须说明该阶段缺失对 Confidence 的影响 |
| 重复调用同一 Specialist | 见 routing.md 第 2 节：先确认再重跑，显式“重新”意图除外 |

## 7. 状态自检（每次状态更新后）

- [ ] state 与最后一个完成的产物一致
- [ ] history 无断点（跳跃有原因记录）
- [ ] 四套代码（证据等级/状态机/Pipeline/Decision）未混用
- [ ] 未发生无依据回退
- [ ] Unknown 字段有明确清单，不冒充已完成

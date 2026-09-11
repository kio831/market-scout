# MarketScoutContext 统一上下文契约（v5.0.0 新增）

> 所有 Specialist 与 Main 通过同一份 Context 传递数据：**字段与 V4 既有卡片一一对应，不重复定义概念**。
> 持久化载体：templates/v5-context-card.md（用户可保存为工作文件）；会话内由模型在推理中维护同名结构。

## 1. 结构定义（YAML 契约）

    context_version: "5.0.0"
    opportunity_id: "MS-###"            # V4 Opportunity ID，无则在此创建
    mode: quick | research | execution  # V4 Mode（工作方式/能力深度），沿用 V4 三模式
    orchestration_mode: full | focused | mid-entry | independent   # V5 调度模式（怎么进入与调度）
    state: IDEA | OBSERVATION | PROBLEM | EVIDENCE | OPPORTUNITY | SCORED | VALIDATION | DECISION | ACTION
    history:                            # 已完成的 State 列表（有序）
      - {state: IDEA, produced_by: user, at: "…"}
      - {state: OBSERVATION, produced_by: Idea Observer, at: "…"}
    idea:                               # 用户原始想法/现象（原样保留）
      text: ""
      source: ""                        # 来自哪里（原话/视频/评论区/资料）
    observation:                        # Idea Observer 产出
      who: ""
      problem: ""
      frequency: ""                     # 重复性信号
      current_solution: ""              # 现在怎么解决
      payment_signal: ""                # 付费信号
      ai_leverage: ""                   # AI 杠杆信号
      hypothesis_flags: []              # 疑似空想/未观察项
    problem:                            # Problem Scout 产出（对齐 problem-card.md）
      card: ""                          # 引用 problem-card 填写结果
      target_user: ""
      scenario: ""
      evidence_level: A | B | C
      category: ""                      # 问题十大分类
    evidence:                           # Evidence Hunter 产出
      chain:                            # 每条证据走五段链
        - {evidence: "", source: "", type: "", confidence: "", proves: "", not_proves: "", level: ""}
      board: ""                         # 引用 v3-evidence-board.md 三态看板
      coverage: {problem: 0, solution: 0, payment: 0, competition: 0, distribution: 0, buildability: 0}
      overall_coverage: 0
      critical_gaps: []
      search_capability: true | false   # false 时全部结论标假设
    opportunity:                        # Opportunity Scout 产出（对齐 opportunity-card.md）
      card: ""
      state: HYPOTHESIS | DEMAND_CONFIRMED | MARKET_CONFIRMED | …
      bottleneck: ""
      demand_summary: ""
      competition_gap: ""               # 切入空间四问结论
    criteria:                           # 评分依据（防调规则锚点）
      rubric: "v3-scoring-rubric.md"
      weights: "demand15 pain15 competition15 monetization20 buildability15 distribution10 ai10"
      locked: true                      # 单个机会分析期间禁止修改
    score:                              # Opportunity Score 产出（对齐 v3-score-card.md）
      dims: {demand: 0, pain: 0, competition: 0, monetization: 0, buildability: 0, distribution: 0, ai: 0}
      total: 0
      formula: ""
      confidence: {score: 0, level: High | Medium | Low}
      hard_gates: {gate: PASS | FAIL, ceiling: [], red_flags: []}
    validation:                         # Validation Scout 产出（对齐 v4-validation-card.md）
      plan: {core_hypothesis: "", method: "", sample: 0, duration: "", cost: "", success: "", failure: "", decision_rule: ""}
      experiment: {done: false, detail: ""}
      result: {sample_n: 0, interested: 0, trial: 0, paid: 0, revenue: 0, observed: [], inference: [], unknown: []}
    decision:                           # Main 产出（对齐 v3-decision-card.md）
      code: RECOMMENDED | POTENTIAL | NOT_RECOMMENDED
      verdict: BUILD | VALIDATE | RESEARCH | PARK | KILL
      why: []
      restart_conditions: []            # PARK 时必填
    action:                             # Main 产出（对齐 v3-action-plan-card.md）
      plan: []
      today: ""
    assumptions: []                     # 全局假设清单（带 HYPOTHESIS 标签）
    unknowns: []                        # 全局未知清单（关键 Unknown 优先）
    sources: []                         # 来源去重后的证据源列表
    confidence: High | Medium | Low     # 汇总置信度（与 score.confidence 一致）

## 2. 字段 ↔ V4 产物映射（禁止重复定义）

| Context 字段 | 唯一权威来源（V4） |
|---|---|
| idea / observation | 用户输入 + 日常观察训练 |
| problem | templates/problem-card.md |
| evidence | templates/evidence-card.md + templates/v3-evidence-board.md |
| evidence.coverage | references/v3-evidence-coverage.md |
| opportunity | templates/opportunity-card.md + templates/demand-validation-card.md |
| criteria / score | references/v3-scoring.md + v3-scoring-rubric.md + v3-confidence.md + v3-hard-gates.md |
| validation | references/v4-validation.md + templates/v4-validation-card.md |
| decision | references/v3-decision.md + 停止机制 |
| action | references/v3-action-plan.md |
| unknowns / sources | 由各阶段累计，Main 汇总 |

## 3. 复用规则（减少重复工作，硬性要求）

1. **Evidence Reuse**：evidence 字段非空且用户未提供新资料 → 禁止重新搜索；Evidence Hunter 只做“缺口搜索”（critical_gaps 指向的维度）。
2. **State Reuse**：history 中已完成的 State → 不重跑；中途进入只补缺失阶段。
3. **Context Reuse**：字段非空 → 不重复询问用户。
4. **Source Reuse**：sources 去重后引用，同源转载不重复计分（v3-evidence-coverage.md 规则）。
5. **User Input Reuse**：用户一句话同时满足多个字段时，一次写入全部字段，不拆成多轮提问。

## 4. 读写规则

- 写入：每个 Specialist 只写自己负责的字段（见 orchestrator/state.md 生产方列），不代写其他字段。
- 读取：Specialist 只读输入契约所需字段；读取不到时返回 MISSING_INPUT，不自行推倒重来。
- 冲突：新旧信息冲突时保留双方，冲突字段置 TO VERIFY 并记入 unknowns，由验证步骤解决（见 routing.md 第 2 节）。
- 版本：context_version 固定 5.0.0；升级规则变更时先迁移字段再继续，禁止半迁移状态运行。

## 4.5 Mode 语义边界（V4 Mode 与 V5 Orchestration Mode 是两个维度）

- **V4 Mode**（mode 字段）：采用哪种已有工作方式/能力深度——Quick（轻量判断）、Research（完整研究）、Execution（停止研究直接执行）。决定"用什么方式做"。
- **V5 Orchestration Mode**（orchestration_mode 字段）：怎么进入与调度——Full（完整流程）、Focused（点名能力）、Mid-entry（中途进入）、Independent（独立调用）。决定"从哪进、调谁"。
- **两层正交、不互相竞争**：V5 Routing 先定 orchestration_mode，再按 V4 Mode 决定工作方式。合法组合示例：Research + Focused（深挖某个能力）、Quick + Full（快速走完整链）、Execution + Mid-entry（已有结论直接执行）。
- 禁止把 Research 理解成 Focused，也禁止把 Focused 当成 V4 Mode；两个字段必须分开记录、分开解释。

## 5. 持久化与跨会话

- 保存：用户可要求“保存当前分析”，输出 templates/v5-context-card.md 填充件（含本契约 YAML + 各阶段结论摘要）。
- 恢复：新会话中用户提供该文件或关键字段 → 按 orchestrator/state.md 第 5 节重建 State。
- 隐私：Context 可能包含用户业务信息；输出到文件时提示用户自行保管，不写入公开位置。

## 6. Context 自检（每次写入后）

- [ ] state 与最新写入字段一致
- [ ] 没有字段被非生产方覆盖
- [ ] 复用的字段没有被重复搜集
- [ ] 冲突都有 TO VERIFY 标记并记入 unknowns
- [ ] sources 去重完成，Unknown 有清单

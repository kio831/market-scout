# MarketScoutContext 状态卡（v5.0.0）

> V5 统一上下文的工作文件：保存当前分析的 State 与全部阶段结论，用于跨会话续跑（orchestrator/state.md 第 5 节）。
> 字段契约见 orchestrator/context.md；本卡与 Opportunity Report V3 不同——本卡是**状态容器**，报告是**结论输出**。

## 状态头

| 项 | 值 |
|---|---|
| context_version | 5.0.0 |
| opportunity_id | MS-### |
| mode | quick / research / execution |
| orchestration_mode | full / focused / mid-entry / independent |
| state | IDEA / OBSERVATION / PROBLEM / EVIDENCE / OPPORTUNITY / SCORED / VALIDATION / DECISION / ACTION |
| history | IDEA → …（已完成的 State 序列） |
| produced_by | （最近一次写入的 Specialist / Main） |

## 1. Idea（用户原始输入）

    text: ""
    source: ""

## 2. Observation（Idea Observer 产出）

    who: ""
    problem: ""
    frequency: ""
    current_solution: ""
    payment_signal: ""
    ai_leverage: ""
    hypothesis_flags: []

## 3. Problem（Problem Scout 产出）

    target_user: ""
    scenario: ""
    evidence_level: A / B / C
    category: ""

## 4. Evidence（Evidence Hunter 产出）

    chain:
      - evidence: "" / source: "" / type: "" / confidence: "" / proves: "" / not_proves: ""
    board: （三态看板摘要 + 充分度）
    coverage: problem _ / solution _ / payment _ / competition _ / distribution _ / buildability _
    overall_coverage: _
    critical_gaps: []
    search_capability: true / false

## 5. Opportunity（Opportunity Scout 产出）

    state: HYPOTHESIS / DEMAND_CONFIRMED / MARKET_CONFIRMED / …
    bottleneck: ""
    demand_summary: ""
    competition_gap: ""

## 6. Criteria + Score（Opportunity Score 产出）

    criteria_locked: true
    dims: demand _ / pain _ / competition _ / monetization _ / buildability _ / distribution _ / ai _
    total: _
    formula: ""
    confidence: score _ / level _
    hard_gates: gate _ / ceiling [] / red_flags []

## 7. Validation（Validation Scout 产出）

    plan: core_hypothesis "" / method "" / sample _ / duration "" / cost "" / success "" / failure "" / decision_rule ""
    experiment: done true/false / detail ""
    result: sample_n _ / interested _ / trial _ / paid _ / revenue _ / observed [] / inference [] / unknown []

## 8. Decision（Main 产出）

    code: RECOMMENDED / POTENTIAL / NOT_RECOMMENDED
    verdict: BUILD / VALIDATE / RESEARCH / PARK / KILL
    why: []
    restart_conditions: []

## 9. Action（Main 产出）

    plan: []
    today: ""

## 10. 全局清单

    assumptions: []
    unknowns: []
    sources: []
    confidence: High / Medium / Low

## 自检（保存前确认）

- [ ] state 与最后完成的产物一致
- [ ] 四套代码（证据等级 / Opportunity State / Pipeline State / Decision Code）未混用
- [ ] 无重复搜集（已有证据未重搜）
- [ ] Unknown 有清单，无冒充完成

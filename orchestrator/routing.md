# Routing Engine 路由引擎（v5.0.0 新增）

> Main Skill 收到用户请求后，**先判断用户当前状态与意图，再决定调用什么**，而不是机械地从头跑完整流程。
> 本文件定义：输入预处理 → 状态检测 → 意图识别 → 模式判定 → Specialist 选择 → 降级与日志。
> 意图识别的主体规则沿用 SKILL.md 的“模式路由（细粒度）”表，本文件在其上加状态维度。

## 1. 路由流水线（固定顺序）

    用户输入
      → 1. 输入预处理（空/模糊/超长/多意图）
      → 2. State Detection（用户现在在哪里）
      → 3. Intent Detection（用户想要什么）
      → 4. Mode 判定（FULL / FOCUSED / MID-ENTRY / INDEPENDENT）
      → 5. Specialist 选择（含缺失输入的最小补位）
      → 6. 执行 → 写回 Context → 检查停手与降级 → 决定下一步

## 2. 输入预处理（异常输入处理）

| 输入情况 | 处理规则 |
|---|---|
| 空输入 / 只有“你好”“在吗” | 不启动流程，返回最简引导：当前可以给我 1) 一个想法 2) 一个问题 3) 一份研究材料 4) 一个已完成的评分，我来判断从哪一步继续 |
| 模糊输入（无法判断状态或意图） | 按优先级链自选：含问题陈述 → 从 IDEA/OBSERVATION 开始；含资料/搜索结果 → 从中途 EVIDENCE 进入；含“值不值得/打分/决策” → 直接 SCORING；仍无法判断 → 默认 Full Mode 从 IDEA 开始并声明假设 |
| 超长输入 | 先抽核心信号（谁/什么问题/有没有现有方案/有没有付费迹象），超过上下文承载时提示用户分批提供，不截断丢弃证据 |
| 多意图输入（如“这个视频能赚钱吗”） | 按链式推进：Reverse Observation → Evidence → Payment → 需要时 Opportunity，不停在半路（沿用 SKILL.md 模式路由规则） |
| 信息与 Context 冲突 | 不静默覆盖：保留新旧双方，标记 TO VERIFY，进入验证步骤时优先解决 |
| 重复调用同一阶段 | 若目标 State 已达成且用户未提供新信息：先确认“已有 X 结果，是否需要基于新信息重跑？”，不自动重跑（“重新评分”是显式重跑意图，除外） |

## 3. State Detection（状态检测）

根据 Context 已有字段 + 用户本次输入内容，判断用户当前所在的 State（完整定义见 orchestrator/state.md）：

| 检测到的事实 | 判定 State |
|---|---|
| 只有一句原始想法/现象，无任何卡片 | IDEA |
| 已拆出谁/什么问题/频率/当前方案等信号 | OBSERVATION |
| 已有 Problem Card 或明确问题定义 | PROBLEM |
| 已有搜索结果/资料/证据清单 | EVIDENCE |
| 已有机会描述/需求验证结论 | OPPORTUNITY |
| 已有 7 维评分/分数 | SCORED |
| 已有验证计划或实验结果 | VALIDATION |
| 已有 RECOMMENDED/POTENTIAL/NOT_RECOMMENDED 结论 | DECISION |
| 已有行动计划/今天做什么 | ACTION |

检测规则：**取所有已满足状态中的最高者**；同时输出 missing_states（当前态与 ACTION 之间缺失的状态），供路由补位。

## 4. Intent Detection（意图识别）

意图识别复用 SKILL.md“模式路由（细粒度）”完整表作为第一层（Quick / Research / Execution / V3 决策 / V4 验证），V5 只做状态化映射：

| 用户意图（示例） | 命中 Specialist | 输出 |
|---|---|---|
| 随手抛一个想法/现象 | Idea Observer（或 Full Mode 起点） | observation 信号 |
| 把观察变成清楚的问题定义 | Problem Scout | Problem Card |
| “帮我找这个问题的真实需求”“找证据”“市场上有谁在解决” | Evidence Hunter | Evidence Chain + Coverage |
| “有没有人做”“竞品怎么样”“切入空间在哪” | Evidence Hunter（Solution/Payment）+ Opportunity Scout | 竞争与空缺 |
| “做成什么机会”“需求真的吗”“值不值得继续研究” | Opportunity Scout（机会判断类按需续接 Opportunity Score → Main，对齐 SKILL.md 模式路由 V3 决策层） | Opportunity Card → Score → Decision |
| “打个分”“机会评分”“重新评分” | Opportunity Score | Score + Confidence + Gates |
| “帮我验证”“怎么验证”“我验证了 N 个人，结果…” | Validation Scout | Validation Plan / Result |
| “帮我决策”“值不值得做” | Main（不派 Specialist） | Decision + 动作裁决 |
| “下一步做什么”“今天做什么” | Main（读 Context） | Action Plan |

## 5. 路由优先级（P0）：Explicit Focused > Existing State > Full Workflow

V4 的模式路由与 V5 的状态/意图路由必须按以下**唯一优先级链**裁决，禁止并行猜测：

    1. Explicit Focused Intent（用户明确点名某个能力）
         → 直接进入 Focused（或 Independent），只调用对应 Specialist
    2. Existing Context / State（已有上下文或续跑意图）
         → Mid-workflow Entry：从最高已完成 State 的下一缺失阶段续跑
    3. Full Workflow（既无明确 Focus，也无已有状态）
         → Full Mode：从头走完整流程

判定顺序（每条输入都依次过三问）：
- **Q1** 用户是否明确要求某个具体能力？（“只要证据”“重新评分”“怎么验证”“帮我决策”等能力关键词）
  是 → 优先级 1：Focused / Independent，按第 6 节执行；已存在字段只读不重做。
- **Q2** Context 中是否已有未完成的分析状态？（含“继续”“接着上次”“续上”“上次说到哪了”等续跑意图）
  是 → 优先级 2：Mid-entry，从当前 State 的下一缺失阶段续跑；已有字段不重复搜集。
- **Q3** 两者都没有？
  是 → 优先级 3：Full Workflow，从 IDEA 开始。

补充规则：
- “继续 / 接着上次 / 续上 / 上次说到哪了”是**显式续跑意图** → 进入 Q2，按 State Detection 取最高已完成 State 续跑；Context 缺失时按 orchestrator/state.md 第 5 节恢复。
- 显式 Focus 与已有状态同时出现（如“已有证据，帮我打个分”）→ Focus 优先（Q1 通过即走 Focused），只补最小缺失输入，不重跑已有字段。
- 多意图输入（“这个视频能赚钱吗”）按第 2 节链式推进，不受本优先级影响。
- 低质量机会 / 证据不足同样走本优先级链；最终裁决由停手权约束（PARK / KILL / RESEARCH / VALIDATE），与路由优先级无关。

## 6. Mode 判定与调度（四种模式）

### 6.1 Full Mode
触发：用户只有一个想法且要求完整分析（或模糊输入默认路径）。
调度：依次调用 Idea Observer → Problem Scout → Evidence Hunter → Opportunity Scout → Opportunity Score → Main 决策门 →（需要时）Validation Scout → Main 重判 → Main Action。

### 6.2 Focused Mode
触发：用户明确点名某个能力。
调度：只调用对应 Specialist；调用前检查其输入契约字段是否齐备——缺则先补最小缺失阶段（一次），补完立即回到目标 Specialist，不继续向后跑。**补位由 Main Orchestrator 发起并执行，Specialist 只负责返回 MISSING_INPUT。**
示例：
- “帮我找这个问题的真实需求” → Evidence Hunter（若 Context 无 PROBLEM，先由 Problem Scout 补问题定义）
- “帮我重新评分” → Opportunity Score（若无 OPPORTUNITY，先由 Opportunity Scout 补机会卡）
- “这个项目怎么验证” → Validation Scout（若无 SCORED，先由 Opportunity Score 补评分）

### 6.3 Mid-workflow Entry（中途进入）
触发：用户已有部分成果（自带资料或历史会话）。
规则：
- 从最高已完成 State 的下一个缺失 State 开始，**不重跑已完成阶段，不重复搜索已有证据**。
- 用户自带资料时，把资料先归入对应字段（Problem/Evidence/Score），再按缺失链续跑。
- 只有用户明确说“全部重新来”才允许重置 Context。

### 6.4 Independent Specialist（独立调用）
触发：用户直接以 Specialist 身份发起（如“用 Evidence Hunter 分析这个问题”），或安装包外单独安装某个 Specialist 后直接触发。
规则：该 Specialist 按自身输入契约独立执行，输出独立的卡片/看板；不要求也不假设后续阶段会运行。输入不足时按该 Specialist 的独立输入规则处理（询问最小必要信息或声明 Unknown）。

### 6.5 V4 Mode 与 V5 Orchestration Mode 是两层，不互相竞争

    User Input
      → V5 Orchestrator Routing（本文件第 5 节）
      → 确定 orchestration_mode：Full / Focused / Mid-entry / Independent（怎么进入和调度）
      → 再按 V4 Mode 决定工作方式：Quick / Research / Execution（用哪种已有能力深度）
      → Specialist（执行）

- **V5 Routing 决定“怎么进入和调度”**；**V4 Mode 决定“采用哪种已有工作方式/能力”**。两者正交并存，禁止互相替代。
- 记录要求：Context 中 mode 字段只写 V4 三模式，orchestration_mode 字段只写 V5 四模式（见 context.md 第 4.5 节）。

## 7. Specialist 选择表（缺失输入最小补位）

    〉目标 Specialist     〉所需输入           〉缺失时的最小补位
    Idea Observer        idea                （起点，无需补位）
    Problem Scout        observation         Idea Observer
    Evidence Hunter      problem             Problem Scout
    Opportunity Scout    problem+evidence    Evidence Hunter（只做缺口搜索）
    Opportunity Score    opportunity+evidence Opportunity Scout
    Validation Scout     opportunity+score    Opportunity Score

补位规则：
- 一次只向前补**一个**阶段；补位用的 Specialist 也要遵守“已有信息足够则不重复搜索”。
- **补位只由 Main Orchestrator 发起**：Specialist 发现输入缺失时只返回 MISSING_INPUT（注明缺什么字段），**禁止 Specialist 自行调用其他 Specialist 或自行补位**。Main Orchestrator 是唯一的流程调度者。

## 8. 降级 Fallback 与日志

- Specialist 执行失败：读对应 reference 重试一次 → 用用户材料降级 → 标记 Unknown 继续；单点失败不中断链路。
- 无搜索能力：声明“【当前无法进行实时市场验证，以下属于假设分析】”，全部结论标假设（V4 铁律第 2 条），Evidence Hunter 输出 Coverage=0 并注明原因；路由仍然继续，但决策自动受 Score Ceiling 约束。
- 搜索无结果：输出 Evidence Insufficient + 缺失项清单，不编造；决策走 PARK / RESEARCH / 最高 POTENTIAL 分支（见 architecture.md 6 节）。
- 日志要求：每次路由记录一行——输入摘要、检测到的 State、Mode、选中 Specialist、输出 State、是否有降级（用于跨会话续跑与复盘，不向用户展示内部日志）。

## 9. 路由自检（每次路由后）

- [ ] State 与 Mode 有明确依据（来自哪条输入/字段）
- [ ] 没有要求用户重复提供已存在的信息
- [ ] 没有安排已完成阶段的重复执行
- [ ] 输出指向了明确的 Specialist 或 Main 决策门
- [ ] 异常输入落入了第 2 节对应分支，没有静默吞掉

## 10. 异常输入 → 处理位置速查表

| 异常输入 | 处理位置 |
|---|---|
| 空输入 | 第 2 节 |
| 模糊输入 | 第 2 节 |
| 超长输入 | 第 2 节 |
| 信息冲突 | 第 2 节 + architecture.md 第 8 节 |
| 搜索无结果 | 第 8 节（降级）+ architecture.md 第 8 节 |
| 上下文缺失 | 第 2 节 + state.md 第 5 节（State Recovery） |
| Specialist 执行失败 | 第 8 节（降级） |
| 重复调用 | 第 2 节 |
| 阶段已经完成 | 第 2 节 + state.md 第 6 节 |
| Validation 无法进行 | 第 8 节（PARK + 重启条件）+ state.md 第 6 节 |

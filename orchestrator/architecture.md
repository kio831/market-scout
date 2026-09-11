# V5 Orchestrator 架构总览（v5.0.0 新增）

> 本文件是 V5 的**总控层**说明：Main Skill（SKILL.md）如何调度六个 Specialist、如何维护统一 Context 与 State、如何最终给出 Decision + Action。
> 配套文件：orchestrator/routing.md（路由引擎）、orchestrator/state.md（状态机）、orchestrator/context.md（统一上下文契约）。
> 原则：**V5 不是重写 V4**。V4 的全部能力（Search First、三类搜索、Evidence Chain、Problem Card、Opportunity 分析、评分、Validation、Decision、Stop Rules）原样保留，V5 只是把它们封装成可路由、可跳转、可独立调用、可组合的模块。

## 1. 总体结构

    ┌───────────────────┐
    │  Main Skill        │
    │  SKILL.md          │
    │  Orchestrator      │
    │  • Routing Engine  │
    │  • State Detection │
    │  • Workflow Control│
    │  • Decision+Action │  ← 停手权保留在主控层
    └─────────┬─────────┘
              │ 读/写
              ▼
    ┌───────────────────┐
    │  Shared Context    │
    │  MarketScoutContext│
    │  （9 态状态机）    │
    └─────────┬─────────┘
     ┌────────┼────────┐
     ▼        ▼        ▼
  Idea    Problem   Evidence
  Observer Scout    Hunter
     └────────┬────────┘
              ▼
     Opportunity Scout
              ▼
     Opportunity Score
              ▼
     Validation Scout
              ▼
     Decision + Action（Main）

## 2. 组件职责

| 组件 | 类型 | 职责 | 对应 V4 能力（复用） |
|---|---|---|---|
| Main Skill | Orchestrator | 状态检测、意图识别、路由、调度、汇总 Decision + Action、停手权 | SKILL.md 全部铁律与路由表 |
| Idea Observer | Specialist | 想法 → 观察信号（谁/什么问题/频率/当前方案/付费信号/AI 杠杆） | 日常观察训练、视频/评论区反向分析 |
| Problem Scout | Specialist | 观察 → Problem Card（目标用户、场景、证据等级） | templates/problem-card.md、problem-framework.md |
| Evidence Hunter | Specialist | 问题 → 三类搜索 → Evidence Chain → Evidence Board + Coverage | Search First、market-research.md、evidence-chain.md、v3-evidence-coverage.md |
| Opportunity Scout | Specialist | 问题 + 证据 → 需求验证 + 竞争切入空间 → Opportunity Card | demand-validation.md、v3-scoring.md 切入空间四问 |
| Opportunity Score | Specialist | 机会 + 证据 → 7 维评分 + Confidence + Hard Gates | v3-scoring-rubric.md、v3-confidence.md、v3-hard-gates.md |
| Validation Scout | Specialist | 机会 + 分数 → Validation Plan → 实验 → 结果分级 → 重算输入 | v4-validation.md、templates/v4-validation-card.md |
| Decision + Action | Main 保留 | 依据完整 Context 给出 BUILD / VALIDATE / RESEARCH / PARK / KILL | v3-decision.md、停止机制、v3-action-plan.md |

## 3. 依赖方向（禁止循环）

    Main Orchestrator
       └─▶ Specialist（只做专业能力，不互相调用）
              └─▶ Shared Context（读写）
                     └─▶ Main Orchestrator（读结果 → 决定下一个 Specialist）

- **Main 负责调度，Specialist 负责专业能力**。Specialist 之间禁止互相调用（不出现 A → B → C → A 的环）。
- 每个 Specialist 只依赖：输入的 Context 字段 + 对应的 V4 reference/template。
- 若 Specialist 发现输入缺失，**不擅自向前补做**其他 Specialist 的工作，而是返回 MISSING_INPUT，由 Main 决定补做最小缺失阶段。

## 4. 完整默认流程（Full Mode）

    IDEA（用户输入想法）
      → [Idea Observer]       → OBSERVATION
      → [Problem Scout]       → PROBLEM
      → [Evidence Hunter]     → EVIDENCE（三类搜索 + 证据链 + Coverage）
      → [Opportunity Scout]   → OPPORTUNITY（需求 + 竞争切入空间）
      → [Opportunity Score]   → SCORED（7 维 + Confidence + Hard Gates）
      → [Main] 决策门          → DECISION（RECOMMENDED / POTENTIAL / NOT_RECOMMENDED）
      → [Validation Scout]    → VALIDATION（当需要验证时；Validate before Build）
      → [Main]（结果重算）     → DECISION（再次判断，Reality > Prediction）
      → [Main]                → ACTION（类型化行动计划 + 今天做什么）

不允许因为模块化丢失闭环：任意一次完整运行必须能从头走到 ACTION；中途进入时只跳步，不省略决策与行动。

## 5. 四种运行模式

| 模式 | 触发 | 行为 |
|---|---|---|
| **Full Mode 完整流程** | 用户只有一个想法/问题，要求完整分析 | 按 4 节顺序走完，每步由一个 Specialist 执行 |
| **Focused Mode 聚焦调用** | 用户点名某一能力（“只要证据”“重新评分”“怎么验证”） | 只调用对应 Specialist，不强制全流程 |
| **Mid-workflow Entry 中途进入** | 用户已有 Problem/Evidence/Score 等部分成果 | 从当前状态直接续跑，**不重复已完成阶段** |
| **Independent Specialist 独立调用** | 用户直接以 Specialist 身份触发 | 该 Specialist 按自身输入契约独立工作，输出独立成果 |

路由判定细节见 orchestrator/routing.md。

## 6. Decision + Action（主控层保留，含停手权）

### 6.1 机会决策（沿用 V4 三档，不新增第四档）

| V4 决策码 | 含义 | V5 动作裁决 |
|---|---|---|
| RECOMMENDED | 值得继续做 | **BUILD**（若 V4 检查仍要求先验证 → **VALIDATE**） |
| POTENTIAL | 有机会但需先验证 | **VALIDATE**（证据覆盖过低且用户要求深挖 → **RESEARCH**） |
| NOT_RECOMMENDED | 当前不建议投入 | **PARK**（暂缓，列出重启条件）或 **KILL**（红旗/硬门槛，明确否定） |

### 6.2 动作裁决五态

- **BUILD**：证据、门槛、验证结果都支持进入 MVP/产品化（仍然先做最小方案，不跳级做完整 SaaS）。
- **VALIDATE**：关键 Unknown（通常是付费意愿）未解 → 由 Validation Scout 设计最低成本验证再回来。
- **RESEARCH**：证据覆盖过低、用户明确要求继续深挖（Quick → Research 升级）。
- **PARK**：证据不足以支持投入，但未来可能出现新证据（列出重启条件，与 V4 停止机制一致）。
- **KILL**：红旗 / Hard Gate 触发，当前证据不支持继续投入（明确否定，不强行制造机会）。

### 6.3 停手权（有停手权，铁律不变）

- V4 铁律第 5、6 条原样生效：证据不足、无重复需求、无付费行为、AI 无优势、竞争壁垒过高、个人无法低成本完成、用户无法触达 → 输出【不建议继续】或 PARK/KILL。
- **禁止为了让系统“看起来完成了闭环”而强行建议 BUILD。** 闭环完整 ≠ 结论一定是正向。
- 每个停止/暂缓结论必须给出：1) 为什么停止；2) 哪个证据导致停止；3) 未来出现什么新证据可重启。

## 7. 与 V4 的关系（兼容性承诺）

- V4 已存在并验证的能力**全部保留**，本架构不删除、不弱化、不重写任何核心逻辑。
- 六个 Specialist 只是把 SKILL.md 标准工作流第 1-9 步与 V3/V4 决策层**按责任封装**，方法细节仍指向原有 references/templates。
- V4 的三种工作模式（Quick / Research / Execution）与细粒度模式路由表**原样保留**，V5 在其上增加“状态维度”的路由。
- 冲突时优先级：V4 已验证功能 > 用户实际使用效果 > 兼容性 > V5 模块化架构 > 代码结构美观。

## 8. 错误处理与降级（运行要求）

- 每个 Specialist 执行失败时：读取对应 reference 重试一次 → 降级为使用用户材料 → 仍不行则标记该字段为 Unknown 并继续，不让单点失败中断整条链路。
- 所有外部搜索/网络调用遵守 pipeline-and-runtime.md 第 3 节：超时、指数退避重试、确定性错误不重试、失败按“换来源 → 用用户材料 → 标【证据不足】”降级。
- 上下文缺失：从最近一个已完成的 State 续跑，只补最小缺失阶段（见 orchestrator/state.md 第 5 节）。
- 信息冲突：不静默平均，保留双方并标记 TO VERIFY，由下一步验证解决。
- 搜索无结果：明确输出 Evidence Insufficient，按规则降级决策（Coverage 低 → Score Ceiling → 最高 POTENTIAL / PARK），**不编造证据**。
- 验证无法进行（无可触达用户）：输出 PARK 及重启条件，不强行设计虚假实验。

## 9. 交付前自检（每次完整运行结束检查）

- [ ] Context 中 state 反映最新已完成阶段，history 连续
- [ ] 每个关键结论有 Evidence / Inference / Unknown 标注，无虚构
- [ ] Score 附可复算公式；Decision 附编号 Why；Action 含“今天做什么”
- [ ] 停手权生效：不该推荐时没有推荐 BUILD
- [ ] 无重复研究：已有证据未被重新搜索

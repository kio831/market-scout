---
name: market-scout
description: 市场侦察与商业验证工作流（Market Scout，v3.0.0）。完整链路 Find 发现 → Validate 需求验证 → Evaluate 项目评估 → Blueprint 机会转项目 → Monetize 商业化与获客（Find → Validate → Evaluate → Monetize）。当用户想做 AI 赚钱副业、找市场需求、发现痛点、分析视频/评论区/帖子隐含商机、判断"某问题/工具能不能用 AI 解决""这件事能不能赚钱、值不值得做"、验证需求是否真实、评估项目可行性与综合机会评分、把机会转成 MVP/项目方案、设计商业模式/定价/获客/第一批客户、寻找竞争对手、做市场调研、拿第一单/第一笔钱、把 AI 能力变现、验证创业点子，或提到"帮我找市场""分析这个视频/评论区""我发现一个问题""这个能不能用 AI""这个能不能赚钱""值不值得做""需求是不是真的""评估一下这个项目""帮我做成产品/MVP""怎么收费/定价""怎么找客户/第一批用户""商业模式怎么设计""帮我拿第一单""继续深挖""寻找类似需求/竞争对手""出一份机会报告/Opportunity Report"时使用。核心原则 Search First（优先实时搜索而非模型记忆），绝不虚构用户、价格与数据；沿用 v1.1 的 Evidence Chain 证据链、Problem/Solution/Payment 三类搜索、Quick/Research/Execution 三模式、Opportunity 交付状态机（HYPOTHESIS→…→PRODUCTIZED）与证据绑定评分；v2.0 新增 Demand Validation 需求验证（痛点/目标用户/需求强度/当前方案/付费理由/证据可信度）、Project Evaluation 项目评估（市场潜力/竞争/差异化/AI 可实现度/开发难度/个人适配/风险，加权综合机会评分 0-100，结论三档：值得做 GO/建议验证后再做 VALIDATE FIRST/不建议做 NO-GO）、Project Blueprint 机会转项目（产品形态/核心用户/核心功能/MVP/技术方向/最小验证/差异化切入点）、Monetization & GTM 商业化获客（Target Customer/Offer/Business Model/Pricing/首批客户/渠道/GTM 路径/无产品验证，模块化设计、预留独立成产品的数据契约，当前不开发支付订阅会员），最终输出结论先行的 Opportunity Report/Opportunity Card。证据等级 A/B/C、交付状态名、V2 流水线阶段名三者相互独立，不共用代码。v3.0 新增决策层：证据三态 Evidence/Inference/Unknown、7 维机会评分 0-100（需求/痛点/竞争切入空间/变现/开发/获客/AI 优势，加权可复算）、三档机会决策（值得继续做 RECOMMENDED / 有机会但需先验证 POTENTIAL / 不建议投入 NOT_RECOMMENDED）、MVP Blueprint 九字段与按机会类型动态生成的 Action Plan；当用户说"打个分""值不值得做""帮我决策""机会评分""第一版做什么""MVP""下一步做什么""今天做什么"时进入 V3 决策层。
---

# Market Scout (v3.0.0)

**Find 发现 → Validate 验证 → Evaluate 评估 → Blueprint 转项目 → Monetize 商业化** 的完整市场机会工作台。
市场侦察 + 需求发现 + 需求验证 + 项目评估 + AI 解决方案/项目设计 + 商业化与获客。
不是"AI 赚钱项目生成器"，而是把真实问题跑成"是否值得做的结论 + 可执行项目 + 第一笔收入路径"的流程工具。

> **v2.0 增量说明**：v1.1 的全部能力（三类搜索、证据链、三模式、8 维证据绑定评分、Level 1-5、状态机、停止机制、第一笔钱、模板与示例）**全部保留并被复用**；v2.0 在其后串接需求验证、项目评估、机会转项目、商业化获客四个新阶段，编排与数据契约见 `references/pipeline-and-runtime.md`。

> **v3.0 增量说明**：v2.0.0 的全部能力（五阶段流水线、三种模式、铁律、停止机制、第一笔钱清单、模板与示例）**全部保留**；v3.0 在其上新增**决策层**（Evidence 证据三态 → Opportunity Score 7 维 0-100 → Decision 三档 → MVP Blueprint → 动态 Action Plan），让分析结果最终产生"决策"。编排与数据契约见 `references/v3-overview.md`。
## 核心定位

先问**"谁遇到了什么问题？为什么愿意付钱解决？"**，再问**"AI 能否让我更低成本、更快地解决它？"**。

最终形成：`真实问题 → 证据 → 需求 → 付费 → 竞争 → AI 杠杆 → 最小方案/MVP → 真实用户 → 第一笔钱 → 标准化 → 自动化 → 产品化`。

核心原则：
- **先验证，再收费，再产品化。**
- 禁止默认"先开发产品 → 再寻找用户"。
- 必须优先"先发现问题 → 搜集证据 → 验证需求 → 验证付费 → 再决定是否开发"。
- 最终目标不是生成漂亮的市场报告，而是把一个问题推进到**第一次真实交易**。

核心闭环：

```
发现问题 → 搜集证据 → 判断需求 → 判断付费 → 分析竞争 → 判断 AI 杠杆
→ 设计最小解决方案 → MVP → 找真实用户 → 交付 → 获得第一笔钱
→ 复盘 → 标准化 → 自动化 → 产品化
```

## V2 主链路：Find → Validate → Evaluate → Monetize（P0）

v2.0 把工作流升级为五个顺序阶段（编排、熔断、断点续跑、数据契约见 `references/pipeline-and-runtime.md`）：

```
FIND 发现            VALIDATE 需求验证       EVALUATE 项目评估
(v1.1 三类搜索、   →   (demand-           →   (project-
 证据链、Problem卡)     validation.md)          evaluation.md)
   ↓                      ↓                       ↓
BLUEPRINT 机会转项目 → MONETIZE 商业化获客 → REPORT 机会报告
(project-blueprint.md)  (monetization-gtm.md)    (templates/opportunity-report.md)
```

| 阶段 | 回答的核心问题 | 方法论 | 输出卡片 |
|---|---|---|---|
| FIND 发现 | 有没有真实问题/现有方案/付费行为？ | `market-research.md`、`evidence-chain.md` | Problem/Evidence Card（v1.1） |
| VALIDATE 需求验证 | 需求真不真、强不强、为何愿意付钱？ | `demand-validation.md` | `templates/demand-validation-card.md` |
| EVALUATE 项目评估 | 作为项目值不值得我投入？综合分多少？ | `project-evaluation.md` | `templates/project-evaluation-card.md` |
| BLUEPRINT 转项目 | 做成什么产品/MVP？怎么验证？ | `project-blueprint.md`（复用 Level 1-5） | `templates/project-blueprint-card.md` |
| MONETIZE 商业化获客 | 谁付钱/卖什么/怎么收费/去哪找/第一批客户怎么来？ | `monetization-gtm.md`（复用第一笔钱清单） | `templates/monetization-gtm-card.md` |
| REPORT | 一张报告判断是否值得做 + 第一步行动 | `pipeline-and-runtime.md` §4 | `templates/opportunity-report.md` |

### 四大新增能力要点

1. **Demand Validation 需求验证**：用户痛点、目标用户三层（核心/扩展/非用户）、需求强度 6 信号合成 1-10、当前解决方案与替代成本、付费理由链（JTBD 5 环）、需求证据可信度；结论三选一（真实需求已验证 / 需求存在但付费未验证 / 伪·弱需求）。
2. **Project Evaluation 项目评估**：7 维加权评分（需求 20%、市场 20%、竞争差异 15%、AI 可实现 15%、开发难度 10%、个人适配 15%、风险 5%）→ 综合机会评分 0-100，**计算式必须可复算**；结论三档 **🟢 值得做 GO / 🟡 建议验证后再做 VALIDATE FIRST / 🔴 不建议做 NO-GO**，由"总分 + 门槛项 + 致命红旗"共同决定，不只看总分；7 条致命红旗一票否决。
3. **Opportunity → Project 机会转项目**：推荐产品形态（对齐 Level 1-5，默认 L1 先卖结果）、核心用户、MoSCoW 核心功能（M≤3）、MVP 五项、推荐技术方向、最小验证实验、差异化切入点落地。
4. **Monetization & GTM 商业化获客**：Target Customer（区分使用者与付费方）、Offer 三档阶梯、Business Model 模式库与选择规则、可解释 Pricing、首批 10 客户获取、渠道矩阵（早期主渠道≤2）、GTM 三阶段、不开发产品的 7 种验证方式、第一笔钱计划。

### 商业化模块的独立化边界（未来设计，当前不实现支付系统）

- Monetization & GTM 是**模块化能力**：有明确输入契约 MonetizationInput 与输出契约 MonetizationPlan（见 `monetization-gtm.md` §8），只依赖结构化数据、不依赖 UI 与其他阶段内部实现。
- 未来可将其独立成产品、独立收费、独立获客，只需按契约喂数据/渲染结果，**无需大规模重构**。
- **当前版本明确不开发**支付、订阅、会员、计费等任何系统，只产出商业化方案与验证动作。

### 三套"代码/状态"互不混淆（重要）

- **证据等级 A/B/C**：需求验证程度（`problem-framework.md` §3）。
- **Opportunity State**：真实世界交付状态（HYPOTHESIS→…→PRODUCTIZED，`opportunity-state-machine.md`），FIRST_PAYMENT 必须真实收款。
- **Pipeline Stage（v2.0 新增）**：分析流水线位置（FIND/VALIDATE/EVALUATE/BLUEPRINT/MONETIZE/REPORT）。
三者正交，例如 `Pipeline=MONETIZE / State=DEMAND_CONFIRMED / 证据等级=B` 完全合法，禁止用一套字母表达多个含义。

## V3 决策层：Evidence → Score → Decision → MVP → Action（v3.0.0 新增）

V2 把机会分析清楚，V3 把分析压缩成**用户 10 秒能看懂、且能照着行动的决策**。V3 不是重做 Market Scout，而是让 V2 的分析结果最终产生"决策"。主流程九步（编排与数据契约见 `references/v3-overview.md`）：

```
INPUT 用户输入想法/问题/机会
  → DISCOVERY 发现用户与痛点（复用 FIND）
  → VALIDATION 验证需求与市场（复用 VALIDATE）
  → EVIDENCE 证据归一化（Evidence/Inference/Unknown + 充分度）
  → COMPETITION 竞品与市场空缺（复用竞争分析 + 切入空间判定）
  → SCORING 计算 Opportunity Score（7 维 0-100 可复算）
  → DECISION 判断值不值得做（RECOMMENDED/POTENTIAL/NOT_RECOMMENDED）
  → MVP 生成 MVP Blueprint（9 字段）
  → ACTION 生成下一步行动计划（按机会类型动态生成）
```

### 五个新增能力要点

1. **Market Evidence 市场证据**：每个关键结论标注 Evidence（找到的公开信息）/ Inference（推导判断）/ Unknown（信息不足）；证据充分度三级；Unknown 按 0 计并显式标注，不编造、不虚高（`v3-evidence.md`）。
2. **Opportunity Score 机会评分**：7 维加权 0-100（需求 15 / 痛点 15 / 竞争切入空间 15 / 变现 20 / 开发 15 / 获客 10 / AI 优势 10），每维拆 3-4 个 1-10 子信号，计算式必须可手工复算；**竞争维度禁止"竞争低=高分"**，分数=切入空间大小，四问必答（`v3-scoring.md`）。
3. **Decision 机会决策**：三档 RECOMMENDED（值得继续做）/ POTENTIAL（有机会但需先验证）/ NOT_RECOMMENDED（不建议投入），由"总分+门槛+红旗+证据充分度"共同决定，必须带编号 Why 列表；与 V2 的 GO/VALIDATE_FIRST/NO_GO 一一对应（`v3-decision.md`）。
4. **MVP Blueprint**：RECOMMENDED 或（POTENTIAL 且 ≥65 分）时生成；9 字段（Product / Target User / Core Problem / Core Value / Must Have≤3 / Nice to Have / Do Not Build / Build Difficulty / Recommended Stack）；只回答"一个人最快怎么验证这个想法"（`v3-mvp.md`）。
5. **Action Plan 行动计划**：按机会类型动态生成（企业工具/个人工具/AI Agent/本地服务/数字产品），每步 5 要素（目标/做什么/成功标准/失败转向），结尾必有"今天做什么"（`v3-action-plan.md`）。

### 第四套代码（防混淆）

V3 新增 Decision Code（RECOMMENDED/POTENTIAL/NOT_RECOMMENDED），与证据等级 A/B/C、Opportunity State、Pipeline Stage 正交，禁止共用一套字母表达多个含义（`v3-overview.md` §5）。

### V3 与 V2 的关系

- V2 五阶段流水线、三种模式、铁律、停止机制、第一笔钱清单**全部不变**，继续作为 V3 的分析引擎。
- V3 只新增决策层与统一口径：V2 的五张卡照常产出，V3 把它们压缩成一张结论先行的 `templates/v3-report.md`。
- V2 的 GO/VALIDATE_FIRST/NO_GO 与 V3 的 RECOMMENDED/POTENTIAL/NOT_RECOMMENDED 一一对应，最终报告统一用 V3 代码。
## 铁律（必须遵守）

1. **Search First（三类搜索）**：只要具备搜索/浏览器能力，必须优先实时搜索。按三类分别验证（详见 `references/market-research.md` §三类搜索）：
   - **Problem Search**：证明真实用户是否遇到这个问题。
   - **Solution Search**：证明用户现在如何解决（不用你的方案时）。
   - **Payment Search**：证明这个问题附近是否已有真实付费行为。
   三者证据齐备才构成商业验证基础；**只有 Problem Evidence 没有 Payment Evidence 时，不得判断为强商业机会。**
2. **禁止假装搜索**：若确实没有搜索能力，必须明确声明"【当前无法进行实时市场验证，以下属于假设分析】"，所有结论标记为假设，不伪装成已核实。
3. **不虚构**：不虚构用户、价格、成交、数据。无法证实的内容只能作为"假设/待验证"，绝不写成"事实/已发现"。
4. **Evidence Chain（证据链）**：每个重要市场结论必须走 `原始证据 → 观察 → 推断 → 假设 → 验证` 链条（详见 `references/evidence-chain.md`）。禁止"原始证据 → 直接得出强商业结论"。每份证据标注 Evidence / Source / Evidence Type / Confidence / Proves / Does NOT prove。证据不足时明确写【证据不足】，不得为凑完整报告而补模型猜测。
5. **有停手权（Stop Conditions）**：证据不足、无重复需求、无付费行为、AI 无优势、竞争壁垒过高、个人无法低成本完成、用户无法触达目标客户等（完整清单见 `references/payment-validation.md` §停止机制）时，直接输出【不建议继续】并说明停止原因与重启条件，禁止强行制造机会。
6. **避免研究上瘾**：当证据已足够支持一个低成本验证时，停止继续研究，输出【研究阶段完成】，进入 Execution Mode。研究不是终点，验证才是终点。

## 三种工作模式

| 模式 | 何时进入 | 目标 | 出口 |
|---|---|---|---|
| **Quick Mode** | 用户随手抛出一个问题/现象（默认入口） | 快速判断"值不值得继续研究"，不写长报告 | `templates/quick-scan.md` |
| **Research Mode** | 用户显式要求深挖/市场研究/找竞争/分析评论区/全面验证 | 完整 Market Scan，跑通全流程 | `templates/market-report.md` |
| **Execution Mode** | 用户说"我准备做/想试/拿第一单/开始执行/这个可以做" | 停止研究，直接推进真实用户与第一笔钱 | 执行清单见 `references/payment-validation.md` §第一笔钱 |

路由逻辑：
- 默认对"一个问题/一个现象"先走 **Quick Mode**；用户未要求深挖时不自动升级成长报告。
- 出现"深挖 / 市场研究 / 找竞争 / 找类似需求 / 分析评论区 / 全面验证"等明确意图 → **Research Mode**。
- 出现"我准备做 / 我想试一下 / 帮我拿第一单 / 开始执行 / 这个可以做" → **Execution Mode**（不再继续研究）。
- 无方向长期找机会 → 30 天侦察或 Market Scan（Research Mode）。
- 出现"打个分 / 值不值得做 / 帮我决策 / 机会评分 / 第一版做什么 / MVP / 下一步做什么"等 V3 决策意图 → **V3 决策层**（Evidence → Score → Decision → MVP → Action，见 `references/v3-overview.md`）。

## 模式路由（细粒度）

| 用户意图 | 触发词（示例） | 工作模式 | 出口 |
|---|---|---|---|
| 随手抛一个问题 | "学校打印店经常有人让老板帮忙改 PDF，有没有机会？" | Quick | `templates/quick-scan.md` |
| 找市场 | "帮我找市场" "找赚钱机会" "有什么需求" | Research / 30天 | `templates/market-report.md` |
| 分析视频/内容 | "分析这个视频" "这个内容能赚钱吗" | Research（Video Reverse） | `references/market-research.md` §视频反向市场分析 |
| 分析评论区 | "分析这个评论区" "看看这些评论" | Research（Comment Mining） | `references/market-research.md` §评论区需求挖掘 |
| 报一个具体问题 | "我发现一个问题……" "XX 很麻烦" | Quick → 需要时 Research | `templates/problem-card.md` |
| 判断 AI 可行性 | "这个问题能不能用 AI" "能不能自动化" | Quick/Research | `references/ai-solution-patterns.md` |
| 判断商业价值 | "这个能不能赚钱" "有没有市场" | Research（Payment） | `references/payment-validation.md` |
| 要第一单 | "帮我拿第一单" "怎么收费" "找谁卖" "我准备做" | **Execution** | `references/payment-validation.md` §第一笔钱 |
| 深挖 | "继续深挖" "再深入" | Research（Deep） | `references/market-research.md` §Deep Research |
| 找类似需求 | "寻找类似需求" "还有谁需要" | Research（Demand Expansion） | `references/problem-framework.md` §三池维护 |
| 找竞争 | "寻找竞争对手" "有没有人做" | Research（Competitor） | `references/market-research.md` §竞争与付费分析 |
| 方案太复杂 | "这个方案太复杂" "有没有更简单的" | 自动降级解决方案 | `references/ai-solution-patterns.md` §降级规则 |
| 无明确项目，想长期找 | "我想做副业但没方向" | 30 天市场侦察 | `references/market-research.md` §30 天侦察模式 |
| 验证需求真假/强度（v2.0） | "这个需求是真的吗""用户真愿意要吗""需求强不强" | V2：VALIDATE | `references/demand-validation.md` |
| 评估项目值不值得做（v3.0） | "评估一下这个项目""值不值得做""可行性分析""打个分""机会评分" | **V3 决策层**：SCORING→DECISION（内部复用 EVALUATE） | `templates/v3-report.md`、`references/v3-scoring.md` |
| 机会转成项目/MVP（v2.0） | "帮我做成产品""设计 MVP""第一版做什么""技术怎么选" | V2：BLUEPRINT | `references/project-blueprint.md` |
| 商业模式/定价/获客（v2.0） | "怎么收费/定价""商业模式怎么设计""怎么找客户""第一批用户哪来""GTM" | V2：MONETIZE | `references/monetization-gtm.md` |
| 完整机会报告（v3.0） | "从头到尾分析一遍""出一份机会报告/Opportunity Report""发现→验证→评估→商业化" | V3：全流程（内部复用 V2 五阶段） | `templates/v3-report.md` |
| 机会决策（v3.0） | "帮我决策""值不值得做""这个想法能做吗" | V3：DECISION | `references/v3-decision.md` |
| MVP 与下一步行动（v3.0） | "第一版做什么""MVP 怎么设计""下一步做什么""今天做什么" | V3：MVP→ACTION | `templates/v3-mvp-card.md`、`templates/v3-action-plan-card.md` |

若输入同时命中多模式（例如"这个视频能赚钱吗"），按链式推进：Reverse Engineering → Payment Validation → 需要时到 AI Solution Design，不要在中间停。
若用户要求完整判断"值不值得做 + 怎么做 + 怎么赚钱"，按 V2 五阶段流水线 FIND→VALIDATE→EVALUATE→BLUEPRINT→MONETIZE 顺序推进（允许从指定阶段切入，但须先补齐该阶段输入契约所缺字段，见 `references/pipeline-and-runtime.md`）。
若用户只要求"打个分 / 值不值得做 / 下一步做什么"这类决策，走 V3 决策层九步主流程（`references/v3-overview.md` §1），V2 五阶段照常复用为分析引擎。

## 标准工作流（v1.1 九步 = V2 流水线 FIND 阶段的内部细化；v2.0 在其后衔接四阶段）

> 关系：下列第 1-9 步完成"发现/初步验证"，对应 V2 的 **FIND**；完成后按第 10 步顺序进入 VALIDATE → EVALUATE → BLUEPRINT → MONETIZE。用户也可直接从某一 V2 阶段切入（需满足该阶段输入契约）。

### 1. 侦察（三类搜索）
- **Problem Search**：搜抱怨、"有没有工具""怎么批量""太麻烦""每天都要""有人能帮我吗""求推荐""怎么解决"、重复劳动、时间浪费、人工成本、错误、效率问题。
- **Solution Search**：搜软件/SaaS/服务商/外包/Freelancer/Agency/人工服务/Excel脚本自动化/免费方案/替代方案。必须回答"用户现在不用我的方案时，是怎么解决的？"
- **Payment Search**：搜 pricing/price/service/freelancer/outsourcing/quote/cost/agency/paid service/marketplace/服务报价/SaaS 价格。必须优先找"市场上有没有人为类似结果付钱"。
- 现实观察：学校、宿舍、公司/实习、商店、小微企业、个体商户、朋友/同学、日常办事流程、重复劳动等。支持 `观察 → 记录 → 搜索 → 对比 → 验证`。

### 2. 记录为 Problem Card + Evidence Card
每个候选问题填 Problem Card（`templates/problem-card.md`），每条重要证据填 Evidence Card（`templates/evidence-card.md`）。

### 3. Evidence Chain 分级
把每条证据放上链条 `原始证据 → 观察 → 推断 → 假设 → 验证`，标注证据属性与证据等级（详见 `references/evidence-chain.md`）。等级判定：A 已验证需求 / B 潜在需求 / C 假设需求。凡无来源的只能到 C。

### 4. 评分（绑定证据）
对值得继续的问题按 8 维评分，**每个分数必须给出：分数 + 评分理由 + 对应证据 + 当前不确定性**（详见 `references/problem-framework.md` §评分绑定证据）。尤其强化 Payment 评分，有明确分档。**禁止仅凭主观感觉打分，禁止只看总分下结论。** 必须回答：为什么值得继续？最大不确定性？缺什么证据？下一步最应该验证什么？

### 5. 分析竞争与付费
每个值得研究的问题检查：是否已有工具/SaaS/人工服务/免费方案、用户为什么不用、当前价格、竞争者优势、最大缺点、个人是否还有切入空间。分析"用户真正购买的是什么"（结果/时间/效率/成本降低/任务完成/信息/质量，不是"买 AI"）。无付费证据必须明确指出。

### 6. 生成解决方案（必须先完成问题分析）
按优先级：L1 人工+AI → L2 半自动化 → L3 自动化 Workflow → L4 小工具 → L5 SaaS/产品。原则：**先卖结果，再产品化**。没有真实用户前，禁止优先开发复杂 SaaS/Agent。一个问题如果"一个人 + AI + 简单工具"就能完成第一次交付，就不要默认建议开发完整产品。若不需要开发，明确写【当前不需要开发】。可落地方案逐项回答（见 `references/ai-solution-patterns.md` §可落地方案清单）。

### 7. Opportunity 状态更新
为每个值得跟踪的机会建立唯一 Opportunity ID（如 MS-001），明确当前状态与当前瓶颈（详见 `references/opportunity-state-machine.md`）。只推进当前瓶颈，不重复无意义搜索。

### 8. MVP 与第一笔钱
- MVP 必须最小，明确【第一版做什么】【第一版不做什么】【验证什么】【什么结果出现后继续】【什么结果出现后放弃】。优先验证"是否有人愿意为结果付钱"。
- 第一笔钱：围绕当前 Opportunity 执行"谁可能买 → 在哪里找到 → 给他什么结果 → 怎么展示 → 多少钱 → 怎么交付 → 怎么收费 → 如何获得反馈"。允许 10/30/50/100 元小额验证。第一笔钱的意义是验证 `真实问题 → 真实解决方案 → 真实支付`。

### 9. 输出
Quick Mode → Quick Scan；Research Mode → Market Scan（`templates/market-report.md`）；Execution Mode → 执行清单 + 今天做什么。

### 10. V2 衔接：Validate → Evaluate → Blueprint → Monetize（v2.0）
FIND 得到值得跟踪的机会后，按序推进（每阶段产出对应卡片，方法见各自 reference）：
1. **VALIDATE 需求验证**：填 `templates/demand-validation-card.md`——痛点、三层用户、需求强度 6 信号、替代成本、付费理由链；伪/弱需求在此熔断。
2. **EVALUATE 项目评估**：填 `templates/project-evaluation-card.md`——7 维加权打分、列出可复算计算式、红旗检查，给出 🟢/🟡/🔴 三档结论；🔴 在此熔断。
3. **BLUEPRINT 机会转项目**：填 `templates/project-blueprint-card.md`——产品 Level、核心用户、MoSCoW、MVP 五项、技术方向、最小验证实验、差异化落地。
4. **MONETIZE 商业化获客**：填 `templates/monetization-gtm-card.md`——付费方/ICP、Offer、商业模式、可解释定价、首批 10 客户、主渠道、GTM、无产品验证、第一笔钱计划。
5. **REPORT**：汇总为 `templates/opportunity-report.md`（结论先行），一屏给"是否值得做 + 今天第一步"。
阶段熔断、回退、断点续跑、失败降级见 `references/pipeline-and-runtime.md`。

## 输出与 UI 规范（v2.0.0，报告即 UI）

所有阶段卡与报告的视觉渲染统一遵守 `references/ui-rendering-spec.md`（Design System：结论带 Banner、阶段进度条、10 格分数条、行动按钮、Loading/Empty/Error/Success 四种状态、移动端窄屏规则、长报告目录与小结）。核心要点（完整版见 `references/pipeline-and-runtime.md` §4 与 `references/ui-rendering-spec.md`）：
- **结论先行**：顶部结论带（信号灯 + 综合分 + Opportunity ID + Pipeline/State），其次关键判断、评分、证据、行动建议；让用户 10 秒看到结论与下一步。
- **评分可解释**：统一 10 格分数条 `████████░░ 8/10`；综合分必须附可手工复算的加权式；禁止"市场很大""前景广阔"等无证据结论。
- **双语不拥挤**：标题/固定标签"中文（English）"，正文中文为主、关键术语括注英文，不逐句翻译；三档结论固定双语（GO / VALIDATE FIRST / NO-GO）。
- **桌面与移动端**：桌面用对比表，窄屏把宽表改为纵向"字段：内容"键值列表，长表拆小表，保证手机上不需左右滑动。
- **代码/数据结构区**：Schema、契约、计算式一律用标注语言的围栏代码块（yaml/json/text），字段名英文、注释中文、缩进规范。
- **运行时健壮性**：所有外部搜索/网络/子 Agent 调用设超时、瞬时错误有限重试（指数退避）、失败按"换来源→用用户材料→标【证据不足】"降级并记录，确定性错误不重试；详见 `references/pipeline-and-runtime.md` §3。

## Evidence Chain 机制（P0）

每个重要市场结论必须走五段链条：

```
原始证据 → 观察 Observation → 推断 Inference → 假设 Hypothesis → 验证 Validation
```

- **禁止**：原始证据 → 直接得出强商业结论。
- 每条证据标注：Evidence（原文）、Source（来源）、Evidence Type（类型）、Confidence（置信度）、What this evidence proves（证明了什么）、What this evidence does NOT prove（不能证明什么）。
- 证据不足写【证据不足】，不补模型猜测。
- 完整定义、证据类型、置信度口径与示例见 `references/evidence-chain.md`。

## 三类搜索（P0）

```
Problem Evidence（有人遇到这个问题？）
+ Solution Evidence（他们现在怎么解决？）
+ Payment Evidence（有没有人为类似结果付钱？）
= 商业验证基础
```

只有 Problem Evidence、没有 Payment Evidence 时，最多判为"潜在机会（B）"，不得判为强商业机会。搜索关键词族与纪律见 `references/market-research.md` §三类搜索。

## Opportunity 状态机（P1）

每个重要机会有唯一 ID（MS-###），沿状态推进：

```
HYPOTHESIS（假设）→ DEMAND_CONFIRMED（已有需求证据）→ MARKET_CONFIRMED（已有市场/付费证据）
→ PAYMENT_VALIDATION（已进行付费验证）→ CUSTOMER_FOUND（已找到真实用户）
→ FIRST_PAYMENT（第一笔钱）→ REPEATED_DELIVERY（已重复交付）→ STANDARDIZED（已标准化）
→ AUTOMATED（已自动化）→ PRODUCTIZED（已产品化）
```

**状态一律用完整英文状态名**（如 DEMAND_CONFIRMED、FIRST_PAYMENT），不用字母代码，避免与**证据等级 A/B/C**（A=已验证需求 / B=潜在需求 / C=假设需求，保持不变）混淆。**FIRST_PAYMENT 必须实际收到真实付款**，"愿意付钱/愿意尝试/报价意愿"只是验证信号，最多推进到 CUSTOMER_FOUND。每次继续研究同一机会：读取之前的证据 → 不重复无意义搜索 → 明确当前状态 → 明确缺失的下一步证据 → 只推进当前瓶颈。完整规则见 `references/opportunity-state-machine.md`。

## 核心决策树

```
真实问题？
↓
有重复发生？
↓
足够痛？
↓
用户主动寻找解决方案？
↓
市场已有类似解决方案？
↓
有人为类似结果付费？
↓
AI 能明显降低成本/时间/技能门槛？
↓
个人可以低成本交付？
↓
找到真实用户？
↓
第一笔钱？
↓
重复交付？
↓
标准化？
↓
自动化？
↓
产品化？
```

任何关键节点为 NO：不硬造机会，回到对应验证环节；或按"停止机制"输出【不建议继续】。

## 快速验证模式

- **7 天验证**：Day1 确认问题与证据 → Day2 研究现有方案 → Day3 制作最小样品 → Day4 寻找潜在用户 → Day5 低成本测试交付 → Day6 收集反馈 → Day7 尝试收费/判断放弃。不适合 7 天的项目必须调整，不得机械套用。
- **30 天市场侦察**（无明确项目时）：W1 每天发现 3-5 个问题不开发 → W2 筛选 5 个 → W3 研究证据/竞争/价格/付费 → W4 选 1-2 个最简单问题用人工+AI 验证。目标不是完美项目，而是第一个真实结果。

## 三池维护（长期运行）

- **Result Pool**：AI 当前能帮人完成什么结果。
- **Demand Pool**：谁需要什么结果。
- **Payment Pool**：谁已经在为类似结果付钱。
优先研究"问题 + 已存在解决方案 + 已存在付费行为"三者同时成立的机会。

## 停止研究机制

出现以下任一情况，主动建议停止并输出【不建议继续】：
- 没有真实问题证据。
- 只有单个偶然案例。
- 没有重复需求。
- 没有任何解决方案市场。
- 没有付费行为。
- 用户已有成熟且满意的解决方案。
- AI 无法明显降低成本/时间/技能门槛。
- 竞争强度远超个人能力。
- MVP 无法快速验证。
- 必须投入大量资金/团队/开发周期。
- 用户本人无法触达目标客户。

停止时必须说明：1) 为什么停止；2) 哪个证据导致停止；3) 未来出现什么新证据可以重新启动。完整版见 `references/payment-validation.md` §停止机制。

## 避免研究上瘾

当证据已足够支持一个低成本验证（有真实问题 + 有重复需求 + 有类似服务收费 + AI 有明显杠杆 + 用户可触达 + 可低成本做 MVP）时：
- 停止继续搜索。
- 输出【研究阶段完成】。
- 下一步是【开始真实用户验证】，不是继续找新机会。

## 日常观察训练

把"看内容的人"训练成"观察需求的人"：
"这个好麻烦"→ 这是问题吗？／"有没有工具"→ 存在需求吗？／"多少钱"→ 存在付费信号吗？／"每天都要做"→ 存在重复劳动吗？／"我不会"→ 存在技能门槛吗？／"这个软件太复杂"→ 存在简化机会吗？

## 参考文件（按需读取）

- `references/problem-framework.md` — Problem Card 字段、问题十大分类、证据等级、**证据绑定评分（含 Payment 分档）**、三池维护、商业嗅觉训练。
- `references/market-research.md` — **三类搜索（Problem/Solution/Payment）**、侦察来源、视频反向分析、评论区挖掘、竞争与付费、7 天/30 天模式、Deep Research。
- `references/payment-validation.md` — 付费信号、**付费评分分档**、**第一笔钱执行清单**、验证指标、**停止机制（含重启条件）**。
- `references/ai-solution-patterns.md` — Level 1-5 方案、可落地方案清单、技术栈要求、MVP 原则、降级规则、Sell Result First。
- `references/evidence-chain.md` — **证据链五段式、证据类型、置信度口径、防跳级规则（P0 新增）**。
- `references/opportunity-state-machine.md` — **Opportunity ID、交付状态机 HYPOTHESIS→…→PRODUCTIZED、瓶颈推进与跨会话续研规则**。
- `references/demand-validation.md` — **【v2.0 新增】需求验证：需求强度 6 信号、三层用户、替代成本、付费理由链 JTBD、需求证据可信度、需求结论三选一（VALIDATE）**。
- `references/project-evaluation.md` — **【v2.0 新增】项目评估：7 维加权、综合机会评分 0-100（可复算）、三档结论 GO/VALIDATE FIRST/NO-GO、竞争格局与差异化、AI 可实现度、Solo Fit、7 条致命红旗（EVALUATE）**。
- `references/project-blueprint.md` — **【v2.0 新增】机会转项目：产品 Level、核心用户、MoSCoW、MVP 五项、技术方向、最小验证实验、差异化落地（BLUEPRINT，复用 Level 1-5）**。
- `references/monetization-gtm.md` — **【v2.0 新增】商业化与获客：付费方/ICP、Offer 阶梯、商业模式库、可解释定价、首批 10 客户、渠道矩阵、GTM 三阶段、无产品验证、MonetizationInput/Plan 模块契约（MONETIZE，可独立）**。
- `references/pipeline-and-runtime.md` — **【v2.0 新增】五阶段流水线编排、三套代码区分、熔断/回退/断点续跑、外部调用超时·重试·失败降级、输出信息层级/双语/桌面移动端/代码区规范、交付前验收清单**。
- `references/ui-rendering-spec.md` — **【v2.0.0 新增】输出渲染与视觉规范（Design System）：结论带 Banner、阶段进度条、分数条、行动按钮、Loading/Empty/Error/Success 四状态、移动端优先、长报告阅读体验、双语、代码区、输出自检清单**。

- `references/v3-overview.md` — **【v3.0 新增】V3 决策层总览：9 步主流程、V2→V3 映射、V3Input/V3Output 契约、四套代码正交、熔断降级、验收清单**。
- `references/v3-evidence.md` — **【v3.0 新增】市场证据层：Evidence/Inference/Unknown 三态、证据充分度 Sufficient/Partial/Insufficient、Unknown 计分、不编造铁律**。
- `references/v3-scoring.md` — **【v3.0 新增】机会评分：7 维 0-100 加权（需求/痛点/竞争切入空间/变现/开发/获客/AI 优势）、子信号、可复算公式、切入空间四问、致命红旗**。
- `references/v3-decision.md` — **【v3.0 新增】机会决策：RECOMMENDED/POTENTIAL/NOT_RECOMMENDED 三档判定、强制 Why、与 V2 Verdict 映射、证据不足处理、各档下一步承诺**。
- `references/v3-mvp.md` — **【v3.0 新增】MVP Blueprint：9 字段输出、触发条件、单人最快验证铁律、最小验证实验（复用 BLUEPRINT）**。
- `references/v3-action-plan.md` — **【v3.0 新增】行动计划：5 种机会类型判定、动态步骤模板（每步 5 要素）、Decision 联动、今天做什么、第一笔钱路径**。

## 模板（直接填充）

- `templates/problem-card.md` — 问题卡片（含证据链字段）。
- `templates/evidence-card.md` — **单条证据卡片（v1.1 新增）**。
- `templates/opportunity-card.md` — 机会卡片（含 Opportunity ID、状态、证据绑定评分）。
- `templates/quick-scan.md` — **Quick Mode 快速判断（v1.1 新增）**。
- `templates/market-report.md` — Market Scan 完整报告（FIND 阶段，含三类搜索证据与状态）。
- `templates/demand-validation-card.md` — **【v2.0 新增】需求验证卡（VALIDATE）**。
- `templates/project-evaluation-card.md` — **【v2.0 新增】项目评估卡（EVALUATE，含评分表/计算式/红旗）**。
- `templates/project-blueprint-card.md` — **【v2.0 新增】机会转项目卡（BLUEPRINT）**。
- `templates/monetization-gtm-card.md` — **【v2.0 新增】商业化与获客卡（MONETIZE，含 MonetizationPlan 契约）**。
- `templates/opportunity-report.md` — **【v2.0 新增】最终机会报告（五阶段汇总，结论先行）**。

- `templates/v3-evidence-board.md` — **【v3.0 新增】证据看板（三态 + 充分度 + 缺失清单）**。
- `templates/v3-score-card.md` — **【v3.0 新增】机会评分卡（7 维 + 计算式 + 百分条 + 切入空间四问 + 红旗）**。
- `templates/v3-decision-card.md` — **【v3.0 新增】机会决策卡（结论带 + Why + 下一步承诺）**。
- `templates/v3-mvp-card.md` — **【v3.0 新增】MVP 方案卡（9 字段 + MVP 五项 + 最小验证实验）**。
- `templates/v3-action-plan-card.md` — **【v3.0 新增】行动计划卡（类型化步骤 + 今天做什么 + 第一笔钱）**。
- `templates/v3-report.md` — **【v3.0 新增】V3 最终机会决策报告（一屏：Score/Decision/Evidence/Pain/Competition/MVP/Action，结论先行）**。

## 示例（演示流程，数据为示意）

- `examples/video-analysis.md` — 视频反向市场分析（含证据链）。
- `examples/comment-analysis.md` — 评论区需求挖掘（含三类搜索）。
- `examples/real-world-problem.md` — **完整 v1.1 运行示例：Quick → Research（三类搜索+证据链）→ Execution（第一笔钱）+ 状态机推进**。
- `examples/full-pipeline-v2.md` — **【v2.0 新增】完整 V2 流水线示例：FIND→VALIDATE→EVALUATE（含可复算评分与"74 分为何仍是🟡"）→BLUEPRINT→MONETIZE（定价/获客/第一批客户）→最终结论**。

- `examples/v3-decision-run.md` — **【v3.0 新增】完整 V3 决策链示例：Evidence 看板 → 7 维评分（可复算）→ Decision → MVP 9 字段 → 动态 Action Plan**。
- `examples/v3-crowded-market.md` — **【v3.0 新增】红海市场示例：竞争激烈但切入空间存在时如何评分与决策（禁止"竞争高=不值得做"）**。

## 用户使用说明

`USER_GUIDE.md` 是面向最终用户（非 Agent）的安装与使用说明：安装方式、版本验证、触发词、三种模式、FAQ。当用户询问"怎么安装 / 怎么用 / 怎么验证版本 / 有哪些触发词"时，引导其阅读 `USER_GUIDE.md`。

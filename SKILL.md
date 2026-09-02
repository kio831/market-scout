---
name: market-scout
description: 市场侦察与商业验证工作流（Market Scout，v1.1）。当用户想做 AI 赚钱副业、找市场需求、发现痛点、分析某个视频/评论区/帖子里隐含的商机、判断"某个问题/工具能不能用 AI 解决"、"这件事能不能赚钱"、寻找竞争对手、做市场调研、拿第一单/第一笔钱、把 AI 能力变现、验证创业点子，或提到"帮我找市场""分析这个视频""分析这个评论区""我发现一个问题""这个能不能用 AI""这个能不能赚钱""帮我拿第一单""继续深挖""寻找类似需求""寻找竞争对手"时使用。核心原则是 Search First（优先实时搜索真实市场信息而非依赖模型记忆），绝不虚构用户、价格与数据；v1.1 增加 Evidence Chain 证据链机制（原始证据→观察→推断→假设→验证，事实/推断/假设严格分离）、Problem/Solution/Payment 三类搜索、Quick/Research/Execution 三种工作模式与 Opportunity 状态机（HYPOTHESIS→DEMAND_CONFIRMED→MARKET_CONFIRMED→PAYMENT_VALIDATION→CUSTOMER_FOUND→FIRST_PAYMENT→REPEATED_DELIVERY→STANDARDIZED→AUTOMATED→PRODUCTIZED），输出含证据绑定评分、MVP 与第一笔钱路径的 Market Scan 报告。证据等级 A/B/C 与机会状态名相互独立，不共用字母代码。
---

# Market Scout (v1.1)

市场侦察 + 需求发现 + 痛点分析 + 商业验证 + AI 解决方案设计。
不是"AI 赚钱项目生成器"，而是把真实问题跑成第一笔收入的流程工具。

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

若输入同时命中多模式（例如"这个视频能赚钱吗"），按链式推进：Reverse Engineering → Payment Validation → 需要时到 AI Solution Design，不要在中间停。

## 标准工作流（v1.1）

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
- `references/opportunity-state-machine.md` — **Opportunity ID、状态机 HYPOTHESIS→DEMAND_CONFIRMED→MARKET_CONFIRMED→PAYMENT_VALIDATION→CUSTOMER_FOUND→FIRST_PAYMENT→REPEATED_DELIVERY→STANDARDIZED→AUTOMATED→PRODUCTIZED、瓶颈推进与跨会话续研规则（P1 新增）**。

## 模板（直接填充）

- `templates/problem-card.md` — 问题卡片（含证据链字段）。
- `templates/evidence-card.md` — **单条证据卡片（v1.1 新增）**。
- `templates/opportunity-card.md` — 机会卡片（含 Opportunity ID、状态、证据绑定评分）。
- `templates/quick-scan.md` — **Quick Mode 快速判断（v1.1 新增）**。
- `templates/market-report.md` — Market Scan 完整报告（含三类搜索证据与状态）。

## 示例（演示流程，数据为示意）

- `examples/video-analysis.md` — 视频反向市场分析（含证据链）。
- `examples/comment-analysis.md` — 评论区需求挖掘（含三类搜索）。
- `examples/real-world-problem.md` — **完整 v1.1 运行示例：Quick → Research（三类搜索+证据链）→ Execution（第一笔钱）+ 状态机推进**。

## 用户使用说明

`USER_GUIDE.md` 是面向最终用户（非 Agent）的安装与使用说明：安装方式、版本验证、触发词、三种模式、FAQ。当用户询问"怎么安装 / 怎么用 / 怎么验证版本 / 有哪些触发词"时，引导其阅读 `USER_GUIDE.md`。

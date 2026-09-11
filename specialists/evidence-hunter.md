---
name: market-scout-evidence-hunter
description: Market Scout V5 专家子技能——Evidence Hunter。对定义好的问题执行三类搜索（Problem/Solution/Payment），生成证据链、证据看板与六维证据覆盖度，严格区分事实/推断/未知，绝不虚构。当用户说“帮我找这个问题的真实需求”“找证据”“市场上有谁在解决”“谁在为这个付费”或单独安装后直接触发时使用。完整分析请用主技能 market-scout。
---

# Evidence Hunter（证据猎人）

> 职责：Problem → Search → Evidence Chain → Evidence Board + Coverage。V5 中**唯一被授权搜索**的 Specialist。
> 继承 V4：Search First 铁律、三类搜索、evidence-chain.md、v3-evidence-coverage.md、v3-evidence.md。

## 输入契约

| 来源 | 字段 | 说明 |
|---|---|---|
| 独立调用 | problem | 问题定义（必须） |
| 独立调用 | 用户提供的研究资料 | 可选：已有搜索结果/文章/数据 |
| 被 Main 调用 | Context.problem + Context.evidence | 已有证据只做缺口搜索，不重复搜索 |

输入不足：无 problem → MISSING_INPUT（由 Problem Scout 补位）。无搜索能力 → 按第 4 节降级，明确声明假设分析。

## 输出契约（写回 Context.evidence）

    evidence:
      chain: 每条证据走五段链（原始证据→观察→推断→假设→验证）
      board: v3-evidence-board.md 三态看板（Evidence/Inference/Unknown + 充分度）
      coverage: 六维各 0-100（problem/solution/payment/competition/distribution/buildability）
      overall_coverage: 等权平均
      critical_gaps: 关键缺口（Payment/Demand 优先）
      search_capability: true/false（false 时全部结论标假设）
      sources: 去重后的来源清单

同时输出：
- State 推进：PROBLEM → EVIDENCE（搜索无结果也算达成，Coverage=0 并注原因）
- Evidence Insufficient 声明（当三类搜索不足以支撑判断时，显式输出，不补模型猜测）

## 执行方法

1. **Search First**：只要具备搜索/浏览器能力，必须先实时搜索，三类齐备：
   - Problem Search：搜抱怨、“有没有工具”“怎么批量”“太麻烦”“每天都要”“有人能帮我吗”“求推荐”、重复劳动、时间浪费、人工成本、错误、效率问题。
   - Solution Search：搜软件/SaaS/服务商/外包/Freelancer/Agency/人工服务/免费方案/替代方案；回答“用户现在不用我的方案时，是怎么解决的”。
   - Payment Search：搜 pricing/price/service/freelancer/quote/cost/paid service/服务报价/SaaS 价格；回答“市场上有没有人为类似结果付钱”。
   关键词族与来源纪律见 references/market-research.md 三类搜索。
2. **逐条证据卡**：每条重要证据按 evidence-card.md 填写六属性：Evidence（原文）/ Source / Evidence Type / Confidence / Proves / Does NOT prove；再入五段证据链。
3. **三态标注**：找到的公开信息= Evidence；基于证据的推导= Inference；无法确认= Unknown。只有 Problem Evidence 没有 Payment Evidence 时，最多判 B 级潜在机会，不得判强商业机会。
4. **覆盖度**：按 v3-evidence-coverage.md 六维打分（0-100），来源去重（同源转载不重复计分），标出 critical_gaps（Payment/Demand 为最高优先缺口）。
5. **缺口搜索（被 Main 调用时）**：若 Context.evidence 已有内容 → 只针对 critical_gaps 做定向搜索，**不重新搜索已覆盖维度**。

## 降级规则

- 无搜索能力：输出“【当前无法进行实时市场验证，以下属于假设分析】”，search_capability=false，coverage 记 0 分并注明原因；全部结论标假设（V4 铁律第 2 条）。
- 搜索无结果：输出 Evidence Insufficient + 缺失维度清单；不编造；把结果交给决策层，由 Score Ceiling 自动约束（最高 POTENTIAL）。
- 搜索失败（超时/网络）：按 pipeline-and-runtime.md 第 3 节——换来源 → 用用户材料 → 标【证据不足】，记录日志。

## 质量铁律

- **不虚构**：不虚构用户、价格、成交、数据；无法证实的内容只能标假设/待验证
- **不跳级**：禁止“原始证据 → 直接得出强商业结论”，必须走五段链
- **证据不足就明说**：不为了凑完整报告补模型猜测
- 证据冲突：保留双方并标记 TO VERIFY，不静默平均

## 独立调用示例

用户：“帮我找这个问题的真实需求——小商家不会开发票每次都找人帮忙。”
输出（摘要）：

    Problem Search:  找到 N 条“小商家/个体户开票麻烦、找人代开”的真实抱怨（附来源）
    Solution Search: 现有方案=代账公司/财务外包/手工 Excel，价格区间 X-Y（附来源）
    Payment Search:  代理记账服务有明确标价与成交（附来源），可确认付费行为存在
    critical_gaps:   payment 覆盖较高；distribution（目标用户聚集地）待补
    Evidence Insufficient: 无

## 被 Main 调度时的行为

- 读 Context.problem + Context.evidence；已有覆盖的维度禁止重搜（Evidence Reuse）。
- 完成后只写 evidence 字段并更新 state/history，交回 Main；证据冲突或 Evidence Insufficient 时随结果返回标注，不下决策。

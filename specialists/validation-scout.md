---
name: market-scout-validation-scout
description: Market Scout V5 专家子技能——Validation Scout。基于机会与评分设计最低成本验证（从最大未知开始、11 问验证计划、方法成本排序、禁止默认 MVP），并读取真实验证结果（Observed/Inference/Unknown 分级）为重新判断提供输入。当用户说“帮我验证”“怎么验证”“设计验证实验”“我验证了 N 个人，结果…”或单独安装后直接触发时使用。完整分析请用主技能 market-scout。
---

# Validation Scout（验证侦察员）

> 职责：Opportunity + Score → Key Assumptions → Validation Plan → Experiment → Result。V5 中**唯一负责设计验证实验**的 Specialist。
> 继承 V4：v4-validation.md 全章（11 问、从最大未知开始、Lowest-Cost 方法映射、Validate before Build、Success/Failure Criteria、Result 分级、R1-R5 重算）。
> 明确区分：**Evidence = 已经存在的外部证据；Validation = 主动验证关键假设**。两者不混用。

## 输入契约

| 来源 | 字段 | 说明 |
|---|---|---|
| 独立调用 | opportunity + score | 机会卡 + 评分（必须） |
| 独立调用 | 用户已做过的验证结果 | 可选：访谈/落地页/预售数据 |
| 被 Main 调用 | Context.opportunity + Context.score + Context.validation | 已有 validation 计划时续跑，不重复设计 |

输入不足：缺 score → MISSING_INPUT（由 Opportunity Score 补位）。用户要求“直接验证”但拒绝提供评分 → 允许按最小输入设计验证，但方法选择理由必须写清。

## 输出契约（写回 Context.validation）

    validation:
      plan:
        core_hypothesis: 要验证的核心假设（从最大 Unknown 取）
        method: UserInterview / LandingPage / PaidTest / PreSale / ManualDelivery / SmallPilot / MVP
        sample: 样本量
        duration: 时长
        cost: 成本
        success: 量化成功线（如 ≥2 人付款且费率 ≥10%）
        failure: 对称失败线（如 0 付款）
        decision_rule: 结果出现后怎么转向
        next_state: VALIDATED / REVISE
      experiment: {done: false, detail: ""}
      result: {sample_n, interested, trial, paid, revenue, observed[], inference[], unknown[]}

同时输出：
- State 推进：SCORED → VALIDATION
- 重算输入（供 Main 按 R1-R5 执行）：被验证维度的新 Coverage 与维度分

## 执行方法

1. **从最大未知开始**：读 V3.1 的 Unknowns / Critical Gaps / Coverage / Confidence / Hard Gates / Decision，锁定最影响决策的 Unknown（通常是付费意愿）；一次只验证一个核心假设。
2. **11 问验证计划**：验证什么 / 为什么 / 谁 / 怎么 / 在哪 / 样本 / 时长 / 成本 / 成功 / 失败 / 下一状态。
3. **最低成本方法**：成本时间排序——访谈 < 落地页 < 报价预售 ≈ 提前收款 < 人工试交付 < 小试点 < MVP；**禁止机械套用**，必须说明为什么该方法适合当前假设与人群触达渠道。
4. **Validate before Build（禁止默认 MVP）**：Payment / Problem 证据不足或关键 Unknown 未解 → 输出 Validation Experiment，不输出 Build MVP。
5. **Success / Failure Criteria**：量化且对称；无依据时阈值标 Unknown + 校准说明（No Fake Precision）。
6. **结果分级**：用户回填真实结果后，区分 Observed（实际发生）/ Inference（推断）/ Unknown（未能确认）；禁止“8 人感兴趣 = 市场已验证”。
7. **重算输入**：按 v4-validation.md R1-R5 准备新 Coverage 与新维度分，交回 Main 重新判断（Reality > Prediction）。

## 质量铁律

- 不默认 MVP：证据不足时验证优先
- 不制造虚假精度：阈值没有依据就标 Unknown 并校准
- 结果不越级：只有 Observed 才能当事实；Inference 必须标注
- 一次一个核心假设，禁止一锅烩验证

## 独立调用示例

用户：“这个项目怎么验证——AI 轻量开票工具，评分 86，distribution 覆盖低。”
输出（摘要）：

    core_hypothesis: 个体户愿意为“轻量自助开票”按年付费
    method: PreSale（在 3 个个体户社群发报价预售页）——成本最低且直接验证付费
    sample: 20 / duration: 14 天 / cost: 0-50 元
    success: ≥2 人付款且费率 ≥10% → 进入 MVP
    failure: 0 付款 → 修改 Offer/人群后重验一次，仍失败则 PARK
    decision_rule: 按 v4 R1-R5 回灌评分重判

## 被 Main 调度时的行为

- 读 Context.score + Context.opportunity；已有 validation.plan 且实验未完成 → 继续执行实验，不重复设计计划。
- 结果回填后只写 validation 字段并更新 state/history；重新判断（重算 Score/Decision）由 Main 按 R1-R5 完成。

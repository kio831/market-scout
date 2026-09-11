---
name: market-scout-problem-scout
description: Market Scout V5 专家子技能——Problem Scout。把观察信号定义成一个可研究的问题（目标用户、场景、问题分类、证据等级 A/B/C），并判断是否值得进入证据研究。当用户说“帮我把这个问题定义清楚”“这个问题真实吗”“这是什么类型的问题”或单独安装后直接触发时使用。完整分析请用主技能 market-scout。
---

# Problem Scout（问题侦察员）

> 职责：Observation → Problem Definition。产出 V4 的 Problem Card，明确“谁、在什么场景、遇到什么问题、有多痛”，并给出问题分类与初始证据等级。
> 继承 V4：templates/problem-card.md、references/problem-framework.md（问题十大分类、证据等级）。

## 输入契约

| 来源 | 字段 | 说明 |
|---|---|---|
| 独立调用 | observation | 谁/什么问题/频率/当前方案/付费信号（至少 who + problem） |
| 独立调用 | 用户补充材料 | 可选：评论、帖子、访谈记录 |
| 被 Main 调用 | Context.observation | 已有则直接读取；缺失返回 MISSING_INPUT（由 Idea Observer 补位） |

输入不足：只有一句话问题没有场景/人群 → 先向用户确认最小二问（谁遇到？什么场景？）；用户无法回答 → 按当前信息定义问题并全部标 C 级（假设），明确提示证据不足。

## 输出契约（写回 Context.problem）

    problem:
      card: Problem Card 填写结果（templates/problem-card.md）
      target_user: 目标用户（具体）
      scenario: 高频/高痛场景（具体）
      evidence_level: A（已验证需求）/ B（潜在需求）/ C（假设需求）
      category: 问题十大分类之一

同时输出：
- State 推进：OBSERVATION → PROBLEM
- 停手判定：无真实问题/单次偶发/用户已有满意方案 → 建议 PARK，不进入证据阶段

## 执行方法

1. **收敛问题**：把观察信号收敛成一句话问题陈述（谁 + 在什么场景 + 做什么事遇到什么阻碍）。
2. **填 Problem Card**：按 problem-framework.md 的卡字段逐项填；证据等级按现有信息判定：有真实用户反馈= B，只有猜测= C，已有多方验证= A。
3. **对照三池**：该问题是否与 Result Pool（AI 能交付的结果）/ Demand Pool（谁需要）/ Payment Pool（谁在付钱）中的记录相关，写入卡备注。
4. **首次停手检查**：无真实问题证据 / 只有单个偶然案例 / 用户已有成熟满意方案 → 直接输出【不建议继续】+ 原因 + 重启条件（V4 停止机制），本阶段即止。
5. **不搜索**：本阶段只用已有材料定义问题；证据搜集是 Evidence Hunter 的职责。

## 质量铁律

- 问题定义必须落实到具体场景，禁止“市场很大”“很多人需要”式空泛定义
- 证据等级必须如实：没有来源就是 C
- 单次偶发必须停止并说明，不硬造需求

## 独立调用示例

用户：“帮我把这个问题定义清楚——小商家不会开发票，每次都要找人帮忙。”
输出（摘要）：

    target_user: 个体户/小微商家（无专职财务）
    scenario: 客户要发票/对账/报价单时，手工处理或花钱找人
    evidence_level: B（用户自述真实场景，仍需外部验证）
    category: 重复劳动 + 专业门槛类问题
    停手检查: 暂无单次偶发或成熟方案迹象 → 建议进入 Evidence Hunter

## 被 Main 调度时的行为

- 读 Context.observation；若已存在 problem 且用户未提供新信息 → 不重跑（State Reuse）。
- 停手时把建议（PARK/KILL）写回 Context.decision 候选区，由 Main 决策门确认，不自行宣布最终决策。

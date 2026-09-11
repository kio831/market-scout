---
name: market-scout-idea-observer
description: Market Scout V5 专家子技能——Idea Observer。把一个想法/现象/素材拆成可研究的观察信号（谁、什么问题、重复频率、当前的解决办法、付费信号、AI 杠杆），判断它是真实观察还是空想。当用户说“帮我分析这个想法”“这个现象值得研究吗”“观察一下这个需求”或单独安装后直接触发时使用。完整分析请用主技能 market-scout。
---

# Idea Observer（想法观察员）

> 职责：Idea → Observation。把用户的一句话想法变成一组“可验证的观察信号”，不提前下结论。
> 继承 V4：日常观察训练、market-research.md 的视频反向分析/评论区挖掘。

## 输入契约

| 来源 | 字段 | 说明 |
|---|---|---|
| 独立调用 | idea.text | 用户的想法/现象/素材（必须） |
| 独立调用 | idea.source | 可选：来自哪里（原话/视频/评论区/资料链接） |
| 被 Main 调用 | Context.idea | 已写入的 idea 字段，直接读取，不重复询问 |

输入不足：只有素材没有想法时，先按“素材里的人在抱怨什么/在求什么”提取问题信号；素材也不足时，声明 OBSERVATION 无法完成，返回 MISSING_INPUT。

## 输出契约（写回 Context.observation）

    observation:
      who: 谁遇到这个问题（具体人群）
      problem: 问题是什么（一句话）
      frequency: 重复性信号（一次偶然还是反复出现）
      current_solution: 现在不用你的方案时怎么解决
      payment_signal: 有没有付费迹象（谁在为类似结果付钱）
      ai_leverage: AI 能否明显降低成本/时间/技能门槛
      hypothesis_flags: 空想/未观察项标记（如“这是我猜的”）

同时输出：
- State 推进：IDEA → OBSERVATION
- 建议下一步（给 Main 或用户）：通常为 Problem Scout

## 执行方法

1. **拆信号**：把想法拆成六问——“这个好麻烦”→ 问题？／“有没有工具”→ 需求？／“多少钱”→ 付费？／“每天都要做”→ 重复？／“我不会”→ 技能门槛？／“太复杂”→ 简化机会？（SKILL.md 日常观察训练）
2. **区分观察与空想**：凡是用户“听说/觉得/猜测”的，进 hypothesis_flags，不进事实字段。
3. **素材类输入**：视频/评论区按 market-research.md 反向分析：找出抱怨、求推荐、替代方案、价格讨论四类信号。
4. **标频率**：单次偶发 vs 反复出现，直接影响是否值得进入下一阶段；单次偶发必须标记（大概率在 Problem Scout 被停手）。
5. **不评分、不搜证据**：本阶段只观察；评分是 Opportunity Score 的事，搜索是 Evidence Hunter 的事。

## 质量铁律

- 不把猜测写成事实：无法确认的观察一律 hypothesis_flags
- 不提前下“这是好机会”的结论
- 不虚构用户（谁 = 具体人群，不写“很多人”这种无主语表述）

## 独立调用示例

用户：“帮我分析这个想法——学校打印店经常有人让老板帮忙改 PDF 格式。”
输出：

    observation:
      who: 大学打印店顾客（学生为主）与打印店老板
      problem: 改 PDF 格式/排版这类小任务要花钱找人或自己折腾
      frequency: “经常”（用户在多个场景观察到，但样本待补）
      current_solution: 付费找打印店老板处理 / 自己装软件折腾
      payment_signal: 有人为这个结果付钱（打印店收费）
      ai_leverage: 高——此类任务正是 AI 工具擅长的低技能重复劳动
      hypothesis_flags: [“样本来源待确认”, “付费金额未见”]

## 被 Main 调度时的行为

- 读 Context.idea；若已有 observation 且用户未给新信息 → 不重跑，直接返回已有结果（State Reuse）。
- 完成后只写 observation 字段并更新 state/history，然后交回 Main 决定下一步。

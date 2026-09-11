---
name: market-scout-opportunity-scout
description: Market Scout V5 专家子技能——Opportunity Scout。基于已有问题与证据完成需求验证（需求强度/目标用户/付费理由链）与竞争切入空间分析（四问），产出机会卡并判定当前瓶颈。当用户说“这个需求是真的吗”“有没有机会”“竞品怎么样”“切入空间在哪”“值不值得继续研究”或单独安装后直接触发时使用。完整分析请用主技能 market-scout。
---

# Opportunity Scout（机会侦察员）

> 职责：Problem + Evidence → Opportunity。把“已证实的问题 + 已搜集的证据”转成机会判断：需求真不真、强不强、为什么愿意付钱、竞品缺什么、我们切哪里。
> 继承 V4：demand-validation.md（需求强度 6 信号、三层用户、付费理由链）、v3-scoring.md（切入空间四问）、templates/opportunity-card.md。**尽可能复用已有证据，不重复研究。**

## 输入契约

| 来源 | 字段 | 说明 |
|---|---|---|
| 独立调用 | problem + evidence | 问题定义 + 证据链/覆盖度（必须） |
| 独立调用 | 用户补充访谈/竞品观察 | 可选 |
| 被 Main 调用 | Context.problem + Context.evidence | 直接读取；缺失返回 MISSING_INPUT |

输入不足：缺 evidence → MISSING_INPUT（由 Evidence Hunter 补位）。用户要求只基于现有材料分析 → 允许，但必须声明结论的证据等级与 Unknown。

## 输出契约（写回 Context.opportunity）

    opportunity:
      card: Opportunity Card 填写结果（templates/opportunity-card.md）
      state: HYPOTHESIS / DEMAND_CONFIRMED / MARKET_CONFIRMED …
      bottleneck: 当前唯一瓶颈（只推进瓶颈，不重复无意义搜索）
      demand_summary: 需求验证结论（真实需求已验证 / 需求存在但付费未验证 / 伪·弱需求）
      competition_gap: 切入空间四问结论（不是“竞争低=好”）

同时输出：
- State 推进：EVIDENCE → OPPORTUNITY
- 初判 Verdict（给 Main 决策门参考：GO / VALIDATE FIRST / NO-GO）

## 执行方法

1. **需求验证**（demand-validation.md）：三层用户（核心/扩展/非用户）、需求强度 6 信号合成 1-10、替代成本、付费理由链（JTBD 5 环）、证据可信度；结论三选一。
2. **竞争与切入空间（禁止简单化）**：竞争高 + 需求高 ≠ 坏机会。必须回答四问：
   - 用户有没有真实需求？
   - 竞品有没有真正解决问题？
   - 用户是否仍在抱怨？
   - 竞品有哪些缺陷/未覆盖细分市场？
   最终回答：**有没有切入空间？** 竞争维度分数=切入空间大小，不由竞争浓度单独决定。
3. **建机会卡**：唯一 Opportunity ID（MS-###），当前状态（真实世界交付状态机，见 opportunity-state-machine.md），当前瓶颈。
4. **三池对照**：问题 + 已有解决方案 + 已有付费行为三者的交集优先。
5. **不搜索**：本阶段不执行新搜索；需要更多证据时返回 MISSING_EVIDENCE + 缺口清单，由 Evidence Hunter 定向补。

## 质量铁律

- 需求结论必须三选一，禁止“应该还行”式模糊结论
- 竞争分析必须回答四问 + 切入空间，禁止“竞争低=高分”的错误逻辑
- 不虚构竞品/价格/用户；证据不足时标注 Unknown
- 已有证据足够时停止研究（避免研究上瘾），把结论交给评分

## 独立调用示例

用户：“机会分析——已有问题定义和证据：小商家开票麻烦，代账服务已有人付费。”
输出（摘要）：

    demand_summary: 真实需求已验证（核心用户=个体户，6 信号中 4 个命中，付费理由链完整）
    competition_gap: 传统代账贵且重，AI 可做轻量开票/对账细分；缺口=轻量自助+低价档
    state: DEMAND_CONFIRMED
    bottleneck: 付费意愿尚未用轻量方案验证

## 被 Main 调度时的行为

- 读 Context.opportunity：已有且用户未给新信息 → 不重跑（State Reuse）。
- 只写 opportunity 字段并更新 state/history；初判 Verdict 交给 Main 决策门，不自行宣布最终决策。

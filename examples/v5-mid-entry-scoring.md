# V5 中途进入示例：已有 Problem + Evidence → 直接评分（数据为示意）

> 演示 Mid-workflow Entry：用户自带资料（问题 + 研究）时，跳过 Idea/Observation/Evidence 重跑，从 Opportunity Scout 开始。
> 核心验证点：**不重复搜索已有证据**。

## 用户输入

“这是我的问题定义和已搜集的证据：问题=小微企业开发票麻烦；资料=5 条用户抱怨 + 2 份代账服务报价单 + 1 份行业文章。帮我从机会分析开始，直接评分。”

## 路由日志（Main）

    state_detected: EVIDENCE（用户自带 problem + evidence 材料）
    mode: MID-ENTRY（从 EVIDENCE 之后开始）
    dispatch: Opportunity Scout → Opportunity Score（跳过 Idea Observer / Problem Scout / Evidence Hunter）
    跳过原因记录: 用户已提供问题定义与原始证据，重复搜索违反 Evidence Reuse

## Opportunity Scout（EVIDENCE → OPPORTUNITY）

    demand_summary: 需求存在但付费未完全验证（抱怨真实；报价单证明代账市场存在付费，轻量档未知）
    competition_gap: 四问——有需求 / 代账解决但贵且重 / 用户抱怨仍在 / 缺口=轻量与按需付费档
    state: DEMAND_CONFIRMED
    bottleneck: 轻量档付费意愿未验证

## Opportunity Score（OPPORTUNITY → SCORED）

    dims: demand 82 / pain 85 / competition 65 / monetization 75 / buildability 90 / distribution 60 / ai 85
    total: 79（=82×0.15+85×0.15+65×0.15+75×0.20+90×0.15+60×0.10+85×0.10）
    confidence: Medium（52）| hard_gates: gate PASS / ceiling [] / red_flags []
    解释: 强项=痛点与开发可行性；弱项=轻量档获客渠道未验证

## Main 决策门（SCORED → DECISION）

    code: RECOMMENDED（总分 79 ≥ 75；demand 82 ≥ 70、pain 85 ≥ 60、monetization 75 ≥ 60；无硬门槛/红旗）
    verdict: VALIDATE（distribution 覆盖 60 临界，先做轻量档付费验证再 BUILD）
    why:
      1. 痛点明显且有真实抱怨来源
      2. 代账付费行为已确认，变现路径存在
      3. 轻量档存在竞争缺口
      4. 开发可行性高
      5. 验证成本低（小样本预售即可）

## 自检

- [x] 未重跑 IDEA / OBSERVATION / EVIDENCE
- [x] 证据被直接复用（机会与评分都引用用户资料，未重新搜索）
- [x] 评分可复算，决策有 Why
- [x] history 记录跳跃原因（mid-entry skip）

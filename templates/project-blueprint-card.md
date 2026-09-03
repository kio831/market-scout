# Project Blueprint Card 机会转项目卡模板（v2.0，流水线阶段 BLUEPRINT）

阶段：FIND 到 VALIDATE 到 EVALUATE 到 BLUEPRINT 到 MONETIZE。方法见 references/project-blueprint.md；Level 1-5、技术生产级要求、MVP 降级规则复用 references/ai-solution-patterns.md。进入条件：EVALUATE 为绿或验证后可转绿的黄；红不进入。默认从 L1 起步先卖结果再产品化。

# 机会转项目（Opportunity → Project）

FIND 已完成到 VALIDATE 已完成到 EVALUATE 已完成到 BLUEPRINT 进行中到 MONETIZE 待开始。

Opportunity ID：MS-### Pipeline Stage：BLUEPRINT 日期：YYYY-MM-DD。上游输入：核心用户需求强度 EVALUATE 结论 AI 可实现度差异化切入点。

项目一页纸 | Opportunity MS-### | 推荐形态 L1/L2。卖给谁到交付什么结果到第一版长什么样到怎么验证付费到凭什么是你。

## 1. 推荐产品形态（Product Form，对齐 Level 1-5）
现在推荐形态 Level：L1 人工加 AI 或 L2 半自动或 L3 自动化工作流或 L4 小工具或 L5 SaaS。为什么是它（引用 AI 可实现度开发难度证据）：。升级到下一级所需的证据：如 5 个付费客户乘重复交付 2 次。无付费用户前不跳到 L4/L5；若当前无需写代码明确写当前不需要开发。

## 2. 核心用户（Core User，收窄到第一版只服务的人群）
一句话画像（身份加场景加最想要的结果）：。他们在哪聚集（具体渠道传给 MONETIZE）：。第一版明确不服务谁：。

## 3. 核心功能（MoSCoW，M 不超过 3 项）
档位 功能 服务于哪个付费理由 第一版是否做。M Must-have（不超过 3）做。S Should-have（人工顶延后）不做。C Could-have 不做。W Won't-have now（黑名单）不做。自检：去掉哪个 M 用户就不会付钱？答不上等于功能未围绕结果设计。

## 4. MVP 范围（五项必填一个不能少）
第一版做什么：。第一版不做什么：。验证什么（优先验证是否有人为结果付钱）：。继续条件（量化）：如 2 周内不低于 3 人付费不低于 1 人复购。放弃转向条件（量化）：如接触 20 人无人愿付。现金成本时间成本（到首次可交付）交付方式。

## 5. 推荐技术方向（Tech Direction）
技术选型（无代码组合或 Python 加 SDK 轻脚本或简单前端或完整产品优先依赖最少）：。AI 做什么：人工做什么（质检点）：。选型理由最大缺点替代方案：。第三方依赖与成本及单项失败兜底：。核心交付物数据结构（字段稳定为 L2 到 L5 自动化与模块独立预留）：Deliverable input_fields output_fields human_qc_points。若 L1 无需开发：当前不需要开发。

## 6. 最小验证方案（Smallest Test of Value，开发前先验证）
验证假设：来自 EVALUATE 最弱项优先付费。实验形式：Concierge 或落地页冒烟或预售或众筹或 Fake Door 或访谈或样品试交付。目标对象：几个什么画像从哪来。成功标准：量化阈值。失败转向：换人群换报价换形态放弃的规则。（无产品验证方式清单见 references/monetization-gtm.md）

## 7. 差异化落地（Wedge）
一句话差异化主张（对谁哪个场景比现状好在哪凭什么你）：。对手复制成本：。在 MVP 中由哪个具体功能服务体现：。

## 8. 下一步与传给 MONETIZE 的输出

下一步行动：启动最小验证实验的第一个动作动词开头可量化。

传给 MONETIZE 的结构化输出：Offer 雏形产品 Level MVP in/out 单次交付成本核心用户聚集渠道。

进入 MONETIZE 最小验证实验 回看 EVALUATE。

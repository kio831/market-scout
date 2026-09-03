# Opportunity Card 模板（v2.0，兼容 v1.1 全部字段）

一屏速览卡：把 Problem Card 升级为值得跟踪的机会。v1.1 的评分（绑定证据）加证据链加竞争加状态加决策全部保留；v2.0 新增 Pipeline 五阶段指针、综合机会评分、三档结论（值得做建议验证后再做不建议做）与下游阶段卡导航。8 维评分与 Payment 分档见 references/problem-framework.md；交付状态机见 references/opportunity-state-machine.md；V2 流水线与综合评分见 references/pipeline-and-runtime.md、references/project-evaluation.md；完整汇总用 templates/opportunity-report.md。

## 机会卡片

Opportunity ID：MS-###（一旦分配固定不变）。机会名称：一句话。问题：来自 Problem Card 的问题表述。用户：具体画像。当前状态（Opportunity State 真实交付状态）：HYPOTHESIS/DEMAND_CONFIRMED/MARKET_CONFIRMED/PAYMENT_VALIDATION/CUSTOMER_FOUND/FIRST_PAYMENT/REPEATED_DELIVERY/STANDARDIZED/AUTOMATED/PRODUCTIZED。注意 FIRST_PAYMENT 必须实际收到真实付款；愿意购买愿意尝试报价意愿最多到 CUSTOMER_FOUND。Pipeline Stage（v2.0 分析流水线位置与交付状态正交）：FIND/VALIDATE/EVALUATE/BLUEPRINT/MONETIZE/REPORT。证据等级：A/B/C 来源：链接原文。v2.0 综合结论（完成 EVALUATE 后回填）：需求强度 Demand Strength N/10 综合机会评分 Opportunity Score NN/100 结论（绿值得做 GO 黄建议验证后再做 VALIDATE_FIRST 红不建议做 NO_GO）。

### 证据链（Problem / Solution / Payment 三类）
搜索类型 证据摘要 来源 证明什么 不能证明什么 置信度。Problem。Solution。Payment。

### 评分（1-10，每分必带理由加证据加不确定性）
维度 分 评分理由 对应证据或标注无直接证据 当前不确定性。Pain 痛苦。Frequency 频率。Payment 付费。Market 市场。AI Leverage AI 杠杆。Feasibility 可执行。MVP Speed 速度。Competition 竞争（越低越好）。

### 四问
为什么值得继续？最大的不确定性是什么？缺什么证据？下一步最应该验证什么（只做一件事）？

### 竞争与付费速览
已有工具 SaaS 人工服务免费方案：有无加例子。用户为什么不用：贵难用不知道不信任。当前价格锚：有则写无则未找到（标 C）。用户真正购买的是什么：结果时间效率成本降低。

### 状态机推进（见 references/opportunity-state-machine.md）
当前瓶颈：当前状态到下一状态缺什么证据。只推进这件事：一个动作。

### 初步判断（v1.1，研究阶段）
绿值得验证黄潜在机会需更多证据红不建议继续。若黄：继续验证的最小下一步。若红：停止原因加哪个证据导致停止加什么新证据可重启。

### V2 五阶段导航（v2.0 新增，逐阶段回填）
阶段 状态 产出卡片 关键结论。FIND 发现（已完成进行中 Problem/Evidence Card v1.1）。VALIDATE 需求验证（templates/demand-validation-card.md 需求强度 N/10 需求结论）。EVALUATE 项目评估（templates/project-evaluation-card.md 综合分 NN/100 Verdict）。BLUEPRINT 机会转项目（templates/project-blueprint-card.md Level MVP 最小验证）。MONETIZE 商业化获客（templates/monetization-gtm-card.md Offer 定价渠道第一笔钱）。

### 最终结论（v2.0，完成流水线后）
绿值得做 GO 黄建议验证后再做 VALIDATE_FIRST 红不建议做 NO_GO（判定规则见 references/project-evaluation.md）。第一步行动（今天做什么）：。完整报告：templates/opportunity-report.md。

# Project Evaluation Card 项目评估卡模板（v2.0，流水线阶段 EVALUATE）

阶段：FIND 到 VALIDATE 到 EVALUATE 到 BLUEPRINT 到 MONETIZE。方法见 references/project-evaluation.md；需求强度直接继承 VALIDATE 不得在此重打高。每一维分数必须四要素齐全：分数加理由加证据加不确定性；禁止市场很大式无依据结论。

# 项目评估（Project Evaluation）

FIND 已完成到 VALIDATE 已完成到 EVALUATE 进行中到 BLUEPRINT 待开始到 MONETIZE 待开始。

Opportunity ID：MS-### Pipeline Stage：EVALUATE 日期：YYYY-MM-DD。机会一句话：上游需求结论需求强度（直接继承不重打）：VALIDATE 结论加 N/10。

黄 建议验证后再做 VALIDATE_FIRST | 综合机会评分 NN/100 | 需求强度 N/10（继承）| Opportunity MS-###。一句话理由：（三档：绿值得做 GO 黄建议验证后再做 VALIDATE_FIRST 红不建议做 NO_GO）。

## 1. 七维评分（1-10，权重合计 100%）
维度（中文 English）权重 分 评分理由 对应证据或无直接证据 不确定性。需求强度 Demand Strength（继承 VALIDATE）20%。市场潜力 Market Potential 20%。竞争与差异化 Competition & Diff. 15%。AI 可实现度 AI Feasibility 15%。开发难度 Dev Effort（越易越高）10%。个人开发者适配度 Solo Fit 15%。风险可控性 Risk Control（越可控越高）5%。

分数条（统一 10 格）：需求强度 市场潜力 竞争与差异化 AI 可实现度 开发难度 个人适配 风险可控。

加权计算式（必须可手工复算）：Opportunity Score = (需求乘0.20 加 市场乘0.20 加 竞争差异乘0.15 加 AI乘0.15 加 开发乘0.10 加 个人适配乘0.15 加 风险乘0.05) 乘 10 = __/100。若调整过默认权重必须写明改了哪项为什么。

最强两项（机会靠什么成立）：最弱两项（可能死在哪里）：。

## 2. 市场潜力（Market Potential）
付费市场证据（在售服务价格成交来自 Payment Search）：。目标人群数量级估计（标注观察推断假设）：。增长趋势证据（两个时点缺则标证据不足）：。

## 3. 竞争与差异化（Competition & Differentiation）
竞争格局：空白早期或分散小玩家或头部集中或巨头碾压（判定理由加证据）。主要竞争者与价格带：。主差异化切入点（只选 1 个说明用户在意加你守得住的证据）：。对手复制它需要付出的成本：。

## 4. AI 可实现度（AI Feasibility）
是否在 AI 成熟能力区：错误代价与人工兜底成本：。质量稳定性数据接口可得性单人驾驭度：。若不稳降级到 Level 1-2 的做法：。

## 5. 开发难度 & 个人适配（Dev Effort & Solo Fit）
到可交付 MVP 的工作量周期现金成本：。Solo Fit 四匹配（匹配部分不匹配加理由）：技能时间资金渠道触达。

## 6. 风险表与致命红旗（Red Flags）
风险类别 具体风险 触发证据 规避低成本验证动作。需求竞争技术获客付费合规机会成本。

致命红旗逐项检查（命中任一直接红无论总分）：R1 无真实重复需求 R2 无任何付费可能使用者无付费权 R3 AI 无杠杆 R4 无法触达客户 R5 巨头免费碾压且无差异 R6 需重资金长周期团队 R7 合规平台明确禁止。

## 7. 结论与下一步（严格按阈值）

判定依据：总分 __；需求强度 __（GO 门槛不低于 7）；Payment 档位 __（GO 需 7-8 以上）；致命红旗 __（GO 需无）。

下一步行动：绿 GO 为什么现在值得做加第一个要盯死的风险到进入 BLUEPRINT。黄 VALIDATE_FIRST 要验证的关键假设最小实验转绿与转红的量化标准：。红 NO_GO 停止三要素为什么停哪个证据导致什么新证据可重启。

进入 BLUEPRINT 最小验证实验 商业化预览 停止机制。

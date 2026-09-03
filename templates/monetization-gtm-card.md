# Monetization & GTM Card 商业化与获客卡模板（v2.0，流水线阶段 MONETIZE）

阶段：FIND 到 VALIDATE 到 EVALUATE 到 BLUEPRINT 到 MONETIZE 到 REPORT。方法见 references/monetization-gtm.md；定价原则与第一笔钱十步清单复用 references/payment-validation.md。六问必须答全：谁会付钱？为什么付钱？卖什么？怎么收费？去哪找客户？第一批客户怎么来？当前版本不实现支付订阅会员系统只产出商业化方案与验证动作。字段对齐输出契约 MonetizationPlan。

# 商业化与获客（Monetization & Go-To-Market）

FIND 已完成到 VALIDATE 已完成到 EVALUATE 已完成到 BLUEPRINT 已完成到 MONETIZE 进行中。

Opportunity ID：MS-### Pipeline Stage：MONETIZE 日期：YYYY-MM-DD。上游输入：核心用户付费方替代成本（定价锚）产品 Level Offer 雏形单次交付成本个人约束（时间资金可触达渠道）。

商业化方案 | Opportunity MS-### | 主力价 价格 | 主渠道 渠道。一句话商业模式：向谁卖什么结果用模式收价格在主渠道获客预计时间动作拿到第一笔钱。第一笔钱目标：金额客户数期限。

## 1. Target Customer — 谁会付钱
角色 画像 说明。使用者 User。付费方 Payer（有无预算能否拍板）。决策影响者。ICP（理想客户）：身份规模最痛场景现有预算可接受客单价区间聚集渠道为什么现在就要。首批 10 个客户的画像与来源类型（不编造真人写到哪用什么筛选条件列出）：。

## 2. Offer — 卖什么（卖结果不卖 AI）
一句可售卖的话：我帮谁在场景用达成相比节省多赚降低交付周期。档位 交付什么 不交付什么 交付方式 单次成本耗时 价格。引流款 Magnet。主力款 Core（首推）。增值款 Upsell。Offer 不得超出 BLUEPRINT 的 MVP 能交付的范围。

## 3. Business Model — 怎么收钱
推荐模式：一次性或按结果按量或订阅包月或服务养产品或数字产品或培训咨询或分成（L1-L2 优先一次性或按结果）。理由：备选模式加切换触发条件：。早期不选 Freemium 付费投放平台抽佣除非已具备对应证据（说明理由）。

## 4. Pricing — 定价（可解释禁止编价）
价值锚（客户当前替代成本证据估算口径）：。市场锚（同类公开价格带 Payment Search 搜不到标证据不足）：。成本底线（现金加时间）：。定价方案：引流首单价主力价正价目标。为什么值这个价一句话：后续提价路径：。

## 5. 首批客户获取（First 10 Customers）
1. 名单来源（3 个具体来源）：。2. 筛选条件关键词：。3. 首次接触话术结构（对方问题到样品结果证明到低门槛尝试）：。4. 第一单转化（样品试做到报价到先收钱或定金）：。5. 第 2-10 单（反馈转介绍可公开案例）：。6. 今天做什么（1-3 个动作）：。

## 6. 获客渠道 & GTM 路径
渠道矩阵（早期主渠道不超过 2 按 ICP 聚集度排序）：渠道 类型（关系内容社区需求大厅合作付费 SEO）优先级 为什么。GTM 三阶段（对齐 Level 与状态机）：阶段 A（L1 0 到第一笔钱）关系线下加垂直社区 Concierge 交付验证付费：。阶段 B（L2-L3 重复交付到标准化）内容案例加转介绍加需求大厅补量：。阶段 C（L4-L5 产品化）内容 SEO 落地页规模化再谈投放 Freemium：。

## 7. 不开发产品的验证（No-Build Validation）
方式：Concierge 或落地页冒烟或 Fake Door 或预售定金或众筹或付费诊断或样品换证言。验证假设成功标准失败规则。纪律：点击留资想要只到 CUSTOMER_FOUND；真实付款才到 FIRST_PAYMENT。

## 8. 第一笔钱计划（对齐 payment-validation 十步）
找谁去哪找提供什么结果怎么展示 Demo 怎么报价怎么交付怎么收钱今天做什么成功标准失败后怎么调。

## 9. 待验证的商业化假设与下一步行动

今天做什么（1-3 个动作）：动词开头可量化能启动第一批客户获取。

待验证假设（Open Questions）：。

生成最终 Opportunity Report 第一笔钱清单 无产品验证。

## 10. 结构化输出（MonetizationPlan，模块数据契约）
MonetizationPlan: opportunity_id icp offer_ladder business_model pricing first_10_customers channels gtm_path no_build_validation first_payment_plan open_questions。进入最终 templates/opportunity-report.md 汇总。

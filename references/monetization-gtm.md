# Monetization & GTM — 商业化与获客（v2.0 新增，流水线第 5 阶段 MONETIZE）

本文件定义商业化评估与进入市场方法，集中回答六个问题：谁会付钱？为什么付钱？卖什么？怎么收费？去哪里找客户？如何获得第一批客户？产出为 templates/monetization-gtm-card.md。

阶段定位：FIND 到 VALIDATE 到 EVALUATE 到 BLUEPRINT 到 MONETIZE（本文件）到输出 Opportunity Report。复用 v1.1 定价原则与第一笔钱执行清单、Execution Mode、验证漏斗；本文件只新增商业模式设计、获客渠道矩阵、GTM 路径、无产品验证与模块化独立边界。

## 0. 模块化定位（为未来独立成产品预留，当前不开发支付订阅会员）

Monetization & GTM 被设计为可独立调用、可独立交付、未来可独立收费的模块：有明确的输入契约（§8.1）、输出契约（§8.2），只依赖结构化数据，不依赖具体 UI 与其他阶段的内部实现。未来可把本模块单独拆成商业化方案生成器或 GTM 顾问独立获客与收费，无需大规模重构。当前版本明确不实现支付、订阅、会员、计费等任何系统；本模块只产出商业化方案与验证动作。

## 1. Target Customer — 谁会付钱（区别于谁使用）

沿用 VALIDATE 的用户分层，但这里必须找到付费方（Payer）：使用者 User（谁日常用）、付费方 Payer（谁掏钱，是否有预算与拍产权）、决策影响者（谁影响购买决定）。使用者不等于付费方时（员工用老板付、学生用家长付、患者用机构付），方案必须围绕付费方的理由设计。输出 ICP（理想客户画像）：行业身份规模加最痛场景加现有预算加能接受的客单价区间加聚集渠道加一句他为什么现在就需要。给出首批 10 个目标客户的画像与来源类型（不是编造具体真人，而是到哪里用什么筛选条件能列出这 10 个）。

## 2. Offer — 卖什么（卖结果，不卖 AI）

用户购买的是结果而非技术。Offer 必须写成一句可售卖的话：我帮目标客户在场景用交付形态达成可感知结果，相比当前替代方案节省或多赚或降低可量化价值，交付周期多少。设计 3 档 Offer 阶梯（用于锚定与升单）：引流款（低门槛尝鲜或免费样品）到主力款（核心结果，首推）到增值款（更多次数或更快或更省心或定制）。每档写清交付什么、不交付什么、交付方式、单次交付成本与耗时（决定毛利与可否规模化）。Offer 必须与 BLUEPRINT 的 MVP 或形态一致，不允许商业化方案卖一个 MVP 交付不了的东西。

## 3. Business Model — 怎么收钱（个人开发者优先的模式库）

模式库：一次性买断（按件按项目，最易成交最快拿到第一笔钱，无复购靠不断接单）、按结果按量计费（可量化结果，客户好理解与价值挂钩，收入随工作量线性增长）、订阅包月 Retainer（周期性重复任务，可预测复购 LTV 高，需要持续交付与信任）、服务费加升级产品（先用服务验证后卖工具，服务现金流养产品化）、模板数字产品（标准化可复制资产，边际成本近零，需要流量与信任积累）、培训咨询社群（知识方法本身有价值，轻资产建立权威，依赖个人时间与影响力）、抽佣分成（撮合或增量价值清晰，客户零前期风险，结算复杂个人难监管）、免费增值 Freemium（L4/L5 产品化之后，获客面广，早期不推荐因为免费用户不等于付费验证且有开发与服务器成本）。
选择规则：L1-L2 阶段优先一次性或按结果快速拿到真实付款；出现重复交付后转订阅（与状态机 REPEATED_DELIVERY 到 STANDARDIZED 对齐）。必须写明推荐模式加理由加备选模式加切换到备选的触发条件。禁止一上来就设计 Freemium 或平台抽佣等需要规模才成立的模式。

## 4. Pricing — 定价（必须可解释）

沿用 payment-validation.md 定价原则（价格锚定在替代成本上），按以下步骤给价：1. 价值锚：客户当前替代成本（VALIDATE 的时间乘时薪、外包费、返工损失），必须有证据或标注估算口径。2. 市场锚：同类产品或服务公开价格带（Payment Search 证据，搜不到标证据不足不得编价）。3. 成本底线：单次交付现金成本加时间成本，低于底线不做。4. 定价方案：给出引流价或首单价、主力价、正价目标，以及为什么值这个价的一句话价值说明。5. 提价路径：随着交付证据或案例积累如何分阶段提价（允许 10/30/50/100 元小额起步验证，这是验证手段不是最终定价）。定价必须能回答客户的潜台词：我现在花 X 成本或忍受 Y 损失，付你 Z 为什么划算？

## 5. 首批客户获取（First 10 Customers）

给出可执行的首批客户获取路径（复用并细化 payment-validation.md 第一笔钱清单）：1. 名单从哪来：列出 3 个能找到目标客户的具体来源（你现有人脉或所在圈层或线下场景或垂直社群或平台搜索或内容评论区或外包需求大厅）。2. 怎么筛：用什么关键词或特征筛出最可能付钱的 10 个人。3. 怎么接触：首次接触话术结构（说对方的问题到给一个样品或结果证明到提出低门槛尝试），不群发硬广。4. 怎么转化第一单：样品或试做或诊断到报价到先收钱再交付（或小额定金）。5. 怎么要到第 2-10 单：交付后要反馈、要转介绍、要可公开案例。6. 今天做什么：1-3 个当天可执行动作（与 Execution Mode 一致）。

## 6. 获客渠道矩阵与 GTM 路径

### 6.1 渠道矩阵（按 ICP 聚集度排序，早期只选 1-2 个主渠道打透）

渠道类型：关系线下 Warm（熟人本地商户同学校友行业群，本地垂直高信任服务，最高优先级零成本反馈最快）、内容获客 Owned（小红书抖音知乎公众号 B 站垂直内容，可被搜索可展示前后对比的结果，高优先级一条爆款内容等于持续线索需持续产出）、社区渗透 Community（垂直论坛 Reddit V2EX 行业微信群 Discord，用户高度集中的圈层，高优先级先贡献价值再转化禁止一进群就卖）、平台需求大厅 Marketplace（闲鱼淘宝服务 Fiverr Upwork 猪八戒，标准化代做按件交付，中优先级来单快但比价严重价格低）、合作分销 Partnership（与互补商家互相推荐，有互补资源后，中优先级需先有交付案例）、付费投放 Paid（信息流搜索广告，L4 加有转化数据后，早期不推荐未验证转化时投流等于烧钱）、SEO 落地页（垂直关键词落地页 Fake Door，有明确搜索需求，中优先级慢热可作为验证与长期资产）。

### 6.2 GTM 路径（与 Level 1-5、状态机对齐）

阶段 A（L1，0 到第一笔钱）：关系线下加垂直社区，Concierge 人工交付，验证付费。阶段 B（L2-L3，第一笔钱到重复交付到标准化）：内容沉淀案例加转介绍加平台需求大厅补量，固定报价与交付。阶段 C（L4-L5，产品化）：内容 SEO 落地页规模化获客，再考虑付费投放与 Freemium。每进入下一阶段需满足证据条件（沿用状态机 FIRST_PAYMENT 到 REPEATED_DELIVERY 到 STANDARDIZED 到 AUTOMATED 到 PRODUCTIZED），不得在 0 付费时直接跳到阶段 C 的打法。

## 7. 不开发产品的验证方式（No-Build Validation）

在写代码前验证商业假设，与 BLUEPRINT 最小验证方案配套：Concierge（人工代做，表面提供服务后台全人工加 AI 完成，验证是否有人为结果付费最强信号）、Smoke Test 落地页（一页讲清价值与价格放购买或报名按钮看点击与留资，验证兴趣与转化意向注意意向不等于付款）、Fake Door（在现有内容或页面加入是否需要 XX 入口看需求，验证需求主动性）、预售定金（先报价收定金再交付，验证真实付费可推进 PAYMENT_VALIDATION）、众筹团购（凑够 N 人再开工，验证需求密度与价格敏感度）、付费咨询诊断（用 1 对 1 诊断收费同时挖需求，验证付费意愿加一手痛点）、代做样品换证言（免费或低价做一份换真实反馈与公开评价，验证价值感知与传播素材）。
纪律（沿用 v1.1）：点击留资我想要愿意试试都只是意向，最多到 CUSTOMER_FOUND；只有真实付款才推进 FIRST_PAYMENT。

## 8. 模块数据契约（接口边界，保证未来可独立）

### 8.1 输入契约（MonetizationInput）

本模块只要求上游提供以下结构化字段（缺失字段标缺失并回退补证据，不编造）：opportunity_id（来自状态机）、demand（来自 VALIDATE：core_user、payer、current_alternatives_cost、pay_reason_chain）、evaluation（来自 EVALUATE：verdict、differentiation_wedge、ai_feasibility_score）、blueprint（来自 BLUEPRINT：product_level、offer_seed、mvp_scope、unit_delivery_cost）、constraints（用户自身约束：weekly_time、cash_budget、channels_access）。

### 8.2 输出契约（MonetizationPlan）

opportunity_id、icp（user、payer、budget_signal、where_to_find）、offer_ladder（tier magnet|core|upsell、deliverable、price、unit_cost）、business_model（primary、why、backup、switch_trigger）、pricing（value_anchor、market_anchor、floor、entry_price、target_price、rationale）、first_10_customers（sources、filter、outreach、first_deal、referral、today_actions）、channels（name、type、priority high|mid|low、why，主渠道不超过 2）、gtm_path（stage A|B|C、move、evidence_to_next）、no_build_validation（method、hypothesis、success_rule、fail_rule）、first_payment_plan（对齐 payment-validation 十步清单）、open_questions（仍待验证的商业化假设）。

独立性保证：任何上游只要按 8.1 提供数据，本模块即可独立产出 8.2；本模块不反向依赖报告排版与其他阶段内部实现。未来独立成产品时，这两个 schema 就是它的 API 边界。

## 9. 输出要求（Monetization & GTM Card）

使用 templates/monetization-gtm-card.md：付费方 ICP、三档 Offer、商业模式与理由、可解释定价、首批 10 客户获取、主渠道、GTM 三阶段、无产品验证、第一笔钱计划、待验证假设。结尾必须落回 Execution：今天做什么、第一笔钱怎么收、成功失败标准（对齐 payment-validation.md）。本卡是最终 Opportunity Report 的第 5 段；字段须满足 8.2 输出契约。

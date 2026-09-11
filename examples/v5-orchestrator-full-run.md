# V5 完整流程示例：Orchestrator Full Mode（数据为示意，演示路由与闭环）

> 演示：一个新想法从 IDEA 走到 ACTION，Main 依次调度六个 Specialist，Context 全程单向更新。
> 本示例同时展示四套代码（证据等级/Opportunity State/Pipeline State/Decision Code）如何正交并存。

## 用户输入（IDEA）

“学校打印店经常有人让老板帮忙改 PDF 格式，能不能做个小工具？”

## 路由日志（Main）

    input_summary: 一句想法，无资料
    state_detected: IDEA（无任何卡片）
    mode: FULL
    dispatch: Idea Observer → Problem Scout → Evidence Hunter → Opportunity Scout → Opportunity Score → Main 决策门 → Action

## Step 1 — Idea Observer（IDEA → OBSERVATION）

    who: 大学打印店顾客与店主
    problem: 改 PDF 格式/合并/排版等小任务要花钱找人或自己折腾
    frequency: 店主称“经常有人来问”（样本待补，标 B）
    current_solution: 付费让店主弄 / 自己装软件折腾
    payment_signal: 打印店按次收费
    ai_leverage: 高——低技能重复劳动，AI 工具可直接输出结果
    hypothesis_flags: [“开场白式估计，未见账单记录”]

## Step 2 — Problem Scout（OBSERVATION → PROBLEM）

    target_user: 打印店顾客（学生为主）与店主
    scenario: 课程材料/论文需要改格式时
    evidence_level: B（真实场景但外部验证不足）
    category: 重复劳动 + 技能门槛类
    停手检查: 通过（非单次偶发，付费行为存在）

## Step 3 — Evidence Hunter（PROBLEM → EVIDENCE）

    Problem Search: 找到多条“打印店改 PDF 收 5-10 元”“毕业论文调格式崩溃”等公开抱怨（来源略）
    Solution Search: 现有方案=打印店人工服务 / WPS 会员 / 免费网站，各有权衡
    Payment Search: 打印店按次收费、代做服务有标价 → 付费行为确认
    coverage: problem 85 / solution 70 / payment 75 / competition 60 / distribution 55 / buildability 80
    overall_coverage: 71 | critical_gaps: [distribution]

## Step 4 — Opportunity Scout（EVIDENCE → OPPORTUNITY）

    demand_summary: 真实需求已验证（核心用户=打印店顾客；付费理由链完整：省时间/省麻烦）
    competition_gap: 四问结论——用户有真实需求；现有方案贵或需会员；用户仍在抱怨；缺口=轻量/按次/不用装软件的档位
    state: DEMAND_CONFIRMED
    bottleneck: 轻量档的付费意愿未验证

## Step 5 — Opportunity Score（OPPORTUNITY → SCORED）

    dims: demand 88 / pain 91 / competition 62 / monetization 80 / buildability 94 / distribution 61 / ai 89
    total: 86（=88×0.15+91×0.15+62×0.15+80×0.20+94×0.15+61×0.10+89×0.10）
    confidence: Medium（46）| hard_gates: gate PASS / ceiling [] / red_flags []
    解释: 高需求高痛点开发成本低是优势；获客难度与代账式竞品是主要风险

## Step 6 — Main 决策门（SCORED → DECISION）

    code: RECOMMENDED（分数≥75 + 需求/痛点/变现均过线 + 无门槛/红旗）
    verdict: VALIDATE（distribution 覆盖 55 < 60，先做最低成本验证再 BUILD）
    why:
      1. 痛点明显且重复出现
      2. 三类搜索证据齐备（含付费行为）
      3. 竞品存在轻量档缺口
      4. MVP 开发难度低
      5. 有明确付费路径

## Step 7 — Validation Scout（DECISION → VALIDATION）

    core_hypothesis: 打印店顾客愿意为“一次几元的临时改格式”付费
    method: PreSale / 人工试交付（在 3 家打印店门口放二维码小样，人工接单）
    sample: 20 / duration: 7 天 / cost: 约 20 元
    success: ≥2 人付款 → BUILD 轻量网页工具
    failure: 0 付款 → 修改 Offer 重验；仍失败 → PARK

## Step 8 — Main Action（VALIDATION → DECISION → ACTION）

    今天的行动: 今天联系 3 家打印店老板，谈“帮你接改格式的活分你 30%”（动词+对象+数量+成功标准：谈下 1 家算成功）

## 闭环自检

- [x] state 链连续：IDEA→OBSERVATION→PROBLEM→EVIDENCE→OPPORTUNITY→SCORED→VALIDATION→DECISION→ACTION
- [x] 每个结论有 Evidence/Inference/Unknown 标注
- [x] 分数可复算，Why 编号齐全，今天做什么可执行
- [x] 停手权未被破坏（证据不足处降为 VALIDATE 而非强行 BUILD）

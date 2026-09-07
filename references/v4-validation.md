# V4 Validation Engine — 验证引擎（v4.0.0 新增）

> V3.1 回答「这个机会怎么样？」；V4 回答「**那我们怎么用最低成本证明它？**」以及验证之后「**真实结果出来了，继续、修改还是放弃？**」
> V4 = V3.1 + **Validation Layer**：不重做、不新增评分体系，只把"判断"延伸成"判断 → 最低成本验证 → 读真实结果 → 重新判断"。
> 主链路：FIND → PROVE → SCORE → DECIDE → **VALIDATE → RESULT → LEARN → DECIDE AGAIN**

## 0. 五条铁律（V4）

1. **Evidence First**：没有证据就标 Unknown，不补模型猜测。
2. **Validate Before Build**：证据不足时先验证，禁止默认输出 Build MVP。
3. **Lowest Cost First**：能验证核心假设的前提下，优先成本最低、时间最短、最容易拿到真实反馈的方法。
4. **Reality > Prediction**：真实验证结果优先于此前的模型判断。
5. **No Fake Precision**：没有依据的阈值/数据一律标 Unknown 或"实验设计假设，需首轮校准"，禁止伪造。

## 1. 从哪里开始：读取 V3.1，找"最大未知"

先读取（复用，不重算）：

```text
Unknowns（v3-evidence 看板）
Critical Gaps（v3-evidence-coverage）
Evidence Coverage（六维）
Confidence（v3-confidence）
Hard Gates / Score Ceiling（v3-hard-gates）
Decision（v3-decision）
Evidence-driven Action（v3-action-plan §6）
```

然后找到**当前最影响决策的 Unknown / Critical Gap**（通常 = 覆盖度最低的关键维度）。

```text
例：Payment Coverage = 20，Confidence = Low
最大未知：用户是否愿意付费
→ 验证围绕"付费意愿"，而不是直接开发产品。
```

## 2. Validation Plan（必须回答 11 问）

| # | 问题 | 输出字段 |
|---|---|---|
| 1 | 验证什么？ | core_hypothesis（一句话，来自最大未知） |
| 2 | 为什么验证？ | critical_unknown（引用 Coverage / 看板） |
| 3 | 验证谁？ | target_user（继承 VALIDATE 核心用户） |
| 4 | 怎么验证？ | method（§3 选择逻辑） |
| 5 | 在哪里验证？ | channel（来自证据，禁止假设不存在的渠道） |
| 6 | 需要多少样本？ | sample_size（含依据；无依据标 Unknown + 校准说明） |
| 7 | 需要多长时间？ | duration |
| 8 | 需要多少成本？ | estimated_cost |
| 9 | 成功是什么？ | success_criteria（量化，§5） |
| 10 | 失败是什么？ | failure_criteria（与成功对称，§5） |
| 11 | 验证后进入哪个状态？ | next_state（§8 状态机） |

## 3. Validation Method / Lowest-Cost Validation

### 3.1 基础映射（禁止机械套用）

| 最大未知 | 默认最低成本方法 | 说明 |
|---|---|---|
| 需求是否真实 | User Interview 用户访谈 | 5-10 人，1 对 1 问痛点与历史行为 |
| 是否愿意尝试 | Landing Page / Demo / Prototype 冒烟 | 一页讲清价值，看点击/留资（意向≠付费） |
| 是否愿意付费 | Offer / Pre-sale / Paid Test | 报价/预售/小额付费测试，验证真实付款 |
| 交付能力 | Manual Delivery / AI-assisted Service | 人工+AI 试交付，验证能否稳定交付 |
| 方案有效性 | Small Pilot 小范围试点 | 少量真实用户跑通全流程 |
| 需求+付费证据已足够 | 才允许 MVP（Build） | §4 判定 |

### 3.2 选择规则（Agent 必须说明理由）

1. 在多个可行方法中，按 **成本（低→高）→ 时间（短→长）→ 反馈真实性（高→低）** 排序，取最低成本。
2. 选择的理由必须绑定当前 Critical Gap / Unknown / Decision / Evidence，不能只看表。
3. 若最低成本方法拿到真实反馈的概率过低，可上升一级并说明原因。

```text
例：同一机会存在 "User Interview" 与 "Build MVP"
→ 最大未知是付费意愿 → 最低成本 = Interview/Paid Test，先于 MVP。
```

## 4. 禁止默认 MVP（Validate before Build）

出现以下任一情况，**输出 Validation Experiment，不输出 Build MVP**：

- Payment 证据不足（Payment 覆盖 < 40，或付费子信号存在 Unknown）
- Problem 证据不足（Problem 覆盖 < 40）
- 存在未解决的关键 Unknown（来自 v3-evidence 看板）

```text
先找 20 个目标用户 → 测试需求 → 测试 Offer → 测试付款 → 再决定是否开发 MVP
```

## 5. Validation Experiment（标准结构）

每个 Validation Plan 必须落成一个具体实验：

```text
Hypothesis        一句话核心假设（来自最大未知）
Target User       谁（继承上游，具体画像）
Channel           在哪验证（来自证据）
Experiment        具体动作（动词+对象+数量）
Offer / Stimulus  用什么刺激（报价/样品/演示）
Sample Size       样本数（含依据）
Duration          时长
Cost              成本（现金+时间）
Success Criteria  成功标准（量化）
Failure Criteria  失败标准（量化，与成功对称）
Decision Rule     成功/部分/失败 → 分别怎么做（§6）
```

```text
例：
Hypothesis: 目标商家愿意为 AI 内容服务付费。
Target:     20 个目标商家（1-3 名员工、本地、近 30 天发过内容）。
Channel:    本地商家微信群 + 小红书本地话题。
Experiment: 私信 20 家 → 展示 1 条免费样品 → 报价 199 元/首月。
Offer:      199 元/首月（锚定代运营 1/10）。
Sample:     20；Duration: 7 天；Cost: 约 4-6 小时。
Success:    ≥5 个明确表达需求 且 ≥2 个愿意付款。
Failure:    20 人中 <2 个愿意付款。
Decision:   Success → Continue；Partial → Modify Offer/Target；Failure → Revisit Problem。
```

## 6. Success / Failure Criteria

- **必须量化**：样本、回复率、兴趣率、转化率、预约率、试用率、付费率、留存、复购。
- 禁止模糊表达："看看反馈怎么样 / 观察市场反应 / 如果反响不错"。
- 无足够依据确定阈值时：`Threshold = Unknown`，并明确告知"当前阈值是实验设计假设，需在首轮测试中校准"。
- **Failure 与 Success 对称**：开始验证前用户就知道什么情况下应停止。

```text
Success: 20 人中 ≥5 人明确表示需求 且 ≥2 人愿意付款
Failure: 20 人中 <2 人愿意付款
```

## 7. Decision Rule（提前定义，事后不凭感觉解释）

```text
IF Success        → Continue（继续推进；通常进入 CUSTOMER_FOUND / FIRST_PAYMENT / BUILDING）
IF Partial Success → Modify（改 Hypothesis / Offer / Target / Channel，重新验证，不直接 Build）
IF Failure        → Stop / Revisit / Abandon（回 Problem 或按停止机制）
```

## 8. Validation Result（用户回填真实验证结果）

用户把真实结果交回，结构示例：

```yaml
validation_result:
  opportunity_id: MS-###
  sample_n: 20
  interested: 8
  trial: 4
  paid: 1
  revenue: 99
  cost: 0
  duration_days: 3
  notes: ""            # 用户补充（真实原话/截图等）
```

### 8.1 事实与判断分级（沿用 Evidence 原则）

```text
Observed（事实）: 20 人中 8 人表达兴趣；1 人实际付款（¥99）。
Inference（推断）: 存在一定需求，但付费证据仍弱。
Unknown（未知）:  是否可以规模化获客、留存如何。
```

**禁止**：`8 人感兴趣 = 市场需求已经验证`。

### 8.2 输入校验

- 缺失字段标【缺失】；observed 计数必须是数字，与 sample_n 一致（interested ≤ sample_n 等）。
- 明显冲突或无法核实 → 按 Unknown 处理并提示，不强行采纳。

## 9. Re-evaluation（规则化重算，可复算）

读取：原 Score / Confidence / Coverage / Hard Gates / Critical Gaps + Validation Result。

```text
R1 结果分级：observed → 被验证维度的 Evidence；推断 → Inference；未测 → Unknown。
R2 覆盖度更新（只动被验证维度）：
   付费维度：paid==0 且 sample≥20 → Payment 覆盖 = 15（insufficient）
             0 < paid/sample < success_rate → 45（partial）
             paid/sample ≥ success_rate → 75（covered）
   需求维度：interested/sample ≥ success_rate → Problem 覆盖 = 75
             0 < rate < success_rate → 45；interested==0 → 15
R3 子信号更新（只动被直接测到的子信号，按 rubric 档位）：
   M1 付费证据：paid_rate==0 → 2；0<rate<success_rate → 6；rate≥success_rate → 8
   D1/D3（若验证的是需求）：按 interested_rate 同理
   其余子信号不动。
   计算约定：子信号明细可得时，更新对应子信号后重算维度分；
   明细不可得时，用维度级校准映射（付费：0→25 / 部分→55 / 达标→80；
   需求：0→30 / 部分→55 / 达标→75），并在报告中写明采用的是哪种。
R4 Confidence 重算：用新 Coverage + 被验证的 Unknown 清零，重跑 v3-confidence 公式。
R5 Decision 重判：用新维度分重算 Opportunity Score，重跑 hard gates/ceilings + v3-decision。
```

输出标注：**"基于真实验证证据重算"**。禁止伪造未测数据（No Fake Precision）。

```text
Before         Validation                 After
Score 82      20 users / 8 interested     Score 86
Confidence Low / 3 trial / 2 paid         Confidence Medium
Decision POTENTIAL                        Decision RECOMMENDED
（示例数字；真实运行按 §9 规则计算）
```

## 10. Learn Loop（闭环）

```text
Hypothesis → Research Evidence → Decision → Validation Experiment → Real-world Evidence → Updated Decision
（FIND → PROVE → SCORE → DECIDE → VALIDATE → LEARN → DECIDE AGAIN）
```

Market Scout 不再是一次性报告生成器：每轮验证产生的新 Evidence 会回灌 Coverage / Confidence / Decision，形成持续迭代。

## 11. Opportunity State 集成（扩展现有状态机，不建第二套）

在既有状态机（`opportunity-state-machine.md`）插入三个状态：

```text
… MARKET_CONFIRMED → VALIDATING（已设计并开始最低成本验证）
                      ↓
                   VALIDATED（达到成功标准）→ CUSTOMER_FOUND / FIRST_PAYMENT …
                      ↓（partial）
                   REVISE（修改假设/Offer/人群）→ 回到 VALIDATING
                      ↓（failure）
                   回 HYPOTHESIS 或按停止机制（STOPPED）
```

- VALIDATING：Validation Plan 已生成并开始执行。
- VALIDATED：Observed 结果达到 Success Criteria。
- REVISE：Partial Success，修改后重新验证。

## 12. 与 Decision 的关系

| Decision | 与 Validation 的关系 |
|---|---|
| RECOMMENDED | 证据已足够支持推进，仍可进入 Validation（用真实结果加固判断） |
| POTENTIAL | 需要验证关键假设，**通常优先进入 Validation** |
| NOT_RECOMMENDED | 默认不应再投入验证成本；仅当用户明确要求重新验证某个核心假设时才进入 |

## 13. V4 数据契约（V3Output 增量）

```yaml
validation:                       # v4-validation.md
  status: not_started | designing | running | succeeded | failed | revised
  core_hypothesis: string
  critical_unknown: string
  method: UserInterview | LandingPage | PreSale | PaidTest | ManualDelivery | SmallPilot | MVP
  why_method: string
  target_user: string
  channel: string
  experiment: string
  sample_size: int|string
  duration: string
  estimated_cost: string
  success_criteria: string
  failure_criteria: string
  decision_rule: {success: "", partial: "", failure: ""}
  next_state: VALIDATING|VALIDATED|REVISE|...
  result: null | {sample_n, interested, trial, paid, revenue, cost, duration_days, notes}
  re_evaluation: null | {updated_coverage, updated_score, updated_confidence, updated_decision, reality_note}
```

## 14. 输出与报告结构

- Validation Output（§18 SOP 字段）：Validation Status / Core Hypothesis / Critical Unknown / Method / Why This Method / Target User / Channel / Experiment / Sample / Duration / Cost / Success / Failure / Decision Rule / Next Action。
- Validation Report（§19 SOP 结构）：Current Decision → Why Validate → Validation Plan → Experiment → Success → Failure → Decision Rule → Validation Result → Updated Assessment → Next Action。
- 输出模板：`templates/v4-validation-card.md`。

## 15. 边界（V4 明确不做）

❌ 新评分体系 / 更多评分指标　❌ 自动联系真实用户　❌ 自动支付/收款　❌ 自动投广告
❌ CRM / 数据库 / 复杂后台　❌ V5 功能　❌ 为了版本号加功能
V4 只做一件事：**Validation**（最低成本验证 + 读结果 + 重新判断）。

## 16. 验收清单

- [ ] 能生成 Validation Plan（11 问齐全）？
- [ ] 能找到 Critical Unknown（引用 Coverage/看板，非拍脑袋）？
- [ ] 优先选择最低成本验证方法（含理由）？
- [ ] 证据不足时不默认 Build MVP（Validate before Build）？
- [ ] Success / Failure Criteria 量化且对称？无依据时标 Threshold=Unknown？
- [ ] 能接受真实 Validation Result 并区分 Observed/Inference/Unknown？
- [ ] 能按 §9 规则重新评估 Score / Confidence / Coverage / Decision（可复算）？
- [ ] 形成完整闭环（LEARN → DECIDE AGAIN）？


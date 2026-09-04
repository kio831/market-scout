# Project Evaluation Card 项目评估卡模板（v2.0，流水线阶段 EVALUATE）

> 阶段：FIND → VALIDATE → **EVALUATE** → BLUEPRINT → MONETIZE。
> 方法见 `references/project-evaluation.md`；需求强度直接继承 VALIDATE，不得在此重打高。
> 每一维分数必须四要素齐全：分数 + 理由 + 证据 + 不确定性；禁止"市场很大"式无依据结论。

---

# 项目评估（Project Evaluation）

`FIND ✅ → VALIDATE ✅ → EVALUATE 🔄 → BLUEPRINT ⏳ → MONETIZE ⏳`

**Opportunity ID**：<MS-###>　**Pipeline Stage**：EVALUATE　**日期**：<YYYY-MM-DD>
**机会一句话**：<>　**上游需求结论/需求强度（直接继承，不重打）**：<VALIDATE 结论 + N/10>

> **🟡 建议验证后再做 VALIDATE_FIRST**　|　综合机会评分 **<NN/100>**　|　需求强度 **<N/10>**（继承）　|　Opportunity **<MS-###>**
> 一句话理由：<>（三档：🟢 值得做 GO / 🟡 建议验证后再做 VALIDATE_FIRST / 🔴 不建议做 NO_GO）

## 1. 七维评分（1-10，权重合计 100%）
| 维度（中文 / English） | 权重 | 分 | 评分理由 | 对应证据 /【无直接证据】 | 不确定性 |
|---|---|---|---|---|---|
| 需求强度 Demand Strength（继承 VALIDATE） | 20% |  |  |  |  |
| 市场潜力 Market Potential | 20% |  |  |  |  |
| 竞争与差异化 Competition & Diff. | 15% |  |  |  |  |
| AI 可实现度 AI Feasibility | 15% |  |  |  |  |
| 开发难度 Dev Effort（越易越高） | 10% |  |  |  |  |
| 个人开发者适配度 Solo Fit | 15% |  |  |  |  |
| 风险可控性 Risk Control（越可控越高） | 5% |  |  |  |  |

### 分数条（统一 10 格）
```
需求强度    ████████░░ N/10
市场潜力    ███████░░░ N/10
竞争与差异化 ██████░░░░ N/10
AI 可实现度 ████████░░ N/10
开发难度    ███████░░░ N/10
个人适配    ███████░░░ N/10
风险可控    ███████░░░ N/10
```

### 加权计算式（必须可手工复算）
```text
Opportunity Score = (需求×0.20 + 市场×0.20 + 竞争差异×0.15 + AI×0.15
                    + 开发×0.10 + 个人适配×0.15 + 风险×0.05) × 10
                  = ( __ + __ + __ + __ + __ + __ + __ ) × 10 = __/100
```
> 若调整过默认权重，必须写明：改了哪项、为什么。

- **最强两项（机会靠什么成立）**：<>
- **最弱两项（可能死在哪里）**：<>

## 2. 市场潜力（Market Potential）
- 付费市场证据（在售服务/价格/成交，来自 Payment Search）：<>
- 目标人群数量级估计（标注观察/推断/假设）：<>
- 增长/趋势证据（两个时点，缺则标【证据不足】）：<>

## 3. 竞争与差异化（Competition & Differentiation）
- 竞争格局：<空白早期 / 分散小玩家 / 头部集中 / 巨头碾压>（判定理由+证据）
- 主要竞争者与价格带：<>
- **主差异化切入点（只选 1 个，说明用户在意 + 你守得住的证据）**：<>
- 对手复制它需要付出的成本：<>

## 4. AI 可实现度（AI Feasibility）
- 是否在 AI 成熟能力区：<>　错误代价与人工兜底成本：<>
- 质量稳定性 / 数据·接口可得性 / 单人驾驭度：<>
- 若不稳，降级到 Level 1-2 的做法：<>

## 5. 开发难度 & 个人适配（Dev Effort & Solo Fit）
- 到可交付 MVP 的工作量/周期/现金成本：<>
- Solo Fit 四匹配（匹配/部分/不匹配 + 理由）：技能<>｜时间<>｜资金<>｜**渠道触达**<>

## 6. 风险表与致命红旗（Red Flags）
| 风险类别 | 具体风险 | 触发证据 | 规避/低成本验证动作 |
|---|---|---|---|
| 需求/竞争/技术/获客/付费/合规/机会成本 |  |  |  |

**致命红旗逐项检查（命中任一 → 直接 🔴，无论总分）**：
- [ ] R1 无真实重复需求　[ ] R2 无任何付费可能/使用者无付费权　[ ] R3 AI 无杠杆
- [ ] R4 无法触达客户　[ ] R5 巨头/免费碾压且无差异　[ ] R6 需重资金长周期团队　[ ] R7 合规/平台明确禁止

## 7. 结论与下一步（严格按阈值）

**判定依据**：总分 __；需求强度 __（GO 门槛≥7）；Payment 档位 __（GO 需 7-8 以上）；致命红旗 __（GO 需无）。

**👉 下一步行动**：
- 🟢 **GO**：为什么现在值得做 + 第一个要盯死的风险 → 进入 BLUEPRINT。
- 🟡 **VALIDATE_FIRST**：要验证的关键假设 / 最小实验 / 转🟢与转🔴的量化标准：<>
- 🔴 **NO_GO**：停止三要素——为什么停 / 哪个证据导致 / 什么新证据可重启。

[📐 进入 BLUEPRINT](templates/project-blueprint-card.md)　[🔬 最小验证实验](references/project-blueprint.md#6-最小验证方案smallest-test-of-value)　[💰 商业化预览](references/monetization-gtm.md)　[⚠️ 停止机制](references/payment-validation.md#6-停止机制stop-conditions)

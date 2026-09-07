# 示例：Validation Plan 验证计划（v4.0.0）

> ⚠️ 演示数据：仅展示方法。真实运行必须基于 V3.1 输出设计，Search First。
> 场景延续 examples/v3-decision-run.md（本地小店小红书文案代做），但此处聚焦"验证计划"环节。

**Opportunity ID**：MS-301　**Validation Status**：designing

## 1. Current Decision（来自 V3.1）

- Score：**73/100**　Confidence：**Low**（59）　Decision：**POTENTIAL**
- Hard Gates：G1-G5 PASS；**C1 Payment CEILING**（Payment 覆盖 20 < 30）
- Coverage：**68%**（critical_gaps：payment evidence）

## 2. Why Validate

- Critical Gap：Payment 覆盖 20（insufficient）
- 最大未知：**目标商家是否愿意为"AI 成品文案月付"付钱**（M1-M4 均为 Unknown）

## 3. Validation Plan

| 字段 | 内容 |
|---|---|
| Core Hypothesis | 本地小店主愿意为 199 元/月的成品文案服务付费 |
| Critical Unknown | 付费意愿与可接受价格（M1/M2 Unknown） |
| Method | **PaidTest / PreSale（报价预售）** |
| Why This Method | 付费意愿是唯一决定性未知；访谈只能得到"愿意"，报价+收款才能得到真实付款（最低成本且反馈最真实） |
| Target User | 周边 3 公里、1-3 名老师/员工、近 30 天发过内容但效果差的小型教培/美甲/餐饮店主 |
| Channel | 本地商家微信群 + 小红书本地话题（Evidence：商家群活跃） |
| Sample Size | 20 家（依据：默认实验设计假设，首轮校准） |
| Duration | 7 天 |
| Estimated Cost | 约 4-6 小时人工（现金≈0） |

## 4. Experiment

```text
1. 用关键词筛选 20 家目标商家名单
2. 每家先免费做 1 条垂直品类样品（前后对比）
3. 报价 199 元/首月（锚定代运营 1/10），48h 内跟进
4. 记录：明确需求数 / 试用数 / 真实付款数
```

## 5. Success Criteria

- ≥5 家明确表达需求（样本 20）
- **且 ≥2 家真实付款**（付费率 ≥10%）

## 6. Failure Criteria

- 20 家中 **<2 家愿意付款**（对称线：0-1 家）

> 阈值当前为实验设计假设（Threshold=Unknown 已注明），需在首轮测试中校准。

## 7. Decision Rule

```text
IF Success（≥5 需求 且 ≥2 付款） → Continue：进入 CUSTOMER_FOUND / 真实交付
IF Partial（有付款但 <2 家）     → Modify：改 Offer（99 体验价 / 换品类），重新验证
IF Failure（0-1 家付款）         → Stop / Revisit：回查 Problem，不开发产品
```

## 8. Next Action（今天）

1. 搜索"本地 教培/美甲 招生"话题，收集 20 家目标名单 → 标准：≥5 家可私信
2. 为最匹配的 3 家各做 1 条免费样品 → 标准：当天发出
3. 48h 内报价并记录回应 → 标准：20 家全部跟进完

**Next State**：VALIDATING（开始执行本计划）


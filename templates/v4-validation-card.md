# Validation Card 验证卡（v4.0.0）

> 方法见 `references/v4-validation.md`。一张卡走完：计划 → 实验 → 结果 → 重新判断。
> 必须先读 V3.1 输出（Unknowns / Critical Gaps / Coverage / Confidence / Hard Gates / Decision）。

**Opportunity ID**：<MS-###>　**Validation Status**：<not_started / designing / running / succeeded / failed / revised>

## 1. Current Decision（当前判断，来自 V3.1）

- Score：<NN>/100　Confidence：<High/Medium/Low>　Decision：<RECOMMENDED / POTENTIAL / NOT_RECOMMENDED>
- Hard Gates：<PASS / CEILING / FAIL>　Coverage：<NN>%（critical_gaps：<...>）

## 2. Why Validate（为什么验证）

- Critical Gap / Unknown（引用）：<...>
- 最大未知：<一句（通常=付费意愿/需求真实性）>

## 3. Validation Plan

- Core Hypothesis：<一句，来自最大未知>
- Critical Unknown：<...>
- Method：<UserInterview / LandingPage / PreSale / PaidTest / ManualDelivery / SmallPilot / MVP>
- Why This Method：<成本/时间/反馈真实性理由，绑定证据>
- Target User：<画像>　Channel：<渠道（来自证据）>
- Sample Size：<N>（依据：<...>；无依据 → Threshold=Unknown + 校准说明）
- Duration：<...>　Estimated Cost：<现金+时间>

## 4. Experiment

```text
实验动作：<动词+对象+数量>
Offer / Stimulus：<报价/样品/演示>
```

## 5. Success Criteria

- <量化：样本/回复率/兴趣率/付费率…>

## 6. Failure Criteria

- <与 Success 对称的量化阈值>

## 7. Decision Rule（提前定义）

```text
IF Success   → Continue（进入 CUSTOMER_FOUND / FIRST_PAYMENT / BUILDING）
IF Partial   → Modify（改 Hypothesis / Offer / Target / Channel，重新验证，不直接 Build）
IF Failure   → Stop / Revisit / Abandon
```

## 8. Validation Result（用户回填）

```yaml
sample_n: <N>
interested: <N>
trial: <N>
paid: <N>
revenue: <金额>
cost: <金额>
duration_days: <N>
notes: <真实原话/截图>
```

### 事实 / 推断 / 未知

```text
Observed：<...>
Inference：<...>
Unknown：<...>
```

## 9. Updated Assessment（Re-evaluation，按 v4-validation §9 规则重算）

- Updated Coverage：<NN>%（更新维度：<...>）
- Updated Score：<NN>/100（计算式：<...>）
- Updated Confidence：<High/Medium/Low>（<score>）
- Updated Decision：<RECOMMENDED / POTENTIAL / NOT_RECOMMENDED>　+ 状态推进：<VALIDATING→VALIDATED/REVISE/...>
- Reality note：<"基于真实验证证据重算"；哪些是 Observed、哪些仍 Unknown>

## 10. Next Action

- <Continue / Modify / Stop 的下一步，动词开头、可量化>


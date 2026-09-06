# Opportunity Report V3 机会决策报告（v3.1.0）

> V3 最终出口：Evidence → Score → Decision → MVP → Action 五段汇总，结论先行，10 秒看懂。
> 方法编排见 `references/v3-overview.md`；渲染规范见 `references/ui-rendering-spec.md`。

```
┌──────────────────────────────┐
│       MARKET SCOUT V3        │
├──────────────────────────────┤
│ Opportunity Score            │
│         <NN>/100             │
│ Decision: <RECOMMENDED/...>  │
├──────────────────────────────┤
│ Market Evidence              │
│ 真实市场信号                  │
├──────────────────────────────┤
│ Pain Point                   │
│ 核心痛点                     │
├──────────────────────────────┤
│ Competition                  │
│ 竞品与市场空缺                │
├──────────────────────────────┤
│ MVP Blueprint                │
│ 第一版应该怎么做              │
├──────────────────────────────┤
│ Action Plan                  │
│ 下一步应该做什么              │
└──────────────────────────────┘
```

> **🟢 RECOMMENDED 值得继续做 / 🟡 POTENTIAL 有机会但需先验证 / 🔴 NOT_RECOMMENDED 不建议投入**｜机会评分 **<NN>/100**｜Confidence **<High/Medium/Low>**｜Coverage **<NN>%**｜Hard Gates **<PASS/CEILING/FAIL>**｜Opportunity **<MS-###>**
> 一句话结论：<...>

`FIND ✅ → VALIDATE ✅ → EVIDENCE ✅ → SCORING ✅ → DECISION ✅ → MVP ✅ → ACTION ✅`
（进行中 🔄 / 待开始 ⏳ / 有降级或证据不足 ⚠️）

## 1. Market Evidence 市场证据（Evidence / Inference / Unknown）

| 结论 | 状态 | 来源 |
|---|---|---|
| | | |

证据充分度：<Sufficient / Partial / Insufficient>　缺：<...>

## 2. Pain Point 核心痛点

- <痛点>（绑定证据）
- 不解决的损失：<量化>
- 现有方案与不满：<...>

## 3. Competition 竞品与市场空缺

- 竞争格局：<空白/分散/头部/巨头>
- 主要竞品与缺点：<...>
- 切入空间：<四问结论 + 切入点 + 复制难度>

## 4. Opportunity Score 机会评分

| 维度 | 分 | 权重 | 一句话理由 |
|---|---|---|---|
| Demand 需求强度 | | | |
| Pain 痛点强度 | | | |
| Competition 竞争与切入空间 | | | |
| Monetization 变现潜力 | | | |
| Buildability 开发可行性 | | | |
| Distribution 获客难度 | | | |
| AI Advantage AI 优势 | | | |

```text
计算式：= ... = <NN>/100
```

最强两项 / 最弱两项 + 红旗检查（详见 `templates/v3-score-card.md`）

## 4A. Confidence / Evidence Coverage / Hard Gates（v3.1）

- **Confidence**：<High/Medium/Low>（score <NN>）——限制因素：<...>
- **Evidence Coverage**：overall <NN>%（计算式：<...>）；critical_gaps：<...>
- **Hard Gates**：G1-G5 <PASS/FAIL>，C1-C4 <命中/未命中>，Red Flags <无/R#>
- 解释：Score=<NN> 表示<机会本身>；Confidence=<...> 表示<判断可靠性>；两者独立的含义：<一句说明>

## 5. MVP Blueprint 第一版应该怎么做

9 字段表 + MVP 五项 + 最小验证实验（详见 `templates/v3-mvp-card.md`）

## 6. Action Plan 下一步应该做什么（Evidence-driven，v3.1）

Evidence Basis：<target_user / channel / payment_signal / unknowns / hard_gates>
步骤表 + 今天做什么（动词+对象+数量+成功标准）+ 第一笔钱路径（详见 `templates/v3-action-plan-card.md`；每步必须有具体 Fallback）

## 最终判定

- <Decision> + 第一步行动（今天做什么）
- 置信度：<高/中/低>　开放问题：<...>

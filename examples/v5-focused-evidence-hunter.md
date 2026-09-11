# V5 聚焦模式示例：独立 Evidence Hunter（数据为示意）

> 演示 Focused Mode 与独立调用：用户点名只要证据，Main 只派 Evidence Hunter，不跑完整流程。
> 同时演示：已有 Problem 时如何跳过 Idea Observer 与 Problem Scout（中途进入的补位规则）。

## 用户输入

“这个想法是给小微企业做轻量财务对账工具。我已经确认了目标用户（月流水 50 万以下的个体户），现在帮我找这个问题的真实证据：有没有人在抱怨、现在怎么解决、有没有人付费。”

## 路由日志（Main）

    state_detected: PROBLEM（用户已给出明确问题定义）
    mode: FOCUSED → Evidence Hunter
    补位检查: problem 已齐，无需 Idea Observer / Problem Scout
    dispatch: Evidence Hunter

## Evidence Hunter 执行（PROBLEM → EVIDENCE）

### 1. Problem Search（有人遇到这个问题？）

    - 找到多条真实抱怨：“个体户对账全靠 Excel 手工”“月底对不上账熬夜重算”（来源：公开讨论帖，证据等级 B）
    - 无来源的推测一律未使用

### 2. Solution Search（现在怎么解决？）

    - 现有方案：代账公司/财务外包（价格区间一致）、Excel 模板（免费但费时）、进销存软件（功能重）
    - 结论：有方案，但轻量自助档存在空白

### 3. Payment Search（有没有人为类似结果付钱？）

    - 代账服务有明确标价与成交记录（付费行为确认，来源 2 个独立渠道）
    - 未发现“轻量对账工具”的现成付费市场 → 记入 Unknown

### 4. 证据链与覆盖度

    coverage: problem 80 / solution 65 / payment 70 / competition 60 / distribution 50 / buildability 75
    overall_coverage: 67 | critical_gaps: [distribution]
    Evidence Insufficient: 无（三类证据齐备，distribution 维度偏低）

## 输出（只交付证据，不下决策）

    - 证据链 5 条（每条含 Evidence/Source/Type/Confidence/Proves/NotProves）
    - 三态看板：Evidence 8 条 / Inference 3 条 / Unknown 2 条
    - 建议：下一步由 Opportunity Scout 做需求与切入空间分析（未执行）

## 自检

- [x] 未重跑 IDEA / PROBLEM（用户已有）
- [x] 未编造来源与价格
- [x] 没有跨越 Specialist 边界下决策

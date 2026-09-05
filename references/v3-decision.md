# V3 Decision — 机会决策（v3.0.0 新增）

> Opportunity Score 之后，必须给出一个明确结论。三档即可：
> **Recommended 值得继续做 / Potential 有机会但需先验证 / Not Recommended 不建议投入**。
> 产出 `templates/v3-decision-card.md`；这是 V3 主流程第 7 步 DECISION 的方法定义。

## 1. 三档结论

| 代码 | 含义 | 对用户的话 |
|---|---|---|
| RECOMMENDED | 值得继续做 | 可以投入，按 MVP Blueprint 和 Action Plan 行动 |
| POTENTIAL | 存在机会，但还需要验证 | 先做最小验证实验，达标再全力投入 |
| NOT_RECOMMENDED | 当前不建议投入 | 停止，按停止三要素与重启条件处理 |

与 V2 Verdict 的映射（统一口径，不破坏 V2）：

| V2 Verdict（EVALUATE） | V3 Decision（最终） | 关系 |
|---|---|---|
| GO | RECOMMENDED | 一致 |
| VALIDATE_FIRST | POTENTIAL | 一致 |
| NO_GO | NOT_RECOMMENDED | 一致 |

V2 阶段卡里保留 V2 代码；V3 最终报告统一用 V3 代码展示，避免一张报告出现两套结论词。

## 2. 判定规则（总分 + 门槛 + 红旗 + 证据充分度共同决定）

| Decision | 判定条件（须同时满足） |
|---|---|
| RECOMMENDED | Score ≥ 75；且 Demand ≥ 70；且 Pain ≥ 60；且 Monetization ≥ 60；且无致命红旗；且证据充分度 ≥ Partial（付费信号至少 Inference 并有明确验证路径） |
| POTENTIAL | 55 ≤ Score < 75；或 Score ≥ 75 但关键假设未验证（付费/切入空间为 Unknown 或仅 Inference）；或证据充分度 = Insufficient 但基础问题证据存在 |
| NOT_RECOMMENDED | Score < 55；或触发任一致命红旗（`v3-scoring.md` §4）；或连"问题是否真实存在"都没有证据 |

- 分数只是决策的一部分：哪怕 86 分，付费/切入空间是 Unknown，也只能 POTENTIAL。
- 红旗优先于分数：分数再高，触发红旗 → NOT_RECOMMENDED。
- 低可信维度（v3-scoring §2.4）视为未验证：参与 POTENTIAL 判定。
- 停止是一种高质量交付：禁止为了照顾情绪硬给 POTENTIAL/RECOMMENDED（沿用 v1.1 停止机制）。

## 3. Decision 必须解释原因（Why，强制）

每个 Decision 必须带编号 Why 列表，每条一句话、绑定证据三态：

```text
Decision: RECOMMENDED
Why:
1. 痛点明显 —— 用户每周花 4-6 小时做低价值重复劳动（Evidence，3 个独立来源）。
2. 需求证据较多 —— 同类求助在多个平台重复出现（Evidence）。
3. 竞品存在明显缺口 —— 现有方案贵且被用户公开吐槽，切入空间成立（Evidence）。
4. MVP 开发难度低 —— L1 人工+AI 一周内可交付第一单（Inference）。
5. 存在明确的付费路径 —— 相邻品类在售服务报价 2000-5000 元/月（Evidence）。
```

```text
Decision: NOT_RECOMMENDED
Why:
1. 用户痛点较弱 —— 现有免费方案基本够用（Evidence）。
2. 已有竞品解决得比较成熟 —— 头部产品口碑良好（Evidence）。
3. 缺乏明显差异化 —— 未找到可守的切入点（Unknown）。
4. 获客成本可能较高 —— 目标用户分散、本人无触达渠道（Inference）。
```

规则：

- 每条 Why 必须对应 Score 的一个维度/子信号，或对应一条红旗。禁止写与评分无关的客套理由。
- Why 数量 3-6 条；顺序按重要性排。

## 4. 证据不足时的处理（P0，配合 v3-evidence.md）

- 证据充分度 = Insufficient → 输出 `Evidence Insufficient 证据不足` 横幅（`ui-rendering-spec.md` §7.2），并声明：
  1. 目前无法确认什么；
  2. 缺什么证据；
  3. 去哪补（对应三类搜索之一）。
- 若基础问题证据存在 → Decision=POTENTIAL，MVP 暂停，Action Plan 前两步改为"补证据"。
- 若基础问题证据都没有 → Decision=NOT_RECOMMENDED（暂缓投入），重启条件写清。
- 任何情况下禁止编造证据把结论"凑"出来。

## 5. 各档的下一步承诺（Next Commitment）

- RECOMMENDED → 生成完整 MVP Blueprint（`v3-mvp.md` §2）+ Action Plan（`v3-action-plan.md` §3 执行路径）。
- POTENTIAL → Score ≥ 65 时生成"验证版 MVP"（只为验证付费假设的最小交付）；Score < 65 时不生成 MVP，Action Plan 输出验证优先路径（不开发）。
- NOT_RECOMMENDED → 不生成 MVP；输出停止三要素（为什么停 / 哪条证据导致停 / 什么新证据可重启）。

## 6. 输出

- 使用 `templates/v3-decision-card.md`：结论带（Decision+Score+ID）+ Why 列表 + 判定依据 + 下一步承诺。
- 结论必须能在 10 秒内被用户看到（结论先行，`ui-rendering-spec.md` §4.1）。

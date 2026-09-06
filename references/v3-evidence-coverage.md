# V3.1 Evidence Coverage — 证据覆盖度（v3.1.0 新增）

> 解决"这份报告到底研究了多少"：衡量**关键决策问题被有效证据覆盖的程度**，
> 而不是简单数来源数量。产出 `evidence_coverage` 对象，是 Confidence 与 Decision 的输入之一。

## 1. 六个覆盖维度

| 维度 | 该维度要回答的子问题 |
|---|---|
| Problem | 问题是否真实存在？多常见？用户是否主动寻找？ |
| Solution | 用户现在用什么解决？为什么不满？缺口在哪？ |
| Payment | 是否有人为此付钱？价格锚？付费方与拍板权？复购可能？ |
| Competition | 现有方案成熟度？未满足程度？差异化与复制难度？ |
| Distribution | 用户在哪聚集？本人能否触达？获客成本路径？ |
| Buildability | 工作量/现金成本/技术成熟度/单人可否完成？ |

## 2. 单维打分（0-100，五档）

每维按以下规则打分，**档位判定依据 = 独立来源数 × 证据状态 × 子问题覆盖完整性**：

| 分数 | 档位标准 |
|---|---|
| 0-19 | 无有效证据（全部 Unknown / 无来源） |
| 20-39 | 仅 1 个来源，或全部为 Inference |
| 40-59 | 2-3 个来源，含至少 1 个独立 Evidence，但该维度关键子问题仍有缺口 |
| 60-79 | 3+ 个独立 Evidence 来源，覆盖该维度大部分子问题，仍缺 1 项关键子问题 |
| 80-99 | 多独立来源（4+），覆盖该维度全部子问题 |
| 100 | 全覆盖且核心结论可复核一手来源（几乎不给；给 100 必须说明为什么） |

## 3. 来源独立性规则（P0，防刷分）

以下情况**不得**计为多个独立来源：

- 同一新闻/文章被多个网站转载
- 同一帖子/评论被不同平台引用
- 同一份原始数据被多篇文章重复使用
- 同一账号/同一作者在不同平台的内容

处理：

- 无法确认独立性时 → 该来源标 `Unknown / Low confidence`，按 1 个来源计。
- 单维打分前先做去重：先按"原始主体"分组，再数独立组数。
- 发现重复 → 在报告中标注"去重后 N 个独立来源"。

## 4. 总覆盖（可复算）

```text
overall = round( (Problem + Solution + Payment + Competition + Distribution + Buildability) / 6 )
```

示例（对齐 SOP 案例）：avg(90, 60, 30, 80, 50, 85) = 395/6 = 65.8 → **66/100**

每维必须给 status：

| status | 含义 |
|---|---|
| covered | ≥ 70 |
| partial | 40-69 |
| insufficient | < 40 |

## 5. 关键维度（Critical Weight）

- **Payment 与 Problem（需求侧）是关键维度**：需求真实性/付费证据未覆盖时，整体覆盖再高也不能支撑高置信。
- critical_gaps 列出来：任一关键子问题（付费证据/付费方/需求真实性）覆盖 < 60 时：

```yaml
critical_gaps:
  - payment evidence
  - demand verification
```

## 6. 与 Sufficiency / Confidence / Decision 的关系

```text
Evidence Coverage（各维 0-100 + overall）
    ↓ 输入
Confidence 公式（v3-confidence.md）
    ↓ 输入
Hard Gates 触发检查（v3-hard-gates.md：Payment 覆盖 < 30 → Score Ceiling）
    ↓
Decision
```

- Coverage ≠ Confidence：Coverage 80% 但由于缺 Payment（关键维度），Confidence 仍可 Low（v3-confidence 覆盖规则 O1/O2）。
- 证据充分度（v3-evidence §3）是运行期总体判定；Coverage 是它的结构化数字表达，二者必须一致（Insufficient ⇔ 关键维度 insufficient）。

## 7. 每维输出格式

```yaml
evidence_coverage:
  problem:      {status: covered,     score: 90}
  solution:     {status: partial,     score: 60}
  payment:      {status: insufficient, score: 30}
  competition:  {status: covered,     score: 80}
  distribution: {status: partial,     score: 50}
  buildability: {status: covered,     score: 85}
  overall: 66
  critical_gaps: [payment evidence]
```

## 8. 搜索停止规则配合

- Evidence Coverage 不改变 V2 的 Research Stop Rule：关键证据足够 + 边际价值低 + 可低成本验证 → 停止搜索进入 Action。
- Coverage 低 ≠ 继续无限搜索；先标出缺什么，把"补证据"作为 Action 的第一步。


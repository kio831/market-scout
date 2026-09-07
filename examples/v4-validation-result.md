# 示例：Validation Result 验证结果回填（v4.0.0）

> ⚠️ 演示数据。展示用户把真实验证结果交回后，系统如何读取与分级（只读，暂不重算）。

**Opportunity ID**：MS-301　**Validation Status**：succeeded（按既定标准判定）

## 用户回填

```yaml
validation_result:
  opportunity_id: MS-301
  sample_n: 20
  interested: 8
  trial: 3
  paid: 2
  revenue: 398
  cost: 0
  duration_days: 7
  notes: "2 家付了 199 首月；3 家说先把样品发完再定"
```

## 事实 / 推断 / 未知（Evidence 原则）

```text
Observed（事实）:
  - 20 家中 8 家明确表达需求
  - 3 家试用样品
  - 2 家真实付款（¥199 × 2，共 ¥398）

Inference（推断）:
  - 存在一定付费意愿；首次转化率 10% 达到预设成功线
  - 但 2 家是小样本，不能推断"整个市场都愿意付"

Unknown（未知）:
  - 是否可规模化获客（20 家名单来自 1 个城市的 1 个品类）
  - 留存/续费如何（尚未经过第二个月）
  - 换品类后付费率是否一致
```

## 判定（按计划中预定义的 Success / Failure 标准）

- Success Criteria：≥5 家明确需求（8 ✓）且 ≥2 家真实付款（2 ✓）
- Failure Criteria：<2 家付款（未触发）
- **结论：Success** → Decision Rule 规定 → Continue

## 输入校验（§8.2）

- interested(8) ≤ sample_n(20) ✓；paid(2) ≤ trial(3) ✓；revenue(398) ≈ 199×2 ✓
- 字段齐全，无冲突。

## 教学点

- **8 人感兴趣 ≠ 市场需求已验证**；只有 2 笔真实付款是 Observed，其余为 Inference/Unknown。
- 结果分级写进卡片，Re-evaluation 只基于 Observed 重算（见 examples/v4-re-evaluation.md）。


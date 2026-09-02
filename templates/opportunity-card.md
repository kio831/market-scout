# Opportunity Card 模板（v1.1）

> 用于把 Problem Card 升级为"值得验证的机会"：评分（绑定证据）+ 证据链 + 竞争 + 状态 + 决策。
> 评分维度与 Payment 分档见 `references/problem-framework.md` §4；状态机见 `references/opportunity-state-machine.md`。

---

## 机会卡片

**Opportunity ID**：<MS-###>（一旦分配固定不变）

**机会名称**：<一句话>

**问题**：<来自 Problem Card 的问题表述>

**用户**：<具体画像>

**当前状态**：<HYPOTHESIS / DEMAND_CONFIRMED / MARKET_CONFIRMED / PAYMENT_VALIDATION / CUSTOMER_FOUND / FIRST_PAYMENT / REPEATED_DELIVERY / STANDARDIZED / AUTOMATED / PRODUCTIZED>
（注意：FIRST_PAYMENT 必须实际收到真实付款；"愿意购买/愿意尝试/报价意愿"最多到 CUSTOMER_FOUND）

**证据等级**：A / B / C　**来源**：<链接/原文>

### 证据链（Problem / Solution / Payment 三类）

| 搜索类型 | 证据摘要 | 来源 | 证明什么 | 不能证明什么 | 置信度 |
|---|---|---|---|---|---|
| Problem |  |  |  |  |  |
| Solution |  |  |  |  |  |
| Payment |  |  |  |  |  |

### 评分（1-10，每分必带理由+证据+不确定性）

| 维度 | 分 | 评分理由 | 对应证据 / 或标注【无直接证据】 | 当前不确定性 |
|---|---|---|---|---|
| Pain 痛苦 |  |  |  |  |
| Frequency 频率 |  |  |  |  |
| Payment 付费 |  |  |  |  |
| Market 市场 |  |  |  |  |
| AI Leverage AI杠杆 |  |  |  |  |
| Feasibility 可执行 |  |  |  |  |
| MVP Speed 速度 |  |  |  |  |
| Competition 竞争（越低越好） |  |  |  |  |

### 四问
- 为什么值得继续？
- 最大的不确定性是什么？
- 缺什么证据？
- 下一步最应该验证什么（只做一件事）？

### 竞争与付费速览
- 已有工具/SaaS/人工服务/免费方案：<有/无 + 例子>
- 用户为什么不用：<贵/难用/不知道/不信任>
- 当前价格锚：<有则写，无则"未找到"（标 C）>
- 用户真正购买的是什么：<结果/时间/效率/成本降低/…>

### 状态机推进（见 `references/opportunity-state-machine.md`）
- 当前瓶颈：<当前状态 → 下一状态缺什么证据>
- 只推进这件事：<一个动作>

### 初步判断
🟢 值得验证 / 🟡 潜在机会，需更多证据 / 🔴 不建议继续
- 若 🟡：<继续验证的最小下一步>
- 若 🔴：<停止原因 + 哪个证据导致停止 + 什么新证据可重启>

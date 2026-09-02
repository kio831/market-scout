# Opportunity State Machine — 机会状态机（P1）

本文件定义如何为每个机会建立唯一 ID、跟踪状态、推进瓶颈、跨会话续研。目的是防止"反复研究同一个机会却永远不推进"。

> **状态代码统一使用完整英文状态名**（如 DEMAND_CONFIRMED），不再使用 C/B/A 等字母。
> 这是为了与**证据等级 A/B/C**（A=已验证需求 / B=潜在需求 / C=假设需求，见 `problem-framework.md` §3）明确区分，避免歧义。证据等级不随本次修改变化。

## 1. 唯一标识

每个值得跟踪的机会分配唯一 ID：`MS-###`（如 MS-001、MS-002）。
ID 一旦分配即固定，后续所有会话/报告/卡片都用它引用，避免重复建卡。

## 2. 状态机

```
HYPOTHESIS（假设）
  ↓
DEMAND_CONFIRMED（已有需求证据）
  ↓
MARKET_CONFIRMED（已有市场/付费证据）
  ↓
PAYMENT_VALIDATION（已进行付费验证）
  ↓
CUSTOMER_FOUND（已找到真实用户）
  ↓
FIRST_PAYMENT（第一笔钱）
  ↓
REPEATED_DELIVERY（已重复交付）
  ↓
STANDARDIZED（已标准化）
  ↓
AUTOMATED（已自动化）
  ↓
PRODUCTIZED（已产品化）
```

**状态一律用完整英文状态名显示**，例如显示为 `DEMAND_CONFIRMED`、`FIRST_PAYMENT`，不用字母缩写，避免与证据等级 A/B/C 冲突。

## 3. 每个状态的判定标准与推进条件

| 状态 | 判定标准 | 推进到下一状态的证据 |
|---|---|---|
| HYPOTHESIS | 仅有观察/猜测，无足够来源 | 出现 2+ 个独立来源的同类问题/求助 → DEMAND_CONFIRMED |
| DEMAND_CONFIRMED | 有重复需求、抱怨或求助 | 出现付费迹象（在售服务/询价/成交/公开价格）→ MARKET_CONFIRMED |
| MARKET_CONFIRMED | 存在类似产品/服务收费或公开价格 | 开始面向真实用户做报价/测试 → PAYMENT_VALIDATION |
| PAYMENT_VALIDATION | 已向真实用户展示并尝试收费 | 确认存在明确需求的真实潜在客户 → CUSTOMER_FOUND |
| CUSTOMER_FOUND | 已找到**明确存在需求的真实潜在客户** | **实际收到真实付款** → FIRST_PAYMENT |
| FIRST_PAYMENT | **已实际收到真实付款**（转账/定金/成交） | 再次交付并收款 → REPEATED_DELIVERY |
| REPEATED_DELIVERY | 交付 2+ 次并有复购/续订 | 固定交付模板与流程 → STANDARDIZED |
| STANDARDIZED | 交付流程/报价/模板已固定 | 把重复环节脚本化 → AUTOMATED |
| AUTOMATED | 核心重复环节已自动化，人工只质检 | 多用户在线产品/规模运营 → PRODUCTIZED |
| PRODUCTIZED | 形成可复用产品/服务 | —（终点，转滚动寻找新机会） |

### CUSTOMER_FOUND 与 FIRST_PAYMENT 的严格区分（重要）

- **CUSTOMER_FOUND（已找到真实用户）**：代表已经找到明确存在需求的真实潜在客户。"愿意购买 / 愿意尝试 / 报价意愿"等口头信号**最多推进到此状态**。
- **FIRST_PAYMENT（第一笔钱）**：**必须实际收到真实付款**（转账、定金、成交款）才能进入。**不得因为"用户说愿意付钱"就把状态推进到 FIRST_PAYMENT。**
- 只有"用户表达了付费意愿" → 停留在 CUSTOMER_FOUND（验证信号），继续推进到真实收款。

## 4. 瓶颈推进原则（核心纪律）

每次继续研究同一个机会时，**必须**：

1. **读取之前的证据**（沿用原 Opportunity ID 的卡片，不新建）。
2. **不重复无意义搜索**（已确认的结论不重查）。
3. **明确当前状态**。
4. **明确缺失的下一步证据**（当前状态 → 下一状态缺什么）。
5. **只推进当前瓶颈**，不横向扩散。

**示例**：某机会已到 DEMAND_CONFIRMED（已有需求证据）但无付费证据。
- ❌ 错误：继续研究 AI 技术、继续找新问题、再搜一百次"有没有人需要"。
- ✅ 正确：只做一件事——"寻找 5 个潜在用户 → 展示方案 → 报价 → 获取真实反馈/购买意愿"，把状态推向 MARKET_CONFIRMED / PAYMENT_VALIDATION。

## 5. 跨会话续研协议

当用户再次提到某个之前研究过的机会（如"上次那个打印店的事，我准备做了"）：
- 输出当前快照：Opportunity ID、当前状态、已确认证据摘要、当前瓶颈。
- 然后**只推进瓶颈**，不要从零重新研究。

## 6. 研究阶段完成判定

当以下全部成立时，状态推进到"可以进入 Execution"：
- 有真实问题 ✅
- 有重复需求 ✅
- 有类似服务收费 ✅
- AI 存在明显杠杆 ✅
- 用户可触达 ✅
- 可以低成本完成 MVP ✅

此时输出【研究阶段完成】，下一步是【开始真实用户验证】（进入 Execution Mode），**不是继续搜索**。

## 7. 状态机与证据链的关系

- 状态**只能**由证据链支撑的证据推进（见 `evidence-chain.md`）。
- 没有新证据 → 状态不得推进；状态停滞本身也是信号：缺证据，去补那一类证据（Problem / Solution / Payment）。
- FIRST_PAYMENT 必须由"真实付款"这类证据支撑，口头付费意愿不足以推进到该状态。

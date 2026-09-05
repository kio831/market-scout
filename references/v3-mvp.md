# V3 MVP Blueprint — MVP 方案（v3.0.0 新增）

> 把"值得做"的机会转成"第一版到底做什么"。方法完全复用 V2 BLUEPRINT
> （产品形态 Level 1-5、MoSCoW、MVP 五项、技术方向、最小验证实验），
> 输出统一为 9 个字段，并强制遵守"单人最快验证"原则。产出 `templates/v3-mvp-card.md`。

## 1. 触发条件

| 条件 | 输出 |
|---|---|
| Decision = RECOMMENDED | 完整 MVP Blueprint（产品方案版） |
| Decision = POTENTIAL 且 Score ≥ 65 | 验证版 MVP（只为验证付费假设的最小交付，明确标注"验证版"） |
| POTENTIAL 且 Score < 65 / NOT_RECOMMENDED | 不生成 MVP；输出补证据/停止说明 |

## 2. 九个输出字段（模板 templates/v3-mvp-card.md）

| # | 字段 | 必须写什么 |
|---|---|---|
| 1 | Product 产品定位 | 一句话"我帮【谁】在【场景】达成【可感知结果】"，卖结果不卖 AI |
| 2 | Target User 目标用户 | 具体可触达的画像（身份+场景+聚集渠道），不写"所有人" |
| 3 | Core Problem 核心问题 | 用户真正要解决的问题（引用 VALIDATE 痛点与付费理由链） |
| 4 | Core Value 核心价值 | 用户获得的结果（时间/钱/风险/增长），尽量量化 |
| 5 | Must Have 第一版必须有 | ≤3 项，每项对应一个付费理由；去掉它用户还会付钱的功能一律降级 |
| 6 | Nice to Have 以后再做 | 重要但第一版可人工替代/延后的项 |
| 7 | Do Not Build 当前不要做 | 黑名单（账号体系/后台/App/多平台/自动化同步……按项目写） |
| 8 | Build Difficulty 开发难度 | 工作量/现金成本/周期 + 当前应停的 Level（1-5） |
| 9 | Recommended Stack 技术方向 | 无代码优先/轻脚本/简单前端/完整产品 + 理由 + 最大缺点 + 替代方案 |

差异化切入点写进 Product 与 Core Value；不要停在口号（`project-blueprint.md` §7）。

## 3. 范围控制铁律（P0）

- **只回答一个问题："如果只有一个人开发，最快怎么验证这个想法？"**
- 禁止直接设计"需要数月开发的完整 SaaS"。
- 默认产品形态 = L1（人工+AI 代做/Concierge），除非已有付费证据支持更高级（`ai-solution-patterns.md` §1）。
- 没有真实付费用户前，禁止推荐 L4/L5（沿用 v1.1 铁律：先卖结果，再产品化）。
- 若 L1 无需写代码 → 明确写【当前不需要开发】，这是合格结论不是缺项。
- MVP 五项（第一版做什么/不做什么/验证什么/什么结果出现后继续/什么结果出现后放弃）沿用 `project-blueprint.md` §4，逐项填写，缺一不可。
- "验证版 MVP"额外标注：本版只为验证付费假设，验证通过前不做产品化。

## 4. 最小验证实验（配合 MONETIZE 的无产品验证）

```text
验证假设：一句话（优先验证"是否有人为结果付钱"）
实验形式：Concierge / 落地页冒烟 / 预售定金 / Fake Door / 用户访谈 / 样品试交付
目标对象：几个、什么画像、从哪来
成功标准：量化阈值
失败转向：不达标时的具体调整规则
```

- 验证方案回答"要不要做"，MVP 回答"第一版做成什么样"（`project-blueprint.md` §6）。
- 能用不开发的验证方式拿到付费证据的，先拿钱再开发（`monetization-gtm.md` §7）。

## 5. 与 V2 BLUEPRINT 的关系

- 方法完全复用 `project-blueprint.md`：Level 1-5 判定、MoSCoW、MVP 五项、技术方向、最小验证、差异化落地。
- V3 只新增"9 字段统一输出 + 触发条件 + 单人最快验证铁律"，不重定义任何 V2 方法。
- 产出同时满足 V2 的 Project Blueprint Card 与 V3 的 MVP 卡；技术方向的生产级要求沿用 `ai-solution-patterns.md` §3。

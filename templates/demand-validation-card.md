# Demand Validation Card 需求验证卡模板（v2.0，流水线阶段 VALIDATE）

> 阶段：FIND → **VALIDATE** → EVALUATE → BLUEPRINT → MONETIZE。
> 方法见 `references/demand-validation.md`；证据链/等级规则见 `references/evidence-chain.md`、`references/problem-framework.md`。
> 每个结论必须可追溯到 Evidence Card；无证据处标【证据不足/假设】，禁止编造。

---

# 需求验证（Demand Validation）

`FIND ✅ → VALIDATE 🔄 → EVALUATE ⏳ → BLUEPRINT ⏳ → MONETIZE ⏳`

**Opportunity ID**：<MS-###>　**Pipeline Stage**：VALIDATE　**日期**：<YYYY-MM-DD>
**机会/问题一句话**：<>
**取证方式**：<实时搜索 / 浏览器 / 用户材料 / 假设分析（无搜索能力时必须声明）>　**失败与降级记录**：<>

> **🟡 需求存在但付费未验证 VALIDATE_FIRST**　|　需求强度 **<N/10>**　`████░░░░░░ N/10`　|　Opportunity **<MS-###>**
> 一句话结论：<>（需求结论三选一：✅ 真实需求已验证 / 🟡 需求存在但付费未验证 / ❌ 伪需求·弱需求）

## 1. 用户痛点（Pain Points）
- 核心痛点（问题十分类标签）：<>
- 不解决的后果（尽量量化：时间/钱/风险/情绪）：<>
- 对应证据（Evidence ID + 来源 + 置信度）：<>

## 2. 目标用户（Target Users，禁止"所有人"）
| 层级 | 画像（身份+场景+数量级） | 痛/频 | 在哪可触达 | 证据/标注 |
|---|---|---|---|---|
| 核心用户 Core |  |  |  |  |
| 扩展用户 Adjacent |  |  |  |  |
| 非用户 Non-users（明确排除） |  | — | — |  |

> 自检：如果只能服务 10 个人，是哪 10 个？答不出 = 本节未完成。

## 3. 需求强度（Demand Strength，6 信号，每信号四要素）
| 信号 | 分(0-10) | 理由 | 对应证据 /【无直接证据】 | 不确定性 |
|---|---|---|---|---|
| S1 痛点严重度 |  |  |  |  |
| S2 发生频率 |  |  |  |  |
| S3 主动寻找 |  |  |  |  |
| S4 现有预算 |  |  |  |  |
| S5 不满程度 |  |  |  |  |
| S6 增长趋势 |  |  |  |  |

- **均分**：<N/10>（S1/S2/S3 任一 ≤3 时总分上限 5）
- **最弱信号**：<>　**最强信号**：<>

## 4. 当前解决方案与替代成本（Current Alternatives）
| 替代方式 | 现在怎么做 | 时间成本 | 金钱成本 | 技能门槛 | 明确不满点 |
|---|---|---|---|---|---|
| 纯人工硬扛 |  |  |  |  |  |
| 免费/通用工具 |  |  |  |  |  |
| 付费工具/SaaS |  |  |  |  |  |
| 外包/人工服务 |  |  |  |  |  |
| 干脆不做 |  |  |  |  |  |

- 用户真正购买的是（结果/时间/效率/成本降低/…）：<>
- **替代成本结论（后续定价锚，传给 MONETIZE）**：<>

## 5. 付费理由链（Willingness-to-Pay / JTBD Chain）
1. Job to be Done（要完成的具体任务，要结果不要功能）：<>
2. Current Cost（现在花多少时间/钱，证据）：<>
3. Switch Trigger（什么事件逼他现在解决）：<>
4. Pay Reason（为什么为你的方案而非继续用替代方案付钱）：<>
5. Pay Ability & Authority（有没有预算、能否拍板；使用者≠付费方时写清）：<>

- 链条通到第几环：<>　**红旗：使用者无付费权且无买单方？是/否**

## 6. 需求证据可信度（Evidence & Confidence）
| 结论 | 证据/来源 | 证据类型 | 置信度 | 等级 A/B/C | 缺口 |
|---|---|---|---|---|---|
| 痛点真实 |  |  |  |  |  |
| 重复发生 |  |  |  |  |  |
| 主动找方案 |  |  |  |  |  |
| 已有替代预算 |  |  |  |  |  |
| 愿为本方案付费 |  |  |  |  |  |

### 证据链分层（事实/推断/假设，不混层）
- 观察（事实）：<>
- 推断：<>
- 假设（待验证）：<>

## 7. 下一步（只做一件事）

**👉 下一步行动**：<>（动词开头、可量化、今天能做；把需求结论再推进一步的唯一动作）

[📊 进入 EVALUATE](templates/project-evaluation-card.md)　[🔬 付费验证实验](references/monetization-gtm.md#7-不开发产品的验证方式no-build-validation)　[⚠️ 停止机制](references/payment-validation.md#6-停止机制stop-conditions)

- 若 ✅ 真实需求已验证：直接进入 EVALUATE。
- 若 🟡 付费未验证：可进 EVALUATE，但付费假设必须在 BLUEPRINT/MONETIZE 用最小实验验证。
- 若 ❌ 伪/弱需求：停止三要素——为什么停 / 哪个证据导致 / 什么新证据可重启。

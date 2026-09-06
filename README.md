<div align="center">

# 🔭 Market Scout

**AI Market Opportunity Discovery & Validation Skill**
**AI 市场机会发现 · 需求验证 · 项目评估 · 商业化决策 Skill**

> 把一个模糊的想法，变成有证据支撑的判断，和可以直接执行的下一步。
> Turn a vague idea into an evidence-backed decision and actionable next steps.

[![Version](https://img.shields.io/badge/version-v3.1.0-blue)](./CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)
![Type](https://img.shields.io/badge/type-Agent%20Skill-orange)
![Platform](https://img.shields.io/badge/platform-Any%20Markdown%20Agent-lightgrey)
![Status](https://img.shields.io/badge/status-Evidence--driven-brightgreen)

### FIND → PROVE → SCORE → DECIDE → ACT → LEARN

**V3.1.0 · Evidence-driven Decision System（Determinism Layer）**

[⬇ 下载 V3.1.0](./releases/market-scout-v3.1.0.zip) · [安装](#-安装) · [快速开始](#-快速开始) · [版本演进](#-版本演进) · [V3.1 深度](#-v31--从分析到可靠决策) · [项目结构](#-项目结构)

*English / 中文 — 中英结合，关键概念双语呈现*

</div>

---

## 这是什么 / What is it?

> **Market Scout is an AI-powered market opportunity discovery and validation Skill that helps turn vague ideas into evidence-backed decisions and actionable next steps.**
>
> **Market Scout 是一个 AI 市场机会发现与验证 Skill：把模糊的想法转化为有证据支撑的判断，并给出可以直接执行的下一步。**

它不是「AI 创业点子生成器」，不会凭空给你编项目。它从**真实问题与真实市场证据**出发，走完一条完整的决策链路：

```
一个想法 → 市场研究 → Evidence → Score → Decision → MVP / Validation → Action
```

## 适合谁 / Who is it for?

| | |
|---|---|
| AI 创业者 / AI Builder | 有想法，但不确定值不值得投入、第一步做什么 |
| 独立开发者 / Indie Hacker | 想验证一个产品想法，而不是盲目开工 |
| 产品经理 / 创业者 | 需要判断「这个需求是真的吗？有人会付钱吗？」 |
| 想验证想法的人 | 一个现象、一条评论、一个视频，都能变成可验证的机会 |

## 它能做什么 / What does it do?

- **市场研究**：三类搜索（问题 / 现有方案 / 付费行为）交叉验证，用真实证据代替直觉
- **需求验证**：需求强度 6 信号 + 证据三态（Evidence / Inference / Unknown），拒绝自我感动
- **机会评估**：7 维加权 0-100 机会评分（计算式可手工复算）
- **决策与行动**：三档决策（值得做 / 先验证 / 不建议投入）+ 证据驱动的分步行动计划
- **最后回答一个问题**：*这件事，到底值不值得做？今天先做什么？*

---

## 🗺 版本演进 / Version Evolution

`BT`
V1    Market Discovery        发现机会
 ↓
V1.1  Problem Discovery       深化问题
 ↓
V2    Structured Evaluation   结构化评估
 ↓
V3    Evidence-driven Pipeline 完整决策 Pipeline
 ↓
V3.1  Reliable Decision System 提高可靠性（当前版本 ⭐）
`BT`

`BT`mermaid
flowchart TB
    V1["V1 · Market Discovery<br/>发现机会"] --> V11["V1.1 · Problem Discovery<br/>深化问题"]
    V11 --> V2["V2 · Structured Evaluation<br/>结构化评估"]
    V2 --> V3["V3 · Evidence-driven Pipeline<br/>完整决策 Pipeline"]
    V3 ==> V31["V3.1 · Reliable Decision System<br/>可靠性强化（当前版本）"]
`BT`

> 历史版本解释「Market Scout 是怎么成长起来的」；**V3.1 是本次发布的核心。**

### V1 — Market Discovery（发现机会）

> **从模糊想法中发现市场机会。** 解决：我有什么想法？这个问题有没有市场？谁可能需要？

- Problem Discovery · Market Discovery · Pain Point Discovery · Opportunity Discovery
- 从 **Find** 出发：市场扫描、Problem Card、三类搜索（Problem / Solution / Payment）、Evidence Chain
- Market Scan 市场扫描、Problem Card、三类搜索（Problem / Solution / Payment）、Evidence Chain

### V1.1 — Problem Discovery（深化问题）

> V1.1 强化问题分析与机会识别，让输出从「想法」走向「问题」。

- Problem Structure · Pain Analysis · User Context · Opportunity Signals
- Quick / Research / Execution 三模式、Opportunity 状态机、停止机制

### V2 — Structured Evaluation（结构化评估）

> **从「发现机会」走向「评估机会」。** V2 回答的不只是「有没有机会」，而是「值不值得继续投入」。

- **Demand**（需求强度 6 信号 + JTBD 付费理由链）· **Market**（替代成本 / 定价锚）
- **Competition**（竞争格局与差异化）· **AI Feasibility** · **Personal Fit** · **Risk**
- Opportunity Evaluation · Scoring · Decision Cards · Pipeline
- V2 四阶段：Validate / Evaluate / Blueprint / Monetize

### V3 — Evidence-driven Decision Pipeline（完整决策流水线）

> **Market Scout 不再只是帮你找创业机会，而是建立了一条从市场发现到决策再到 MVP 的完整 Pipeline。**

`BT`
DISCOVERY → VALIDATION → EVIDENCE → COMPETITION → SCORING → DECISION → MVP → ACTION
`BT`

- **Evidence**：证据三态 Evidence / Inference / Unknown，每分绑定证据
- **Opportunity Score**：7 维加权 0-100，计算式可复算
- **Decision Code**：🟢 RECOMMENDED / 🟡 POTENTIAL / 🔴 NOT_RECOMMENDED
- **MVP Blueprint**：9 字段最小方案（默认 L1 人工 + AI 先卖结果）
- **Action Plan**：按机会类型动态生成
- Runtime / State · Research Stop Rule · Failure / Fallback

---

## ✨ V3.1 — 从分析到可靠决策

### V3.1 does not add another stage. It makes the existing decision pipeline more reliable.
### V3.1 没有增加新的决策阶段，而是在 EVIDENCE → SCORING → DECISION → ACTION 之间增加五层约束。

> 核心认知：**「机会评分高」不等于「应该推荐」。** Score 表示机会本身有多好；Confidence 表示我们有多确定；Hard Gates 保证关键短板不被总分掩盖。

### V3.1 Architecture

`BT`mermaid
flowchart TB
    I["INPUT<br/>Idea / Problem"] --> E["EVIDENCE<br/>Evidence / Inference / Unknown"]
    E --> C["Evidence Coverage<br/>6 Dimensions"]
    C --> R["Score Rubric<br/>26 Sub-signals"]
    R --> S["Opportunity Score<br/>0-100"]
    S --> CC["Confidence"]
    S --> G["Hard Gates"]
    CC --> D["DECISION<br/>Recommended / Potential / Not Recommended"]
    G --> D
    D --> A["Evidence-driven Action"]
    A --> L["LEARN"]
`BT`

### Before vs V3.1（为什么值得升级）

**Before（V3）**

`BT`
Idea → Research → Score → Decision → MVP
`BT`

问题：为什么是这个分数？这个判断有多可靠？关键证据够不够？总分是否掩盖短板？下一步具体做什么？

**V3.1**

`BT`
Idea → Evidence → Coverage → Rubric → Score → Confidence → Hard Gates → Decision → Evidence-driven Action → Learn
`BT`

> **V3.1 is not more complicated for the sake of complexity. It is more constrained where decisions matter.**
> **V3.1 不是为了复杂而复杂，而是在决策真正关键的地方加约束。**

### 五大核心能力 / Five Capabilities

---

#### 01 · Score Rubric 评分细则

**Why** — 为什么是 7 分，而不是 8 分？

`BT`
Before:  Evidence → LLM 感觉 → Score
V3.1:    Evidence → Rubric → Score
`BT`

- 26 个子信号（D1-D4 / P1-P3 / C1-C4 / M1-M4 / B1-B4 / D1-D4 / A1-A4）
- 每个子信号 **5 个可观察档位**（1-2 / 3-4 / 5-6 / 7-8 / 9-10），档位判据各不相同
- 每个分数可追溯到：分数 + 档位 + 理由 + 证据 ID + 证据状态 + 置信度
- 同一证据输入 → 稳定落档（可复现，防随机漂移）

---

#### 02 · Confidence 决策置信度

**Why** — 这个机会分数很高，但我们真的确定吗？

V3.1 把 **Opportunity Score（机会本身有多好）** 与 **Decision Confidence（证据有多充分）** 彻底分离：

`BT`
Opportunity Score   86 / 100
Confidence          LOW
Decision            POTENTIAL
`BT`

- 固定公式、可手工复算，不允许 LLM 随意修改
- 覆盖规则：关键付费证据缺失时强制降级（Coverage 高 ≠ Confidence 高）
- **Unknown（信息不足）≠ Low（机会差）**：两者显式分离

---

#### 03 · Hard Gates 硬门槛

**Why** — 一个项目不能因为其他维度分数高，就掩盖掉致命短板。

三层约束：

`BT`
Hard Gate        核心维度低于门槛 → NOT_RECOMMENDED
Score Ceiling    关键证据不足     → 最高 POTENTIAL
Red Flag         明确致命风险     → NOT_RECOMMENDED
`BT`

`BT`
Demand = 30
Monetization = 25
Total Score = 71

Decision → NOT_RECOMMENDED     （高分不能掩盖短板）
`BT`

> **High Score ≠ Automatically Recommended**

---

#### 04 · Evidence Coverage 证据覆盖度

**Why** — 这份报告到底研究了多少？

六维覆盖（每维 0-100）+ overall 等权平均：

`BT`
Problem       90
Solution      70
Payment       20
Competition   85
Distribution  60
Buildability  90
Overall       69

Critical Gap: Payment Evidence
`BT`

- 覆盖度衡量「关键决策问题被有效证据覆盖的程度」，不是简单数来源数量
- 同源转载 / 重复引用**去重**，不假装独立来源
- **总覆盖率不能掩盖关键证据缺失**（如 Payment）

---

#### 05 · Evidence-driven Action 证据驱动行动

**Why** — 分析完之后，下一步到底做什么？

`BT`
Evidence + Target User + Channel + Payment Signal + Unknown + Failure Condition
        ↓
具体 Action（不是"找客户 → 做 MVP → 测试"这种通用步骤）
`BT`

每一步必须包含：

`BT`
Action          做什么（动词 + 对象 + 数量 + 渠道，全部来自证据）
Success         成功标准（可量化）
Fallback        失败转向（If 条件 Then 具体决策，禁止"再努力"）
`BT`

`BT`
找到 30 个目标用户 → 筛选 10 个高意向 → 测试 Offer → 验证付费
  达到成功标准 → 进入 MVP
  未达到     → 修改 Offer（不开发产品）
`BT`

---

## 🧭 使用场景 / Use Cases

### AI Product

`BT`
我发现一个 AI 工具需求 → Market Scout → 验证需求/竞争/付费 → 判断是否开发
`BT`

### Indie Hacker

`BT`
一个产品想法 → Evidence → Score → Decision → Validation MVP
`BT`

### Service → Product

`BT`
一个重复人工需求 → 验证用户 → 验证付费 → 找自动化机会 → 决定是否产品化
`BT`

### Local Business / Offline

`BT`
线下真实痛点 → 用户证据 → 付费验证 → AI Solution → Action
`BT`

> 这里只展示 Market Scout 能做什么，不构成夸大商业承诺。

---

## 📺 真实使用示例 / Real Example

> 输入（V3.1 完整决策链，演示数据，方法见 examples/）

`BT`
INPUT: "我发现很多小商家不会做短视频，能不能做一个 AI 工具帮他们自动生成内容？"
`BT`

`BT`
Evidence       本地商家"不会做内容/代运营贵"的重复求助（Evidence）
Coverage       六维覆盖，Payment 覆盖 Partial → critical gap 明确
Score          Opportunity Score 0-100（计算式可复算）
Confidence     与 Score 分开展示（High / Medium / Low）
Hard Gate      核心门槛检查，缺付费证据 → Score Ceiling
Decision       🟡 POTENTIAL（付费未验证）
Action         证据驱动：用指定关键词找 30 家目标商家 → 筛 10 家高意向
               → 人工 + AI Concierge 交付样品 → 测试 99 元/次 Offer
               → 成功标准：10 人中 ≥3 有效回复、≥1 付费
               → 无人付费 → 修改 Offer，不开发产品
`BT`

> **Market Scout 不一定告诉你「去开发这个产品」。** 它也可能告诉你：**先用人工 + AI 验证 5–10 个客户是否愿意付费。** 这正是 V3.1 的价值。

更多示例（均为演示数据）：[V3.1 高分低置信](./examples/v3-1-high-score-low-confidence.md) · [V3.1 Score Ceiling](./examples/v3-1-hard-gate-score-ceiling.md) · [V3.1 证据驱动行动](./examples/v3-1-evidence-driven-action.md) · [V3 完整决策链](./examples/v3-decision-run.md) · [V3 红海市场](./examples/v3-crowded-market.md) · [V2 全流程](./examples/full-pipeline-v2.md)

## 📄 输出包含什么 / Output

最终给你的不是一篇「市场分析报告」，而是**一个有证据、有约束、有下一步行动的机会判断**：

`BT`
Opportunity Score      机会评分（可复算）
Confidence             决策置信度（与评分分离）
Evidence Coverage      证据覆盖度 + 关键缺口
Hard Gates             硬门槛检查（PASS / CEILING / FAIL）
Decision               三档结论 + Why
Critical Gaps          缺什么证据
MVP / Validation Plan  最小方案或验证实验
Today Action           今天做什么（动词 + 对象 + 数量 + 成功标准）
Fallback               失败后改什么
`BT`

---

## 🚀 安装 / Installation

> 以仓库真实安装方式为准（与 USER_GUIDE.md 完全一致）。纯 Markdown Skill：**不需要 npm / pip，不运行任何服务，无额外依赖。**

**方式一：拖拽一键安装（推荐）**

1. 下载并解压 [market-scout-v3.1.0.zip](./releases/market-scout-v3.1.0.zip)，取出其中的 market-scout 文件夹（部分客户端支持直接拖 zip）。
2. 拖入 AI 客户端的「技能 / 一键安装」入口；不支持时改用方式二。
3. 按「验证安装」确认版本。

**方式二：手动放入技能目录**

1. 解压得到 market-scout 文件夹。
2. 放入 AI 客户端的技能目录（通常叫 .user_skills/ 或 skills/）。
3. 保证路径为 <技能目录>/market-scout/SKILL.md。
4. 重启或刷新客户端。

**或 Clone 本仓库**：`git clone https://github.com/kio831/market-scout.git`，使用仓库根目录的 market-scout/ 内容。

> 装过旧版：V3.1 向下兼容、旧能力全部保留；部分平台同名目录不覆盖，建议先删除旧 market-scout 文件夹再安装。

**验证安装**：打开安装后的 SKILL.md，同时搜到 Opportunity Score 和 值得继续做 RECOMMENDED = V3.1.0；再搜到 v3-confidence.md 与 v3-hard-gates.md = V3.1 强化层就位。

## ⚡ 快速开始 / Quick Start

`BT`
1. Install Market Scout
2. Give it an idea / problem / observation
3. Choose Quick / Research / Execution
4. Let Market Scout analyze
5. Read Decision
6. Follow Evidence-driven Action
`BT`

示例输入：

`BT`
"我发现很多独立开发者不会做产品市场验证，我想做一个 AI 工具帮他们验证。"
`BT`

| 你想做什么 | 可以这样说 |
|---|---|
| 快速判断一个想法 | "学校打印店总有人让老板改 PDF，有没有机会？" |
| 分析视频 / 评论区 | "分析这个评论区，看能不能做成生意" |
| 验证需求真假 | "这个需求是真的吗？用户真的愿意付钱吗？" |
| 打分与决策 | "这个想法值不值得做，打个分" / "帮我决策" |
| MVP 与下一步 | "第一版做什么？" / "下一步做什么？" / "今天做什么？" |
| 完整跑一遍 | "从发现到商业化完整分析一遍，出一份机会报告" |

**三种工作模式**：Quick Mode（随手判断，默认，保持轻量）· Research Mode（深挖完整报告）· Execution Mode（停止研究、直接给执行清单，不重复研究）。

## 📚 Documentation

- [USER_GUIDE.md](./USER_GUIDE.md) — 面向最终用户的安装与使用说明
- [CHANGELOG.md](./CHANGELOG.md) — 版本变更记录
- [CONTRIBUTING.md](./CONTRIBUTING.md) — 贡献指南

## 📁 项目结构 / Repository Structure

`BT`
market-scout/
├── SKILL.md                    # 核心入口：铁律、V2 五阶段流水线、V3 决策层、V3.1 强化层、模式路由
├── README.md                   # 本文件（GitHub 项目主页）
├── USER_GUIDE.md               # 用户安装与使用说明
├── CHANGELOG.md                # 版本变更记录（v1.0 → v1.1 → v2.0.0 → v3.0.0 → v3.1.0）
├── CONTRIBUTING.md / LICENSE / .gitignore
├── references/  (22)           # 方法论文档
│   ├── v1 基础（6）：problem-framework / market-research / payment-validation
│   │                     ai-solution-patterns / evidence-chain / opportunity-state-machine
│   ├── v2 流水线（6）：demand-validation / project-evaluation / project-blueprint
│   │                     monetization-gtm / pipeline-and-runtime / ui-rendering-spec
│   ├── v3 决策层（6）：v3-overview / v3-evidence / v3-scoring
│   │                     v3-decision / v3-mvp / v3-action-plan
│   └── v3.1 强化层（4）：v3-scoring-rubric / v3-evidence-coverage
│                         v3-confidence / v3-hard-gates
├── templates/   (16)           # 可直接填充的卡片/报告模板
├── examples/    (9)            # 流程示例（全部为演示数据，含 3 个 V3.1 示例）
├── tools/
│   ├── validate_skill.py       # 自检脚本（382 项检查，无第三方依赖）
│   └── test_v31_cases.py       # V3.1 规则用例测试（A-F + 矩阵）
├── releases/
│   └── market-scout-v3.1.0.zip # ✅ V3.1.0 正式安装包
└── website/
    └── index.html              # 项目落地页（可挂 GitHub Pages）
`BT`

## 🗺 Roadmap

| 版本 | 状态 | 内容 |
|---|---|---|
| v1.0 | ✅ 已发布 | Market Discovery：三类搜索、Problem Card、Level 1-5 |
| v1.1 | ✅ 已发布 | Problem Discovery：Evidence Chain、三模式、状态机、停止机制 |
| v2.0.0 | ✅ 已发布 | Structured Evaluation：四阶段、0-100 评分、UI 规范 |
| v3.0.0 | ✅ 已发布 | Evidence-driven Pipeline：证据三态、三档决策、MVP、行动计划 |
| **v3.1.0** | **🚀 当前版本** | **Reliable Decision System：Rubric / Confidence / Hard Gates / Coverage / Evidence-driven Action** |
| 后续设想 | 📋 规划中 | 交互式 HTML 报告、多机会对比看板、评分历史追踪 |
| 远期设想 | 🔮 探索中 | 商业化模块独立服务、真实市场数据源接入、Web 化 |

> 当前版本是**纯 Markdown 文档型 Skill**：不含支付/订阅/计费系统、不含内置数据源或自动化 API，所有市场数据来自 Agent 运行时的实时搜索。

## 🤝 Contributing & License

欢迎 Issue 与 PR，流程见 [CONTRIBUTING.md](./CONTRIBUTING.md)。

[MIT](./LICENSE) © Market Scout Contributors —— 可自由使用、修改、分发，包括用于个人副业探索与商业项目。

---

<div align="center">

> **我有一个想法 → Market Scout 帮我找证据 → 评估这个机会 → 告诉我判断有多可靠 → 防止关键短板被总分掩盖 → 告诉我下一步具体做什么。**

**I have an idea → Market Scout finds the evidence → scores the opportunity → tells me how confident the decision is → prevents critical weaknesses from being hidden → tells me what to do next.**

### From vague ideas to evidence-backed decisions.

**FIND → PROVE → SCORE → DECIDE → ACT → LEARN**

[⬆ 回到顶部](#-market-scout)

</div>


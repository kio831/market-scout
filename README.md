# Market Scout

Market Scout is an AI Agent Skill for **market reconnaissance, demand discovery, pain-point analysis, business validation, and AI-solution design**.

It is not an "AI money-making idea generator." It does not start from "what can AI do to make money." It starts from:

> **Who has a real problem, and why would they pay to solve it?**

Then it asks: *Can AI let me solve it cheaper and faster?*

Core loop:

```
Real problem → Evidence → Demand → Payment → Competition → AI leverage
→ Minimum solution / MVP → Real users → First payment
→ Standardize → Automate → Productize
```

Core principle: **Validate first, then charge, then productize.** Never default to "build the product first, find users later."

---

## Why it is NOT an AI money-making idea generator

- It refuses to fabricate users, prices, transactions, or market data.
- Every market conclusion is labeled **Fact / Inference / Hypothesis** and must be traceable to a source.
- It has an explicit **stop condition**: if there is no evidence, no repeated demand, no payment behavior, or no AI advantage, it says **"not recommended to continue"** instead of forcing an opportunity.
- It avoids "research addiction": when evidence is enough for a low-cost real-world test, it stops researching and moves to execution.

## Core Workflow

1. **Recon (Three Searches)**:
   - **Problem Search** — does anyone actually have this problem?
   - **Solution Search** — how do they solve it today?
   - **Payment Search** — does anyone already pay for a similar result?
   - Problem + Solution + Payment evidence = business validation basis. **Problem evidence alone is only a "potential opportunity."**
2. **Record** every problem as a Problem Card; every important evidence as an Evidence Card.
3. **Evidence Chain** grading — A (validated) / B (potential) / C (hypothesis).
4. **Evidence-bound scoring** — 8 dimensions (Pain / Frequency / Payment / Market / AI Leverage / Feasibility / MVP Speed / Competition), each score must cite evidence.
5. **Competition & payment analysis** — what users really buy is the *result*, not "AI."
6. **Solution levels (Sell Result First)**: L1 human+AI → L2 semi-automation → L3 workflow → L4 small tool → L5 SaaS. Don't build a product by default.
7. **MVP + First payment** — small, minimal, start from 10/30/50/100.
8. **Opportunity state update** — track and advance only the current bottleneck.
9. **Output** — Quick Scan / Market Scan / Execution checklist.

## Three Modes

| Mode | When | Output |
|---|---|---|
| **Quick** | A casual problem/observation | Quick judgment: worth studying or not |
| **Research** | "Dig deeper / analyze this video / analyze these comments / full validation" | Complete Market Scan report |
| **Execution** | "I'm ready / get me the first customer" | Direct execution checklist (who, where, offer, pricing, delivery) |

## Evidence Chain

Every important market conclusion must follow:

```
Raw Evidence → Observation → Inference → Hypothesis → Validation
```

Each evidence record carries: **Source / Evidence Type / Confidence / What it proves / What it does NOT prove**. Jumping from raw evidence to a strong business conclusion is forbidden. When evidence is insufficient, write **"insufficient evidence"** instead of guessing.

## Opportunity Lifecycle (State Machine)

Each opportunity gets a unique ID (MS-###) and advances through:

```
HYPOTHESIS → DEMAND_CONFIRMED → MARKET_CONFIRMED → PAYMENT_VALIDATION
→ CUSTOMER_FOUND → FIRST_PAYMENT → REPEATED_DELIVERY → STANDARDIZED
→ AUTOMATED → PRODUCTIZED
```

- **CUSTOMER_FOUND** = a real potential customer with confirmed demand exists. "Willing to buy / willing to try" is only a validation signal.
- **FIRST_PAYMENT** = actual money received (transfer / deposit / paid order). Verbal willingness is NOT a first payment.

Note: **Evidence Level A/B/C** (validated / potential / hypothesis demand) and **Opportunity State names** are two separate systems and never share letter codes.

## Installation / Usage

- This skill works in AI clients that support skills (e.g. Doubao / agent platforms).
- Option A (drag & drop): drop `market-scout.zip` or `market-scout.skill` into the skill installer.
- Option B (manual): unzip into your skill directory so that `market-scout/SKILL.md` exists.
- To verify the installed version is v1.1: open `SKILL.md` and check it contains `CUSTOMER_FOUND` and `FIRST_PAYMENT`.
- For end-user instructions (in Chinese), see `USER_GUIDE.md`.

Trigger phrases (examples): "帮我找市场" · "分析这个视频" · "分析这个评论区" · "我发现一个问题…" · "这个能不能用 AI" · "这个能不能赚钱" · "帮我拿第一单" · "继续深挖" · "寻找竞争对手".

## Simple Example

A user observed that a small restaurant owner manually reconciles takeaway-platform orders into Excel for 1–2 hours every night, often making errors.

- **Problem Search** → forum posts: "reconciling accounts every day is exhausting", "is there a tool for auto-reconciliation" → repeated demand (B).
- **Solution Search** → manual entry; paid SaaS (expensive for small owners); gap = cheap, simple, done-for-you.
- **Payment Search** → paid reconciliation SaaS/accounting exists; low-cost done-for-you not yet mature → only a potential opportunity until verified.
- **AI solution** → Level 1 (human + AI): parse platform export, build a weekly reconciliation summary, human only reviews. **No development needed.**
- **MVP** → one store, one platform, Excel delivery; validate whether the owner pays 30/week or 100/month.
- **First payment** → free one-week trial → quote → actual payment → `FIRST_PAYMENT`.

## Files

```
market-scout/
├── SKILL.md                # Core workflow, rules, modes, decision tree
├── README.md               # This file
├── USER_GUIDE.md           # End-user installation & usage guide (Chinese)
├── LICENSE                 # MIT
├── .gitignore
├── references/             # 6 methodology docs (evidence chain, three searches, state machine, ...)
├── templates/              # 5 fillable templates (problem card, evidence card, report, ...)
└── examples/               # 3 worked examples (incl. full problem→first-payment walkthrough)
```

> Note: data in `examples/` is illustrative only, for demonstrating methodology — not real market findings.

## License

[MIT](LICENSE) © 2026 kio831

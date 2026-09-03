<div align="center">

# Market Scout

**An AI-powered tool for discovering, validating, evaluating, and commercializing project opportunities.**

Turn a vague idea into a clear verdict (worth doing or not), an executable project, and a path to first revenue.

[![Version](https://img.shields.io/badge/version-v2.0.0-blue)](https://github.com/kio831/market-scout/releases)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Skill Type](https://img.shields.io/badge/type-Agent%20Skill-orange)]()
[![Platform](https://img.shields.io/badge/platform-Any%20Markdown%20Agent-lightgrey)]()

**Find to Validate to Evaluate to Monetize**

```
+----------+    +----------+    +----------+    +----------+
|   FIND   | -> | VALIDATE | -> | EVALUATE | -> | MONETIZE |
| Discover |    |  Demand  |    | Project  |    |    & GTM  |
+----------+    +----------+    +----------+    +----------+
```

</div>

---

## What is Market Scout?

Market Scout is an **AI Agent Skill** — a pure Markdown methodology package that, once installed into a Skill-compatible AI client, gives the agent a complete workflow for market opportunity reconnaissance and commercial validation.

It is not an "AI money-making project generator." It does not invent projects. Its core question sequence is:

> **Who has what problem? Why would they pay to solve it? Can AI let me solve it cheaper and faster? Is it worth doing, what should it be, how do I charge, and where do the first customers come from?**

Not just for discovering new market opportunities — you can also feed in an existing project idea and validate, evaluate, and commercialize it.

### What problem it solves

People starting a side project or business typically get stuck at: having a vague idea but not knowing if it's real demand; sensing demand but not knowing if users will pay; not knowing whether the project is worth the time; deciding to build but not knowing what the MVP should be; and not knowing how to price or where to find customers. Market Scout structures each step with evidence-bound analysis.

### Who it's for

- Solo developers and indie makers validating side project ideas
- Content creators and operators looking for monetizable niche opportunities
- Students and first-time founders who need a structured, low-cost validation path
- Anyone who wants to turn "I think there's a market" into "here's the evidence, the score, and the first action"

### Why you need it

- **Evidence over intuition** — every conclusion is bound to real search evidence; "the market is huge" without evidence is explicitly forbidden
- **Reproducible scoring** — the 7-dimension weighted score (0-100) can be recalculated by hand
- **Validate before building** — default to Level 1 (human + AI, sell the result first); 7 no-build validation methods
- **From idea to first payment** — not just a market report, but "what to do today" and "how to collect the first payment"

---

## Core Features

### 1. Discover Opportunity

Find opportunities from markets, communities, and real user discussions.

- Three search types: Problem / Solution / Payment
- Evidence Chain (raw evidence to observation to inference to hypothesis to validation)
- Problem Card and Evidence Card with 8-dimension rough scoring
- Video / comment / post reverse analysis

### 2. Validate Demand

Verify whether user pain points are real.

- Pain point analysis + three-layer target users (core / extended / non-users)
- Demand Strength 1-10 score from 6 signals, each bound to evidence
- Current solutions and substitution cost (pricing anchor)
- Payment reason chain (JTBD): Job to Cost to Trigger to Reason to Authority
- Demand evidence credibility matrix

### 3. Evaluate Project

Analyze market, competition, development difficulty, differentiation, and project value.

- 7-dimension weighted scoring: Demand 20% / Market 20% / Competition and Differentiation 15% / AI Feasibility 15% / Development Difficulty 10% / Solo Fit 15% / Risk 5%
- Composite Opportunity Score 0-100, formula must be hand-recalculable
- 7 fatal red flags (one-vote veto)
- Three-tier verdict: **GO** (worth doing) / **VALIDATE_FIRST** (validate before committing) / **NO_GO** (not recommended)

### 4. Opportunity to Project

Turn a market opportunity into a concrete, executable MVP.

- Recommended product form (aligned with Level 1-5, default L1: sell the result first)
- MoSCoW feature prioritization (Must-have at most 3)
- MVP five items: what to build / what not to build / what to validate / continue condition / abandon condition
- Recommended tech direction + minimal validation experiment + differentiation entry point

### 5. Monetization and GTM

Analyze target customers, business model, pricing, and first-customer acquisition.

- Target Customer (distinguishes user from payer)
- Offer three-tier ladder (lead / main / value-add)
- Business Model library with selection rules
- Explainable Pricing: value anchor / market anchor / cost floor / first-payment price / regular price / price increase path
- First 10 customers acquisition method + channel matrix (main channels at most 2) + GTM three phases
- 7 no-build validation methods (Concierge / landing page smoke test / Fake Door / pre-sale / crowdfunding / paid diagnosis / sample for testimonial)
- Modular data contract (MonetizationInput / MonetizationPlan) — designed to become a standalone product in the future

---

## What's New in V2

V1 focused on **market opportunity discovery**. V2 completes the full loop: **validate demand, evaluate project, generate project plan, monetization and GTM analysis**.

| V1 | V2 |
|---|---|
| Market Discovery | Market Discovery |
| Basic Analysis | Demand Validation |
| — | Project Evaluation |
| — | Opportunity to Project |
| — | Monetization and GTM |
| — | Modular data contracts |
| — | Runtime robustness (timeout / retry / fallback / resume) |
| — | UI rendering spec and unified stage cards |
| — | Final Opportunity Report (conclusion-first) |

All V1 capabilities are preserved — this is an incremental, backward-compatible upgrade.

---

## How It Works

```
Market / Idea (market phenomenon or existing idea)
        |
        v
   Discover
   Three search types + Evidence Chain + Problem/Evidence Card
        |
        v
   Validate
   Demand strength 6 signals + payment reason chain -> is demand real and strong?
        |  (fake/weak demand circuit breaks here)
        v
   Evaluate
   7-dimension weighted score 0-100 + red flag check -> GO / VALIDATE_FIRST / NO_GO
        |  (NO_GO circuit breaks here)
        v
   Build MVP
   Product form + MoSCoW + MVP five items + minimal validation experiment
        |
        v
   Monetize
   Pricing + business model + acquisition channels + first 10 customers
        |
        v
   Go To Market
   First payment plan + action roadmap (today / this week / 2-4 weeks)
        |
        v
   Opportunity Report (final)
   Conclusion-first: what is being analyzed -> what was found -> what to do next
```

---

## Demo / Screenshots

> Screenshots pending. Market Scout's "UI" is the Markdown report rendered by the AI Agent — it looks different across agent platforms. Real usage screenshots will be added here.

Expected screenshot sequence (by user flow):

1. Home / input
2. Opportunity Discovery (Problem Card / Evidence Card)
3. Demand Validation (demand strength score + payment reason chain)
4. Project Evaluation (7-dimension score table + verdict)
5. Monetization and GTM (pricing + first 10 customers)
6. Final Opportunity Report (conclusion-first summary)

No fabricated screenshots or fake data are used.

---

## Quick Start

### Requirements

- **Python 3.8+** — only needed to run the self-check script (tools/validate_skill.py); no third-party dependencies
- **A Markdown-Skill-compatible AI Agent platform** — e.g. Doubao, Claude Desktop, Cursor, or any agent that reads SKILL.md from a skills directory

### Installation

**Method 1: Drag-and-drop (recommended)**

1. Download market-scout.skill (or .zip) from the [Releases](https://github.com/kio831/market-scout/releases) page
2. Drag it into your AI client's "Skill / one-click install" entry point
3. Verify: open SKILL.md and search for `Monetization & GTM` and `GO` — both present means v2.0.0 is installed

**Method 2: Manual install**

1. Unzip market-scout.zip — you get a market-scout/ folder
2. Place it in your AI client's skills directory (usually .user_skills/ or skills/)
3. Ensure the path is skills-directory/market-scout/SKILL.md
4. Restart or refresh the client

### Environment Variables

None required. Market Scout relies on the agent platform's already-configured search and browser capabilities.

### Run Development Server

**Not applicable.** Market Scout is a pure Markdown documentation Skill — there is no frontend dev server, no backend, and no database. The "UI" is the Markdown report rendered by the AI Agent at runtime.

### Build for Production

**Not applicable.** There is no build chain. A "release" is simply packaging the market-scout/ directory into .zip and .skill files:

```bash
# On Windows (PowerShell)
Compress-Archive -Path ./market-scout -DestinationPath ./market-scout.zip -Force
Copy-Item ./market-scout.zip ./market-scout.skill

# Run self-check before release
python ./market-scout/tools/validate_skill.py
```

---

## Tech Stack

Only technologies actually used by the project are listed.

| Category | Technology |
|---|---|
| Core format | Markdown + YAML frontmatter |
| Data contracts | YAML / JSON Schema (MonetizationInput, MonetizationPlan) |
| Tooling | Python 3 (tools/validate_skill.py, zero third-party dependencies) |
| Runtime | Agent-native capabilities (general search / browser / file read) |
| Frontend | None — no frontend framework |
| Backend | None — no server |
| Database | None — no persistence layer |
| Deployment | GitHub Pages for website/index.html (optional) |

---

## Project Structure

```
market-scout/
├── SKILL.md                 # Core entry: rules, pipeline, mode routing, UI spec
├── README.md                # This file
├── USER_GUIDE.md            # End-user installation and usage guide
├── CHANGELOG.md             # Version history
├── LICENSE                  # MIT
├── CONTRIBUTING.md          # Contribution guide
├── references/              # Methodology documents (12 files)
│   ├── problem-framework.md # [v1] Problem Card, evidence grades, 8-dim scoring
│   ├── market-research.md   # [v1] Three search types, video/comment analysis
│   ├── payment-validation.md# [v1] Payment signals, first-payment checklist, stop mechanism
│   ├── ai-solution-patterns.md # [v1] Level 1-5, MVP, degradation rules
│   ├── evidence-chain.md    # [v1] Evidence chain, anti-jump rules
│   ├── opportunity-state-machine.md # [v1] Delivery state machine
│   ├── demand-validation.md # [v2] Demand validation (VALIDATE)
│   ├── project-evaluation.md# [v2] Project evaluation and scoring (EVALUATE)
│   ├── project-blueprint.md # [v2] Opportunity to Project (BLUEPRINT)
│   ├── monetization-gtm.md  # [v2] Monetization and GTM (MONETIZE, modular contract)
│   ├── pipeline-and-runtime.md # [v2] Pipeline orchestration, runtime robustness
│   └── ui-rendering-spec.md # [v2.0.0] Output rendering and visual spec (Design System)
├── templates/               # Fill-in templates (10 files)
│   ├── problem-card.md / evidence-card.md / quick-scan.md / market-report.md  # [v1]
│   ├── opportunity-card.md  # [v2 upgraded] compatible with v1 fields
│   ├── demand-validation-card.md / project-evaluation-card.md
│   ├── project-blueprint-card.md / monetization-gtm-card.md
│   └── opportunity-report.md # [v2] Final five-stage report
├── examples/                # Workflow examples (4 files)
│   ├── video-analysis.md / comment-analysis.md / real-world-problem.md  # [v1]
│   └── full-pipeline-v2.md  # [v2] Complete five-stage example with reproducible score
├── tools/
│   └── validate_skill.py    # Self-check script (161 checks)
└── website/
    └── index.html           # Product landing page (GitHub Pages ready)
```

---

## Roadmap

- [x] Market Opportunity Discovery (v1.x)
- [x] Evidence Chain and three search types (v1.x)
- [x] Quick / Research / Execution three modes (v1.x)
- [x] Demand Validation (v2.0.0)
- [x] Project Evaluation with 7-dimension scoring (v2.0.0)
- [x] Opportunity to Project (v2.0.0)
- [x] Monetization and GTM with modular data contract (v2.0.0)
- [x] UI rendering spec and unified stage cards (v2.0.0)
- [x] Final Opportunity Report (v2.0.0)
- [x] Open-source release assets: README, CHANGELOG, LICENSE, CONTRIBUTING, landing page (v2.0.0)
- [ ] More data source integrations (job boards, SaaS review sites, e-commerce reviews)
- [ ] Better opportunity scoring with real market data
- [ ] Interactive HTML report generator
- [ ] Multi-opportunity comparison dashboard
- [ ] Monetization module as standalone callable API
- [ ] Real pricing / market data API integration
- [ ] Web application version

---

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) for the process.

- Bug reports and feature suggestions: open an Issue
- New features: open an Issue to discuss first, then a PR
- Documentation improvements: PR directly

## License

[MIT](LICENSE) (c) Market Scout Contributors

Free to use, modify, and distribute — including for personal side-project exploration and commercial projects.

---

<div align="center">

If this tool helps you collect your first payment, come back and share your story.

</div>

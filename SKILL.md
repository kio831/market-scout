---
name: market-scout
description: Market Scout (v2.0.0) — AI-powered market opportunity discovery, validation, evaluation and commercialization. Complete pipeline: Find (discover) to Validate (demand) to Evaluate (project) to Blueprint (MVP) to Monetize (pricing & GTM). Use when user wants to find market opportunities, validate demand, evaluate project feasibility, score opportunities, design MVP/business model/pricing, find first customers, analyze videos/comments for hidden business opportunities, or get first payment. Core principle: Search First, never fabricate users/prices/data. Preserves all v1.1 capabilities (Evidence Chain, three search types, three modes, Opportunity state machine, evidence-bound scoring). v2.0 adds Demand Validation, Project Evaluation (7-dimension weighted score 0-100, GO/VALIDATE_FIRST/NO_GO), Opportunity to Project, Monetization & GTM with modular MonetizationInput/MonetizationPlan data contracts. Outputs conclusion-first Opportunity Report. Evidence grades A/B/C, delivery state names, and pipeline stage names are three independent code systems.
---

# Market Scout (v2.0.0)

**Find to Validate to Evaluate to Blueprint to Monetize** — complete market opportunity workbench.
Market reconnaissance + demand discovery + demand validation + project evaluation + AI solution/project design + monetization and GTM.
Not an "AI money-making project generator" — turns real problems into "verdict on worth doing + executable project + path to first revenue".

> **v2.0 incremental note**: All v1.1 capabilities (three search types, evidence chain, three modes, 8-dimension evidence-bound scoring, Level 1-5, state machine, stop mechanism, first payment, templates and examples) are **all preserved and reused**; v2.0 appends four new stages after discovery: demand validation, project evaluation, opportunity to project, monetization and GTM. Orchestration and data contracts see `references/pipeline-and-runtime.md`.

## Core Positioning

First ask **"Who has what problem? Why would they pay to solve it?"**, then ask **"Can AI let me solve it cheaper and faster?"**.

Final flow: `real problem to evidence to demand to payment to competition to AI leverage to minimal solution/MVP to real users to first payment to standardization to automation to productization`.

Core principles:
- **Validate first, then charge, then productize.**
- Forbid defaulting to "build product first, then find users".
- Must prioritize "discover problem first, collect evidence, validate demand, validate payment, then decide whether to build".
- Final goal is not generating a pretty market report, but advancing a problem to **first real transaction**.

Core loop:

```
discover problem -> collect evidence -> judge demand -> judge payment -> analyze competition -> judge AI leverage
-> design minimal solution -> MVP -> find real users -> deliver -> get first payment
-> review -> standardize -> automate -> productize
```

## V2 Main Pipeline: Find to Validate to Evaluate to Monetize (P0)

v2.0 upgrades the workflow to five sequential stages (orchestration, circuit breaking, resume from breakpoint, data contracts see `references/pipeline-and-runtime.md`):

```
FIND (discover)         VALIDATE (demand)       EVALUATE (project)
(v1.1 three search,  ->  (demand-validation  ->  (project-
  evidence chain,          .md)                    evaluation.md)
  Problem card)
   |                        |                        |
   v                        v                        v
BLUEPRINT (opportunity  MONETIZE (commercial    REPORT (opportunity
to project)             ization & GTM)           report)
(project-blueprint.md)  (monetization-gtm.md)    (templates/opportunity-report.md)
```

| Stage | Core question answered | Methodology | Output card |
|---|---|---|---|
| FIND discover | Are there real problems/existing solutions/payment behavior? | `market-research.md`, `evidence-chain.md` | Problem/Evidence Card (v1.1) |
| VALIDATE demand validation | Is demand real, strong, why would users pay? | `demand-validation.md` | `templates/demand-validation-card.md` |
| EVALUATE project evaluation | Is this project worth my investment? Composite score? | `project-evaluation.md` | `templates/project-evaluation-card.md` |
| BLUEPRINT opportunity to project | What product/MVP to build? How to validate? | `project-blueprint.md` (reuses Level 1-5) | `templates/project-blueprint-card.md` |
| MONETIZE monetization & GTM | Who pays/what to sell/how to charge/where to find/how first customers come? | `monetization-gtm.md` (reuses first payment checklist) | `templates/monetization-gtm-card.md` |
| REPORT | One report to judge worth doing + first action | `pipeline-and-runtime.md` section 4 | `templates/opportunity-report.md` |

### Four New Capability Summaries

1. **Demand Validation**: user pain points, three-layer target users (core/extended/non-users), demand strength 6-signal synthesis 1-10, current solutions and substitution cost, payment reason chain (JTBD 5 rings), demand evidence credibility; conclusion three-choice (real demand validated / demand exists but payment not validated / fake-weak demand).
2. **Project Evaluation**: 7-dimension weighted scoring (Demand 20%, Market 20%, Competition & Differentiation 15%, AI Feasibility 15%, Development Difficulty 10%, Solo Fit 15%, Risk 5%) to composite Opportunity Score 0-100, **formula must be hand-recalculable**; conclusion three-tier **GO (worth doing) / VALIDATE_FIRST (validate before committing) / NO_GO (not recommended)**, determined by "total score + threshold items + fatal red flags" together, not just total score; 7 fatal red flags one-vote veto.
3. **Opportunity to Project**: recommended product form (aligned with Level 1-5, default L1 sell result first), core users, MoSCoW core features (Must-have at most 3), MVP five items, recommended tech direction, minimal validation experiment, differentiation entry point.
4. **Monetization & GTM**: Target Customer (distinguishes user from payer), Offer three-tier ladder, Business Model library with selection rules, explainable Pricing, first 10 customers acquisition, channel matrix (main channels at most 2), GTM three phases, 7 no-build validation methods, first payment plan.

### Monetization Module Independence Boundary (future design, payment system not implemented currently)

- Monetization & GTM is a **modular capability**: has clear input contract MonetizationInput and output contract MonetizationPlan (see `monetization-gtm.md` section 8), only depends on structured data, does not depend on UI or other stage internal implementations.
- In the future it can be independent as a product, independently charged, independently acquiring customers, only need to feed data/render results per contract, **no major refactoring needed**.
- **Current version explicitly does not develop** payment, subscription, membership, billing or any systems, only produces monetization plans and validation actions.

### Three Independent "Code/State" Systems (important)

- **Evidence grade A/B/C**: demand validation degree (`problem-framework.md` section 3).
- **Opportunity State**: real-world delivery state (HYPOTHESIS to ... to PRODUCTIZED, `opportunity-state-machine.md`), FIRST_PAYMENT must be real payment received.
- **Pipeline Stage (v2.0 new)**: analysis pipeline position (FIND/VALIDATE/EVALUATE/BLUEPRINT/MONETIZE/REPORT).
Three are orthogonal, e.g. `Pipeline=MONETIZE / State=DEMAND_CONFIRMED / evidence grade=B` is completely legal, forbid using one set of letters to express multiple meanings.

## Iron Rules (must obey)

1. **Search First (three search types)**: as long as search/browser capability exists, must prioritize real-time search. Verify separately by three types (see `references/market-research.md` section three search types):
   - **Problem Search**: prove whether real users encounter this problem.
   - **Solution Search**: prove how users currently solve (without your solution).
   - **Payment Search**: prove whether real payment behavior already exists near this problem.
   All three evidence types together form commercial validation foundation; **when only Problem Evidence but no Payment Evidence, must not judge as strong commercial opportunity.**
2. **Forbid pretending to search**: if truly no search capability, must clearly state "[currently cannot perform real-time market validation, below is hypothetical analysis]", all conclusions marked as hypothesis, not disguised as verified.
3. **No fabrication**: no fabricated users, prices, transactions, data. Content that cannot be verified can only be "hypothetical/to be validated", never written as "fact/discovered".
4. **Evidence Chain**: every important market conclusion must go through `raw evidence to observation to inference to hypothesis to validation` chain (see `references/evidence-chain.md`). Forbid "raw evidence to directly strong commercial conclusion". Each evidence marked Evidence/Source/Evidence Type/Confidence/Proves/Does NOT prove. When evidence insufficient clearly write [insufficient evidence], must not fill model guesses to complete report.
5. **Right to stop (Stop Conditions)**: when evidence insufficient, no repeated demand, no payment behavior, AI no advantage, competition barrier too high, individual cannot complete at low cost, user cannot reach target customers, etc. (full list see `references/payment-validation.md` section stop mechanism), directly output [not recommended to continue] and explain stop reason and restart conditions, forbid forcibly creating opportunities.
6. **Avoid research addiction**: when evidence already sufficient to support a low-cost validation, stop continuing research, output [research phase complete], enter Execution Mode. Research is not the endpoint, validation is.

## Three Work Modes

| Mode | When to enter | Goal | Exit |
|---|---|---|---|
| **Quick Mode** | user casually throws a problem/phenomenon (default entry) | quickly judge "worth continuing research", no long report | `templates/quick-scan.md` |
| **Research Mode** | user explicitly requests deep dive/market research/find competitors/analyze comments/full validation | complete Market Scan, run full pipeline | `templates/market-report.md` |
| **Execution Mode** | user says "I'm ready to do/want to try/get first order/start executing/this can work" | stop research, directly advance real users and first payment | execution checklist see `references/payment-validation.md` section first payment |

Routing logic:
- Default for "a problem/a phenomenon" first go **Quick Mode**; when user does not request deep dive do not automatically upgrade to long report.
- When "deep dive / market research / find competitors / find similar demand / analyze comments / full validation" etc. clear intent appears -> **Research Mode**.
- When "I'm ready to do / I want to try / help me get first order / start executing / this can work" -> **Execution Mode** (no longer continue research).
- No direction long-term opportunity finding -> 30-day reconnaissance or Market Scan (Research Mode).

## Mode Routing (fine-grained)

| User intent | Trigger words (example) | Work mode | Exit |
|---|---|---|---|
| Casually throw a problem | "School print shop always has people asking boss to edit PDF, any opportunity?" | Quick | `templates/quick-scan.md` |
| Find market | "Help me find market" "Find money-making opportunities" "Any demand" | Research / 30-day | `templates/market-report.md` |
| Analyze video/content | "Analyze this video" "Can this content make money?" | Research (Video Reverse) | `references/market-research.md` section video reverse market analysis |
| Analyze comments | "Analyze this comment section" "Look at these comments" | Research (Comment Mining) | `references/market-research.md` section comment demand mining |
| Report a specific problem | "I found a problem..." "XX is troublesome" | Quick -> Research if needed | `templates/problem-card.md` |
| Judge AI feasibility | "Can this problem use AI" "Can it be automated" | Quick/Research | `references/ai-solution-patterns.md` |
| Judge commercial value | "Can this make money" "Is there a market" | Research (Payment) | `references/payment-validation.md` |
| Get first order | "Help me get first order" "How to charge" "Who to sell to" "I'm ready to do" | **Execution** | `references/payment-validation.md` section first payment |
| Deep dive | "Continue deep dive" "Go deeper" | Research (Deep) | `references/market-research.md` section Deep Research |
| Find similar demand | "Find similar demand" "Who else needs this" | Research (Demand Expansion) | `references/problem-framework.md` section three-pool maintenance |
| Find competitors | "Find competitors" "Is anyone doing this" | Research (Competitor) | `references/market-research.md` section competition and payment analysis |
| Solution too complex | "This solution is too complex" "Any simpler one" | Auto downgrade solution | `references/ai-solution-patterns.md` section downgrade rules |
| No clear project, want long-term finding | "I want to do side hustle but no direction" | 30-day market reconnaissance | `references/market-research.md` section 30-day reconnaissance mode |
| Validate demand reality/strength (v2.0) | "Is this demand real" "Do users really want it" "How strong is demand" | V2: VALIDATE | `references/demand-validation.md` |
| Evaluate project worth doing (v2.0) | "Evaluate this project" "Worth doing" "Feasibility analysis" "Give a score" | V2: EVALUATE | `references/project-evaluation.md` |
| Opportunity to project/MVP (v2.0) | "Help me make it a product" "Design MVP" "What first version does" "How to choose tech" | V2: BLUEPRINT | `references/project-blueprint.md` |
| Business model/pricing/GTM (v2.0) | "How to charge/price" "How to design business model" "How to find customers" "Where first users come from" "GTM" | V2: MONETIZE | `references/monetization-gtm.md` |
| Complete opportunity report (v2.0) | "Analyze end to end" "Output an opportunity report" "Discovery to validation to evaluation to monetization" | V2: full pipeline | `templates/opportunity-report.md` |

If input hits multiple modes simultaneously (e.g. "Can this video make money?"), advance by chain: Reverse Engineering to Payment Validation to AI Solution Design if needed, do not stop in middle.
If user requests complete judgment "worth doing + how to do + how to make money", advance by V2 five-stage pipeline FIND to VALIDATE to EVALUATE to BLUEPRINT to MONETIZE in order (allow entering from specified stage, but must first fill missing fields required by that stage input contract, see `references/pipeline-and-runtime.md`).

## Standard Workflow (v1.1 nine steps = internal refinement of V2 pipeline FIND stage; v2.0 connects four stages after)

> Relationship: steps 1-9 below complete "discovery/preliminary validation", corresponding to V2 **FIND**; after completion enter VALIDATE to EVALUATE to BLUEPRINT to MONETIZE per step 10. User can also directly enter from a V2 stage (must satisfy that stage input contract).

### 1. Reconnaissance (three search types)
- **Problem Search**: search complaints, "any tool", "how to batch", "too troublesome", "do every day", "can anyone help me", "recommend", "how to solve", repeated labor, time waste, labor cost, errors, efficiency problems.
- **Solution Search**: search software/SaaS/service providers/outsourcing/Freelancer/Agency/manual service/Excel script automation/free solutions/alternatives. Must answer "how do users solve when not using my solution?"
- **Payment Search**: search pricing/price/service/freelancer/outsourcing/quote/cost/agency/paid service/marketplace/service quote/SaaS price. Must prioritize finding "does anyone in the market pay for similar results?"
- Real-world observation: schools, dorms, companies/internships, shops, small/micro businesses, individual merchants, friends/classmates, daily workflow, repeated labor. Supports "observe to record to search to compare to validate".

### 2. Record as Problem Card + Evidence Card
Each candidate problem fill Problem Card (`templates/problem-card.md`), each important evidence fill Evidence Card (`templates/evidence-card.md`).

### 3. Evidence Chain Grading
Put each evidence on chain `raw evidence to observation to inference to hypothesis to validation`, mark evidence attributes and evidence grade (see `references/evidence-chain.md`). Grade judgment: A validated demand / B potential demand / C hypothetical demand. Anything without source can only reach C.

### 4. Scoring (bound to evidence)
For problems worth continuing, score by 8 dimensions, **each score must give: score + scoring reason + corresponding evidence + current uncertainty** (see `references/problem-framework.md` section evidence-bound scoring). Especially strengthen Payment scoring, with clear tiers. **Forbid scoring only by subjective feeling, forbid concluding only by total score.** Must answer: why worth continuing? Biggest uncertainty? What evidence missing? What should be validated next?

### 5. Analyze competition and payment
For each problem worth researching, check: any existing tools/SaaS/manual services/free solutions, why users don't use, current price, competitor advantages, biggest disadvantages, whether individual still has entry space. Analyze "what do users really buy" (results/time/efficiency/cost reduction/task completion/information/quality, not "buy AI"). No payment evidence must be clearly pointed out.

### 6. Generate solution (must complete problem analysis first)
By priority: L1 human+AI to L2 semi-automation to L3 automated Workflow to L4 small tool to L5 SaaS/product. Principle: **sell result first, then productize**. Before real users, forbid prioritizing developing complex SaaS/Agent. If a problem can be completed for first delivery by "one person + AI + simple tools", do not default recommend developing complete product. If no development needed, clearly write [currently no development needed]. Actionable solutions answer item by item (see `references/ai-solution-patterns.md` section actionable solution checklist).

### 7. Opportunity state update
For each opportunity worth tracking, establish unique Opportunity ID (e.g. MS-001), clarify current state and current bottleneck (see `references/opportunity-state-machine.md`). Only advance current bottleneck, do not repeat meaningless searches.

### 8. MVP and first payment
- MVP must be minimal, clearly [what first version does] [what first version does not do] [what to validate] [what result means continue] [what result means abandon]. Prioritize validating "will anyone pay for results?"
- First payment: around current Opportunity execute "who might buy to where to find to what result to give to how to展示 to how much to how to deliver to how to charge to how to get feedback". Allow 10/30/50/100 yuan small-amount validation. First payment meaning is validating `real problem to real solution to real payment`.

### 9. Output
Quick Mode to Quick Scan; Research Mode to Market Scan (`templates/market-report.md`); Execution Mode to execution checklist + what to do today.

### 10. V2 Connection: Validate to Evaluate to Blueprint to Monetize (v2.0)
After FIND gets an opportunity worth tracking, advance in order (each stage produces corresponding card, methods see respective reference):
1. **VALIDATE demand validation**: fill `templates/demand-validation-card.md` — pain points, three-layer users, demand strength 6 signals, substitution cost, payment reason chain; fake/weak demand circuit breaks here.
2. **EVALUATE project evaluation**: fill `templates/project-evaluation-card.md` — 7-dimension weighted scoring, list hand-recalculable formula, red flag check, give GO/VALIDATE_FIRST/NO_GO three-tier conclusion; NO_GO circuit breaks here.
3. **BLUEPRINT opportunity to project**: fill `templates/project-blueprint-card.md` — product Level, core users, MoSCoW, MVP five items, tech direction, minimal validation experiment, differentiation落地.
4. **MONETIZE monetization & GTM**: fill `templates/monetization-gtm-card.md` — payer/ICP, Offer, business model, explainable pricing, first 10 customers, main channels, GTM, no-build validation, first payment plan.
5. **REPORT**: consolidate to `templates/opportunity-report.md` (conclusion-first), one screen gives "worth doing + first step today".
Stage circuit breaking, fallback, resume from breakpoint, failure degradation see `references/pipeline-and-runtime.md`.

## Output and UI Spec (v2.0.0, report is UI)

All stage cards and report visual rendering uniformly follow `references/ui-rendering-spec.md` (Design System: verdict banner, stage progress bar, 10-cell score bar, action buttons, Loading/Empty/Error/Success four states, mobile narrow-screen rules, long report TOC and summary). Core points (full version see `references/pipeline-and-runtime.md` section 4 and `references/ui-rendering-spec.md`):
- **Conclusion first**: top verdict band (signal light + composite score + Opportunity ID + Pipeline/State), then key judgments, scoring, evidence, action suggestions; let user see conclusion and next step in 10 seconds.
- **Explainable scoring**: unified 10-cell score bar; composite score must attach hand-recalculable weighted formula; forbid "market is huge" "prospects are broad" etc. evidence-free conclusions.
- **Bilingual not crowded**: titles/fixed labels "Chinese (English)", body Chinese primary with key terms in parentheses English, not sentence-by-sentence translation; three-tier verdict fixed bilingual (GO / VALIDATE_FIRST / NO_GO).
- **Desktop and mobile**: desktop use comparison tables, narrow screen change wide tables to vertical "field: content" key-value lists, split long tables into small tables, ensure no horizontal scrolling on phone.
- **Code/data structure area**: Schema, contracts, formulas all use fenced code blocks with language tags (yaml/json/text), field names English, comments Chinese, proper indentation.
- **Runtime robustness**: all external search/network/sub-agent calls set timeout, transient errors bounded retry (exponential backoff), failure graded degrade by "switch source to use user material to mark [insufficient evidence]" and record, deterministic errors no retry; see `references/pipeline-and-runtime.md` section 3.

## Evidence Chain Mechanism (P0)

Every important market conclusion must go through five-segment chain:

```
raw evidence -> observation -> inference -> hypothesis -> validation
```

- **Forbid**: raw evidence -> directly strong commercial conclusion.
- Each evidence marked: Evidence (original text), Source, Evidence Type, Confidence, What this evidence proves, What this evidence does NOT prove.
- Insufficient evidence write [insufficient evidence], do not fill model guesses.
- Full definitions, evidence types, confidence calibration and examples see `references/evidence-chain.md`.

## Three Search Types (P0)

```
Problem Evidence (does anyone encounter this problem?)
+ Solution Evidence (how do they currently solve?)
+ Payment Evidence (does anyone pay for similar results?)
= commercial validation foundation
```

When only Problem Evidence, no Payment Evidence, at most judge "potential opportunity (B)", must not judge as strong commercial opportunity. Search keyword families and discipline see `references/market-research.md` section three search types.

## Opportunity State Machine (P1)

Each important opportunity has unique ID (MS-###), advances along states:

```
HYPOTHESIS -> DEMAND_CONFIRMED -> MARKET_CONFIRMED
-> PAYMENT_VALIDATION -> CUSTOMER_FOUND
-> FIRST_PAYMENT -> REPEATED_DELIVERY -> STANDARDIZED
-> AUTOMATED -> PRODUCTIZED
```

**States always use full English state names** (e.g. DEMAND_CONFIRMED, FIRST_PAYMENT), not letter codes, to avoid confusion with **evidence grade A/B/C** (A=validated demand / B=potential demand / C=hypothetical demand, unchanged). **FIRST_PAYMENT must actually receive real payment**; "willing to pay/willing to try/quote willingness" are only validation signals, at most advance to CUSTOMER_FOUND. Each time continuing research on same opportunity: read previous evidence -> do not repeat meaningless searches -> clarify current state -> clarify missing next evidence -> only advance current bottleneck. Full rules see `references/opportunity-state-machine.md`.

## Core Decision Tree

```
Real problem?
|
Repeated occurrence?
|
Painful enough?
|
Users actively seek solutions?
|
Market has similar solutions?
|
Anyone pays for similar results?
|
AI can significantly reduce cost/time/skill barrier?
|
Individual can deliver at low cost?
|
Find real users?
|
First payment?
|
Repeat delivery?
|
Standardize?
|
Automate?
|
Productize?
```

Any key node is NO: do not forcibly create opportunity, return to corresponding validation step; or output [not recommended to continue] per "stop mechanism".

## Quick Validation Modes

- **7-day validation**: Day1 confirm problem and evidence -> Day2 research existing solutions -> Day3 make minimal sample -> Day4 find potential users -> Day5 low-cost test delivery -> Day6 collect feedback -> Day7 try charge/judge abandon. Projects not suitable for 7 days must adjust, must not mechanically apply.
- **30-day market reconnaissance** (when no clear project): W1 discover 3-5 problems daily no development -> W2 filter 5 -> W3 research evidence/competition/price/payment -> W4 choose 1-2 simplest problems validate with human+AI. Goal is not perfect project, but first real result.

## Three-Pool Maintenance (long-term running)

- **Result Pool**: what results can AI currently help people complete.
- **Demand Pool**: who needs what results.
- **Payment Pool**: who already pays for similar results.
Prioritize researching opportunities where "problem + existing solutions + existing payment behavior" all hold simultaneously.

## Stop Research Mechanism

When any of following occurs, proactively suggest stopping and output [not recommended to continue]:
- No real problem evidence.
- Only single accidental case.
- No repeated demand.
- No any solution market.
- No payment behavior.
- Users already have mature and satisfied solutions.
- AI cannot significantly reduce cost/time/skill barrier.
- Competition intensity far exceeds individual capability.
- MVP cannot quickly validate.
- Must invest large funds/team/development cycle.
- User themselves cannot reach target customers.

When stopping must explain: 1) why stop; 2) which evidence caused stop; 3) what new evidence in future can restart. Full version see `references/payment-validation.md` section stop mechanism.

## Avoid Research Addiction

When evidence already sufficient to support a low-cost validation (real problem + repeated demand + similar service charging + AI has clear leverage + user reachable + can do MVP at low cost):
- Stop continuing search.
- Output [research phase complete].
- Next step is [start real user validation], not continue finding new opportunities.

## Daily Observation Training

Train "person who watches content" into "person who observes demand":
"This is so troublesome" -> is this a problem? / "Any tool?" -> does demand exist? / "How much?" -> does payment signal exist? / "Must do every day" -> does repeated labor exist? / "I don't know how" -> does skill barrier exist? / "This software is too complex" -> does simplification opportunity exist?

## Reference Files (read as needed)

- `references/problem-framework.md` — Problem Card fields, problem ten categories, evidence grades, evidence-bound scoring (including Payment tiers), three-pool maintenance, commercial intuition training.
- `references/market-research.md` — three search types (Problem/Solution/Payment), reconnaissance sources, video reverse analysis, comment mining, competition and payment, 7-day/30-day modes, Deep Research.
- `references/payment-validation.md` — payment signals, payment scoring tiers, first payment execution checklist, validation metrics, stop mechanism (including restart conditions).
- `references/ai-solution-patterns.md` — Level 1-5 solutions, actionable solution checklist, tech stack requirements, MVP principles, downgrade rules, Sell Result First.
- `references/evidence-chain.md` — evidence chain five-segment, evidence types, confidence calibration, anti-jump rules (P0 new).
- `references/opportunity-state-machine.md` — Opportunity ID, delivery state machine HYPOTHESIS to ... to PRODUCTIZED, bottleneck advancement and cross-session resume rules.
- `references/demand-validation.md` — [v2.0 new] demand validation: demand strength 6 signals, three-layer users, substitution cost, payment reason chain JTBD, demand evidence credibility, demand conclusion three-choice (VALIDATE).
- `references/project-evaluation.md` — [v2.0 new] project evaluation: 7-dimension weighted, composite Opportunity Score 0-100 (recalculable), three-tier conclusion GO/VALIDATE_FIRST/NO_GO, competition landscape and differentiation, AI feasibility, Solo Fit, 7 fatal red flags (EVALUATE).
- `references/project-blueprint.md` — [v2.0 new] opportunity to project: product Level, core users, MoSCoW, MVP five items, tech direction, minimal validation experiment, differentiation落地 (BLUEPRINT, reuses Level 1-5).
- `references/monetization-gtm.md` — [v2.0 new] monetization & GTM: payer/ICP, Offer ladder, business model library, explainable pricing, first 10 customers, channel matrix, GTM three phases, no-build validation, MonetizationInput/Plan module contract (MONETIZE, can be independent).
- `references/pipeline-and-runtime.md` — [v2.0 new] five-stage pipeline orchestration, three code systems distinction, circuit breaking/fallback/resume from breakpoint, external call timeout/retry/failure degradation, output information hierarchy/bilingual/desktop-mobile/code area spec, pre-delivery acceptance checklist.
- `references/ui-rendering-spec.md` — [v2.0.0 new] output rendering and visual spec (Design System): verdict banner, stage progress bar, score bar, action buttons, Loading/Empty/Error/Success four states, mobile-first, long report reading experience, bilingual, code area, output self-check checklist.

## Templates (fill directly)

- `templates/problem-card.md` — problem card (includes evidence chain fields).
- `templates/evidence-card.md` — single evidence card (v1.1 new).
- `templates/opportunity-card.md` — opportunity card (includes Opportunity ID, state, evidence-bound scoring).
- `templates/quick-scan.md` — Quick Mode quick judgment (v1.1 new).
- `templates/market-report.md` — Market Scan complete report (FIND stage, includes three search types evidence and state).
- `templates/demand-validation-card.md` — [v2.0 new] demand validation card (VALIDATE).
- `templates/project-evaluation-card.md` — [v2.0 new] project evaluation card (EVALUATE, includes score table/formula/red flags).
- `templates/project-blueprint-card.md` — [v2.0 new] opportunity to project card (BLUEPRINT).
- `templates/monetization-gtm-card.md` — [v2.0 new] monetization & GTM card (MONETIZE, includes MonetizationPlan contract).
- `templates/opportunity-report.md` — [v2.0 new] final opportunity report (five-stage consolidation, conclusion-first).

## Examples (demonstrate workflow, data is illustrative)

- `examples/video-analysis.md` — video reverse market analysis (includes evidence chain).
- `examples/comment-analysis.md` — comment demand mining (includes three search types).
- `examples/real-world-problem.md` — complete v1.1 running example: Quick to Research (three search types+evidence chain) to Execution (first payment) + state machine advancement.
- `examples/full-pipeline-v2.md` — [v2.0 new] complete V2 pipeline example: FIND to VALIDATE to EVALUATE (includes recalculable score and "why 74 points is still VALIDATE_FIRST") to BLUEPRINT to MONETIZE (pricing/acquisition/first customers) to final conclusion.

## User Guide

`USER_GUIDE.md` is installation and usage guide for end users (not Agents): installation methods, version verification, trigger words, three modes, FAQ. When user asks "how to install / how to use / how to verify version / what trigger words", guide them to read `USER_GUIDE.md`.

# Market Scout User Guide (v2.0.0)

> This guide is for anyone who has the installation package: read "How to Install" first, then "How to Use". Check the FAQ at the end for questions.

## 1. What is this

**Market Scout v2.0.0** is an AI Agent Skill, not an "AI money-making project generator."
It walks you through a complete pipeline:

```
FIND: discover problems, collect evidence, validate demand/payment/competition/AI leverage
  to VALIDATE: is the demand real, strong, why would users pay
  to EVALUATE: composite scoring, clear verdict of worth doing / validate first / not recommended
  to BLUEPRINT: product form, core features, MVP, tech direction, minimal validation, differentiation
  to MONETIZE: who pays, what to sell, how to price, where to find customers, how first customers come
  to output an Opportunity Report: worth doing plus first step today
(after real launch) first payment to repeat purchase to standardization to automation to productization
```

In one sentence: starting from a vague idea or phenomenon, use real evidence to judge "is it worth doing", then give you a complete answer of "what to build, how to charge, where customers come from".

## 2. What can you use it for

- Throw out a phenomenon, quickly judge "worth researching" (Quick Mode)
- Deep-dive a market / analyze videos / analyze comment sections, output complete market report (Research Mode)
- Validate whether a demand is real, strong, whether users will pay (Demand Validation)
- Give an opportunity a composite score (0-100), directly give verdict and reasoning (Project Evaluation)
- Turn opportunity into project: what first version does, what not to do, what tech, how to validate with minimal cost (Opportunity to Project)
- Design how to make money: what to sell, how to charge, what price, where to acquire customers, how first 10 customers come (Monetization and GTM)
- Ready to launch: directly give "who to find, where to find, how to quote, how to get first order" (Execution Mode)
- Long-term opportunity tracking (Opportunity ID + state machine), no repeated research

## 3. How to install

You have two installation packages, identical content (same zip with different extension):
- market-scout.zip - generic archive
- market-scout.skill - skill package format

### Method 1: Drag-and-drop one-click install (recommended, fastest)
1. Open your AI client / Agent platform's "Skills" or "one-click install" entry point.
2. Drag market-scout.skill into it (if format not supported, drag market-scout.zip).
3. After success, go to section 4 to verify.

### Method 2: Manual place in skills directory
1. Unzip market-scout.zip, you get a market-scout folder.
2. Find your AI client's skills directory (commonly called .user_skills or skills).
3. Place the entire market-scout folder in it, ensuring path is:
   skills-directory/market-scout/SKILL.md (SKILL.md at folder root).
4. Restart / refresh client, then go to section 4 to verify.

> If you previously installed v1.1/v1.0: v2.0.0 is incremental and backward-compatible, but some platforms do not overwrite same-name folders. Recommend deleting old market-scout folder before installing new version.

## 4. How to confirm installation succeeded (important)

1. Open market-scout/SKILL.md after installation.
2. Search for two keywords: Monetization & GTM and GO (worth doing).
3. Both present = v2.0.0 latest installed; only FIRST_PAYMENT but not above two = still v1.1; neither found = old version, uninstall and reinstall.

## 5. How to start using

After installation, directly say any of the following to the AI:

| What you want to do | You can say |
|---|---|
| Quickly judge an idea | "School print shop always has people asking boss to edit PDF, any opportunity?" |
| Find market / direction | "Help me find a market" / "I want to do side hustle but no direction" |
| Analyze video / comments | "Analyze this video/comments, see if it can be a business" |
| Validate demand reality | "Is this demand real? Do users really want it?" |
| Evaluate worth doing | "Evaluate if this project is worth doing, give a score" |
| Turn opportunity into project | "Help me turn this idea into an MVP, what should first version do?" |
| Design how to make money | "How to charge? What price? How to design business model?" |
| Find first customers | "Where do first users/customers come from? How to acquire?" |
| Complete analysis end to end | "Help me complete analysis from discovery to monetization, output an opportunity report" |
| Ready to launch | "Help me get first order" / "I'm ready to do this" |

## 6. Relationship between five stages and three modes

- Five-stage pipeline (v2.0.0 main line): FIND to VALIDATE to EVALUATE to BLUEPRINT to MONETIZE, finally consolidated into one opportunity report. You can run from start, or enter directly from a stage (e.g. "I've validated demand, evaluate directly").
- Three work modes (v1.1 preserved):
  - Quick Mode: casual judgment, quick answer "worth continuing research".
  - Research Mode: output complete report when deep dive requested.
  - Execution Mode: when say "ready to do / get first order", stop research, directly give execution checklist.

## 7. How to read evaluation verdict (three tiers)

- GO (worth doing): high composite score, strong demand, clear payment evidence, no fatal risk - can invest, follow report actions.
- VALIDATE_FIRST (recommend validate before doing): looks good but key assumption (usually "will they pay") not yet proven - first do the minimal cheapest experiment in the report, if达标 go full, if not stop.
- NO_GO (not recommended): low composite score or triggered fatal red flag (no real demand / nobody will pay / AI no advantage / cannot reach customers / giant crushes etc.) - report also tells you why stopped, what new evidence can restart.

> Note: it will not force "worth doing" to make you happy. How score is calculated will be written clearly, you can verify yourself.

## 8. Three rules before use (must read)

1. Real-time search first: prioritize online search for real info (problems / existing solutions / payment behavior). When offline, will clearly mark "below is hypothetical analysis", will not pretend to have searched.
2. No fabrication: no made-up users, prices, transactions; conclusions without evidence only marked "hypothetical / to be validated".
3. Validate before building: default recommend "human + AI" deliver first, charge first, will not tell you to develop App/SaaS from start; v2.0.0 also does NOT include any payment, subscription, membership systems, only gives monetization plans.

## 9. File structure overview

```
market-scout/
├── SKILL.md                # Core: five-stage pipeline, modes, rules, decision tree
├── README.md               # Developer-facing documentation
├── USER_GUIDE.md           # This user guide
├── references/  (12)       # Methodology documents (discovery/evidence chain/demand validation/evaluation/blueprint/monetization etc.)
├── templates/   (10)       # Fill-in templates (stage cards + final opportunity report)
├── examples/    (4)        # Workflow examples (includes v2.0.0 complete five-stage case)
└── tools/                  # Package self-check script (can ignore for normal use)
```

## 10. FAQ

Q1: Installation says "format not supported"?
Try the other package (.skill to .zip or vice versa); if still fails, use Method 2 manual placement.

Q2: Previously installed v1.1, will it conflict? Are v1.1 capabilities still there?
v2.0.0 is incremental upgrade, all v1.1 methods, templates, examples preserved. Some platforms do not overwrite same-name, recommend delete old folder first.

Q3: Are users and prices in examples real?
No. examples/ are all demonstration illustrative data, only show methodology. Real use will online search real-time evidence.

Q4: Must be online?
Recommended online (evidence real). Offline can also give hypothesis-based analysis, but all conclusions marked "hypothetical", cannot be treated as market facts.

Q5: Will it help me build payment/membership systems?
No. v2.0.0 explicitly does not develop payment, subscription, membership, only outputs "how to price, how to charge, how to acquire" plans and validation actions. Monetization module designed to potentially become standalone product in future, but current version has no transaction system.

Q6: Can I modify this skill?
Yes, all are plain Markdown text (plus one optional Python self-check script), directly edit; after editing, place back in skills directory per Method 2 to take effect.

## 11. Copyright and usage

This skill can be freely used, forwarded, uploaded to GitHub for personal learning and side-hustle exploration. Content is original methodology documentation, no third-party commercial assets. Do not use to generate or spread false marketing information.

# Changelog

All notable changes to Market Scout are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-09-03

### Added — Four new pipeline stages (Find to Validate to Evaluate to Monetize)

- Demand Validation: demand strength 6-signal synthesis (1-10), three-layer target users, substitution cost and pricing anchor, payment reason chain (JTBD 5 rings), demand evidence credibility matrix
- Project Evaluation: 7-dimension weighted scoring (Demand 20% / Market 20% / Competition and Differentiation 15% / AI Feasibility 15% / Development Difficulty 10% / Solo Fit 15% / Risk 5%), composite Opportunity Score 0-100 (hand-recalculable formula), 7 fatal red flags (one-vote veto), three-tier verdict GO / VALIDATE_FIRST / NO_GO
- Opportunity to Project: product form (aligned with Level 1-5), MoSCoW feature prioritization, MVP five items, recommended tech direction, minimal validation experiment, differentiation entry point
- Monetization and GTM: Target Customer (distinguishes user from payer), Offer three-tier ladder, Business Model library, explainable Pricing, first 10 customers acquisition, channel matrix, GTM three phases, 7 no-build validation methods
- Modular data contract: MonetizationInput / MonetizationPlan defined for future standalone product without major refactoring

### Added — Pipeline and Runtime

- Five-stage pipeline orchestration, three independent code systems (evidence grade A/B/C / delivery state machine / pipeline stage), stage circuit breaker and fallback, resume from breakpoint
- Runtime robustness spec: unified timeout for external search/API/sub-agent calls, bounded retry with exponential backoff for transient errors, graded failure fallback (switch source to use user material to mark insufficient evidence), no retry for deterministic errors

### Added — UI and UX

- Unified output rendering spec (Design System): verdict banner, stage progress bar, 10-cell score bar, action buttons, Loading/Empty/Error/Success four state templates, mobile-first (tables max 6 columns, narrow-screen key-value lists), desktop information density, long report table of contents and per-stage summary, bilingual spec, code block format, output self-check checklist
- All v2 stage cards and report templates unified with top verdict banner, stage progress bar, and bottom action buttons

### Added — Final Report and Full Example

- Final opportunity report: five-stage consolidated report, conclusion-first, understandable in 10 seconds
- Complete five-stage example (local tutoring studio customer acquisition content service), with reproducible score (74/100), demonstrating high score can still be VALIDATE_FIRST, pricing and first-customer acquisition

### Added — Open Source Release Assets

- README rewritten as open-source product landing page
- CHANGELOG, LICENSE (MIT), CONTRIBUTING, .gitignore
- website/index.html product landing page (GitHub Pages ready)

### Changed

- SKILL.md version upgraded to v2.0.0, added V2 main pipeline, four capability summaries, monetization module independence, three code systems distinction, output and UI spec, v2 trigger words
- opportunity-card.md incrementally upgraded to v2, compatible with all v1.1 fields, added Pipeline Stage, composite score, three-tier verdict, five-stage navigation
- USER_GUIDE.md updated to v2.0.0

### Notes

- All v1.x capabilities preserved (three search types, evidence chain, three modes, 8-dimension scoring, Level 1-5, delivery state machine, stop mechanism, first-payment checklist)
- Currently does not implement payment, subscription, membership, or billing systems
- This is a pure Markdown documentation Agent Skill, no frontend code, build chain, or database

---

## [1.1.0] - 2026 (previous)

### Added
- Evidence Chain mechanism
- Problem / Solution / Payment three search types
- Quick / Research / Execution three work modes
- Opportunity delivery state machine
- Evidence-bound scoring
- Stop research mechanism with restart conditions
- evidence-card.md, quick-scan.md templates
- evidence-chain.md, opportunity-state-machine.md references
- real-world-problem.md complete workflow example

## [1.0.0] - 2026 (initial)

### Added
- Market Scan, Problem Card, 8-dimension scoring
- Level 1-5 solution grading
- 7-day / 30-day validation modes
- Three-pool maintenance
- Video / comment reverse market analysis

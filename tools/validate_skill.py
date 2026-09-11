#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Market Scout skill package self-check (v5.0.0).

Usage:
    python tools/validate_skill.py [skill_dir] [--dev|--release]

Modes:
    --dev       (default) development validation: skill files, specialists,
                context, routing, state, schemas, scripts, local tests.
                Release artifact (releases/*.zip) is NOT required in dev mode.
    --release   release validation: everything in dev mode PLUS the release
                artifact must exist in releases/.

Note: the release zip is a publish-phase artifact; it lives in releases/ of
the source tree and is intentionally NOT nested inside the install package.
Running the check on an extracted package is therefore only meaningful in
dev mode (package content is verified by byte-exact comparison instead).

Checks:
  1. File manifest completeness (all expected files exist, incl. release assets).
  2. SKILL.md YAML frontmatter (name / description).
  3. Cross references: every `references|templates|examples/<file>.md`
     cited in any markdown actually exists.
  4. Required sections/fields inside v2 + v3 cards/templates.
  5. Version consistency on top-level docs (v4.0.0 across SKILL/USER_GUIDE/README).
  6. UI rendering spec anchors in v2 templates (verdict banner / pipeline bar / action).
  7. Open-source release assets (CHANGELOG / LICENSE / CONTRIBUTING / .gitignore / website).
  8. V5 Orchestrator layer (orchestrator/* + specialists/* + v5 template/examples/tests).
  9. V5 state machine (9 states) & unified context contract fields.
  10. V5 routing modes & priority chain (Focused Intent > Existing State > Full Workflow).
  11. Release artifact check only in --release mode.
Exit code 0 = all passed; 1 = errors found.
"""
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ---- Expected manifest -------------------------------------------------------
EXPECTED = [
    "SKILL.md", "README.md", "USER_GUIDE.md",
    "references/problem-framework.md",
    "references/market-research.md",
    "references/payment-validation.md",
    "references/ai-solution-patterns.md",
    "references/evidence-chain.md",
    "references/opportunity-state-machine.md",
    "references/demand-validation.md",
    "references/project-evaluation.md",
    "references/project-blueprint.md",
    "references/monetization-gtm.md",
    "references/pipeline-and-runtime.md",
    "references/ui-rendering-spec.md",
    "CHANGELOG.md", "LICENSE", "CONTRIBUTING.md", ".gitignore",
    "website/index.html",
    "templates/problem-card.md",
    "templates/evidence-card.md",
    "templates/opportunity-card.md",
    "templates/quick-scan.md",
    "templates/market-report.md",
    "templates/demand-validation-card.md",
    "templates/project-evaluation-card.md",
    "templates/project-blueprint-card.md",
    "templates/monetization-gtm-card.md",
    "templates/opportunity-report.md",
    "examples/video-analysis.md",
    "examples/comment-analysis.md",
    "examples/real-world-problem.md",
    "examples/full-pipeline-v2.md",
    "references/v3-overview.md",
    "references/v3-evidence.md",
    "references/v3-scoring.md",
    "references/v3-decision.md",
    "references/v3-mvp.md",
    "references/v3-action-plan.md",
    "templates/v3-evidence-board.md",
    "templates/v3-score-card.md",
    "templates/v3-decision-card.md",
    "templates/v3-mvp-card.md",
    "templates/v3-action-plan-card.md",
    "templates/v3-report.md",
    "examples/v3-decision-run.md",
    "examples/v3-crowded-market.md",
    "references/v3-scoring-rubric.md",
    "references/v3-evidence-coverage.md",
    "references/v3-confidence.md",
    "references/v3-hard-gates.md",
    "examples/v3-1-high-score-low-confidence.md",
    "examples/v3-1-hard-gate-score-ceiling.md",
    "examples/v3-1-evidence-driven-action.md",
    "tools/validate_skill.py",
    "tools/test_v31_cases.py",
    "references/v4-validation.md",
    "templates/v4-validation-card.md",
    "examples/v4-validation-plan.md",
    "examples/v4-lowest-cost-validation.md",
    "examples/v4-validation-result.md",
    "examples/v4-re-evaluation.md",
    "tools/test_v4_validation.py",
    "orchestrator/architecture.md",
    "orchestrator/routing.md",
    "orchestrator/state.md",
    "orchestrator/context.md",
    "specialists/idea-observer.md",
    "specialists/problem-scout.md",
    "specialists/evidence-hunter.md",
    "specialists/opportunity-scout.md",
    "specialists/opportunity-score.md",
    "specialists/validation-scout.md",
    "templates/v5-context-card.md",
    "examples/v5-orchestrator-full-run.md",
    "examples/v5-focused-evidence-hunter.md",
    "examples/v5-mid-entry-scoring.md",
    "tools/test_v5_orchestrator.py",
    "tools/test_v5_e2e.py",
    "tools/verify_source_sync.py",
]

# Release-phase artifacts (only required in --release mode; publish stage)
RELEASE_EXPECTED = [
    "releases/market-scout-v5.0.0.zip",
]

# ---- Required keywords per v2 artifact (must ALL appear) ---------------------
REQUIRED_KEYWORDS = {
    "SKILL.md": ["Find 发现", "VALIDATE", "EVALUATE", "BLUEPRINT", "MONETIZE",
                 "值得做 GO", "建议验证后再做", "不建议做 NO-GO",
                 "demand-validation.md", "project-evaluation.md",
                 "project-blueprint.md", "monetization-gtm.md", "pipeline-and-runtime.md"],
    "references/demand-validation.md": ["需求强度", "付费理由链", "核心用户", "Demand Strength"],
    "references/project-evaluation.md": ["综合机会评分", "权重", "GO", "VALIDATE_FIRST",
                                          "NO-GO", "红旗", "Opportunity Score"],
    "references/project-blueprint.md": ["MoSCoW", "MVP", "Level", "最小验证"],
    "references/monetization-gtm.md": ["Target Customer", "Business Model", "Pricing",
                                       "MonetizationInput", "MonetizationPlan", "第一批"],
    "references/pipeline-and-runtime.md": ["超时", "重试", "降级", "断点续跑", "双语"],
    "references/ui-rendering-spec.md": ["结论带", "阶段进度条", "Loading", "Empty", "Error", "Success", "移动端", "分数条"],
    "CHANGELOG.md": ["2.0.0", "Added", "Demand Validation", "Project Evaluation", "Monetization"],
    "website/index.html": ["Market Scout", "Find", "Validate", "Evaluate", "Monetize", "v4.0.0", "Validation"],
    "templates/demand-validation-card.md": ["需求强度", "付费理由链", "VALIDATE"],
    "templates/project-evaluation-card.md": ["综合机会评分", "权重", "计算式", "红旗", "GO"],
    "templates/project-blueprint-card.md": ["MoSCoW", "MVP", "BLUEPRINT"],
    "templates/monetization-gtm-card.md": ["Business Model", "Pricing", "MonetizationPlan", "MONETIZE"],
    "templates/opportunity-report.md": ["FIND", "VALIDATE", "EVALUATE", "BLUEPRINT", "MONETIZE", "Verdict"],
    "templates/opportunity-card.md": ["Pipeline Stage", "Opportunity Score", "值得做 GO"],
    "examples/full-pipeline-v2.md": ["74", "VALIDATE", "EVALUATE", "BLUEPRINT", "MONETIZE", "MonetizationPlan"],
    "README.md": ["v4.0.0", "Find", "Validate", "Evaluate", "Monetize", "Decision",
                  "RECOMMENDED", "POTENTIAL", "NOT_RECOMMENDED", "Roadmap", "License",
                  "validate_skill.py", "releases/market-scout-v4.0.0.zip", "Validation Engine"],
    "USER_GUIDE.md": ["v2.0.0", "值得做 GO", "Monetization & GTM"],
}

# ---- Required keywords for v3 artifacts (merged into REQUIRED_KEYWORDS) ------
V3_REQUIRED_KEYWORDS = {
    "SKILL.md": ["v3.0.0", "V3 决策层", "RECOMMENDED", "POTENTIAL", "NOT_RECOMMENDED", "v3-overview.md"],
    "references/v3-overview.md": ["V3Input", "V3Output", "Evidence", "RECOMMENDED", "验收清单"],
    "references/v3-evidence.md": ["Evidence", "Inference", "Unknown", "Sufficient", "Insufficient", "不编造"],
    "references/v3-scoring.md": ["需求强度", "痛点强度", "竞争与切入空间", "变现潜力", "开发可行性", "获客难度", "AI Advantage", "切入空间", "红旗"],
    "references/v3-decision.md": ["RECOMMENDED", "POTENTIAL", "NOT_RECOMMENDED", "Why", "VALIDATE_FIRST"],
    "references/v3-mvp.md": ["Product", "Target User", "Core Problem", "Core Value", "Must Have", "Do Not Build", "Recommended Stack"],
    "references/v3-action-plan.md": ["B2B_TOOL", "CONSUMER_TOOL", "AI_AGENT", "LOCAL_SERVICE", "DIGITAL_PRODUCT", "今天做什么"],
    "CHANGELOG.md": ["3.0.0", "决策层", "Opportunity Score", "MVP Blueprint", "Action Plan"],
    "templates/v3-evidence-board.md": ["Evidence", "Inference", "Unknown", "充分度"],
    "templates/v3-score-card.md": ["计算式", "百分条", "切入空间", "红旗"],
    "templates/v3-decision-card.md": ["RECOMMENDED", "Why", "下一步承诺"],
    "templates/v3-mvp-card.md": ["Product", "Must Have", "Do Not Build", "Recommended Stack", "最小验证实验"],
    "templates/v3-action-plan-card.md": ["机会类型", "今天做什么", "第一笔钱路径"],
    "templates/v3-report.md": ["MARKET SCOUT V3", "Market Evidence", "Pain Point", "Competition", "MVP Blueprint", "Action Plan"],
    "examples/v3-decision-run.md": ["Opportunity Score", "Action Plan"],
    "examples/v3-crowded-market.md": ["切入空间", "Opportunity Score"],
    "USER_GUIDE.md": ["v3.0.0", "RECOMMENDED", "18 个", "16 个"],
}
for _k, _v in V3_REQUIRED_KEYWORDS.items():
    REQUIRED_KEYWORDS.setdefault(_k, []).extend(_v)

# ---- Required keywords for v3.1 artifacts ------------------------------------
V3_1_REQUIRED_KEYWORDS = {
    "SKILL.md": ["v3.1.0", "Score Rubric", "Confidence", "Hard Gates", "Evidence Coverage",
                 "Evidence-driven Action", "v3-scoring-rubric.md", "v3-hard-gates.md"],
    "references/v3-scoring-rubric.md": ["rubric_band", "1-2", "9-10", "防调规则", "D1 需求真实性", "A4 相对替代方案的优势"],
    "references/v3-evidence-coverage.md": ["Problem", "Solution", "Payment", "Competition", "Distribution", "Buildability",
                                            "overall", "critical_gaps", "来源独立性", "去重"],
    "references/v3-confidence.md": ["Confidence Score", "0.30", "0.20", "0.35", "0.15", "High", "Medium", "Low", "可复算", "Unknown 与 Low"],
    "references/v3-hard-gates.md": ["Hard Gate", "Score Ceiling", "Red Flag", "< 45", "< 40", "< 35", "< 30", "score_ceiling"],
    "references/v3-action-plan.md": ["Evidence-driven Action", "Evidence Basis", "Fallback", "动词 + 对象 + 数量"],
    "references/v3-overview.md": ["evidence_coverage", "hard_gates", "4.5", "V3.1 强化层"],
    "CHANGELOG.md": ["3.1.0", "Score Rubric", "决策置信度", "Hard Gates", "Evidence Coverage", "Evidence-driven Action"],
    "templates/v3-score-card.md": ["档 <1-2/3-4/5-6/7-8/9-10>", "Evidence Coverage", "Confidence", "Hard Gates"],
    "templates/v3-decision-card.md": ["Confidence", "Coverage", "Hard Gates", "score_ceiling"],
    "templates/v3-action-plan-card.md": ["Evidence Basis", "动词 + 对象 + 数量 + 成功标准", "Fallback"],
    "templates/v3-report.md": ["Confidence", "Coverage", "Hard Gates", "Evidence Basis"],
    "examples/v3-1-high-score-low-confidence.md": ["85", "Confidence", "Low", "POTENTIAL"],
    "examples/v3-1-hard-gate-score-ceiling.md": ["Score Ceiling", "POTENTIAL", "Monetization"],
    "examples/v3-1-evidence-driven-action.md": ["Evidence-driven", "失败转向", "Today", "Evidence Basis", "payment_signal"],
    "USER_GUIDE.md": ["v3.1.0", "五层强化", "23)"],
}
for _k, _v in V3_1_REQUIRED_KEYWORDS.items():
    REQUIRED_KEYWORDS.setdefault(_k, []).extend(_v)

# ---- Required keywords for v5 artifacts -------------------------------------
V5_REQUIRED_KEYWORDS = {
    "SKILL.md": ["v5.0.0", "V5 Orchestrator", "状态路由", "MarketScoutContext",
                 "Idea Observer", "Problem Scout", "Evidence Hunter",
                 "Opportunity Scout", "Opportunity Score", "Validation Scout",
                 "BUILD", "PARK", "KILL", "orchestrator/routing.md",
                 "specialists/idea-observer.md", "templates/v5-context-card.md"],
    "orchestrator/architecture.md": ["Orchestrator", "Full Mode", "Routing",
                                     "MarketScoutContext", "BUILD", "VALIDATE",
                                     "RESEARCH", "PARK", "KILL", "有停手权"],
    "orchestrator/routing.md": ["State Detection", "Intent Detection", "Full Mode",
                                "Focused Mode", "Mid-workflow", "中途进入",
                                "Independent", "降级", "空输入", "模糊输入",
                                "超长输入", "信息冲突", "搜索无结果", "上下文缺失",
                                "Specialist 执行失败", "重复调用", "阶段已经完成",
                                "Validation 无法进行", "路由优先级",
                                "Explicit Focused", "Existing Context",
                                "Full Workflow", "继续", "接着上次",
                                "MISSING_INPUT", "Main Orchestrator 是唯一的流程调度者"],
    "orchestrator/state.md": ["IDEA", "OBSERVATION", "PROBLEM", "EVIDENCE",
                              "OPPORTUNITY", "SCORED", "VALIDATION", "DECISION",
                              "ACTION", "State Recovery", "允许前进跳步",
                              "禁止无依据回退"],
    "orchestrator/context.md": ["context_version", "opportunity_id", "mode", "state",
                                "history", "idea", "observation", "problem",
                                "evidence", "opportunity", "criteria", "score",
                                "validation", "decision", "action", "assumptions",
                                "unknowns", "sources", "confidence", "Evidence Reuse",
                                "orchestration_mode", "V4 Mode",
                                "V5 Orchestration Mode"],
    "orchestrator/routing.md": ["V4 Mode", "V5 Orchestration Mode",
                                "怎么进入和调度", "工作方式"],
    "templates/v5-context-card.md": ["state", "history", "verdict", "BUILD",
                                     "PARK", "KILL", "today"],
    "examples/v5-orchestrator-full-run.md": ["IDEA", "OBSERVATION", "PROBLEM",
                                             "EVIDENCE", "OPPORTUNITY", "SCORED",
                                             "VALIDATION", "DECISION", "ACTION",
                                             "今天做什么"],
    "examples/v5-focused-evidence-hunter.md": ["Evidence Hunter", "Problem Search",
                                               "Solution Search", "Payment Search",
                                               "未重跑"],
    "examples/v5-mid-entry-scoring.md": ["MID-ENTRY", "未重跑", "Evidence Reuse",
                                         "RECOMMENDED"],
    "CHANGELOG.md": ["5.0.0", "Orchestrator", "Specialist", "MarketScoutContext"],
    "tools/test_v5_orchestrator.py": ["case_a_full_pipeline", "case_b_mid_entry",
                                      "case_c_focused_mode", "case_d_independent_specialists",
                                      "case_e_stop_rights", "case_f_edge_cases",
                                      "case_g_v4_preserved"],
    "tools/test_v5_e2e.py": ["case_e2e01_full_new_idea", "case_e2e02_evidence_only",
                             "case_e2e03_problem_exists", "case_e2e04_evidence_exists",
                             "case_e2e05_score_only", "case_e2e06_validation_only",
                             "case_e2e07_continue_last", "case_e2e08_low_quality",
                             "case_r1_context_write_back", "case_r2_priority_and_backfill",
                             "case_r3_boundaries", "case_r4_mode_boundary"],
    "tools/verify_source_sync.py": ["verify_source_sync", "worktree", "package",
                                    "PASS", "FAIL", "releases/"],
}
for _k, _v in V5_REQUIRED_KEYWORDS.items():
    REQUIRED_KEYWORDS.setdefault(_k, []).extend(_v)



# v2 templates that must follow UI rendering spec (verdict banner + pipeline bar + action)
UI_SPEC_TEMPLATES = [
    "templates/demand-validation-card.md",
    "templates/project-evaluation-card.md",
    "templates/project-blueprint-card.md",
    "templates/monetization-gtm-card.md",
    "templates/opportunity-report.md",
]
UI_SPEC_CHECKS = {
    "verdict_banner": lambda t: "> **" in t,  # quote-block banner
    "pipeline_bar": lambda t: "FIND " in t and ("✅" in t or "🔄" in t or "⏳" in t),
    "action_button": lambda t: "👉" in t or "下一步" in t,
}

# v1.1 artifacts that must remain (non-destruction guarantee)
V3_UI_SPEC_TEMPLATES = [
    "templates/v3-score-card.md",
    "templates/v3-decision-card.md",
    "templates/v3-mvp-card.md",
    "templates/v3-action-plan-card.md",
    "templates/v3-report.md",
]
V3_UI_SPEC_CHECKS = {
    "action": lambda t: ("下一步" in t) or ("今天做什么" in t),
}
V3_VERDICT_TEMPLATES = ["templates/v3-decision-card.md", "templates/v3-report.md"]

LEGACY_MUST_KEEP = [
    "references/evidence-chain.md", "references/opportunity-state-machine.md",
    "templates/quick-scan.md", "templates/market-report.md",
    "examples/real-world-problem.md",
]

REF_PATTERN = re.compile(r"(?:references|templates|examples|orchestrator|specialists)/[A-Za-z0-9_\-]+\.md")
VERSION_TOP = {"SKILL.md": "v4.0.0", "USER_GUIDE.md": "v4.0.0", "README.md": "v4.0.0"}
VERSION_TOP_V5 = {"SKILL.md": "v5.0.0", "CHANGELOG.md": "5.0.0"}


def main() -> int:
    release_mode = "--release" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    root = Path(args[0]).resolve() if args else Path(__file__).resolve().parent.parent
    mode_label = "release mode" if release_mode else "dev mode"
    errors, warnings, passed = [], [], 0

    def ok(msg):
        nonlocal passed
        passed += 1

    # 1. manifest
    for rel in EXPECTED:
        p = root / rel
        if not p.exists():
            errors.append(f"[missing] {rel}")
        else:
            ok(f"exists: {rel}")
    for rel in RELEASE_EXPECTED:
        p = root / rel
        if release_mode:
            if p.exists():
                ok(f"exists (release): {rel}")
            else:
                errors.append(f"[missing][release] {rel} (required in --release mode)")
        else:
            if p.exists():
                ok(f"dev mode: release artifact present, checked: {rel}")
            else:
                ok("dev mode: release artifact check skipped (use --release at publish stage)")
    for rel in LEGACY_MUST_KEEP:
        if (root / rel).exists():
            ok(f"legacy kept: {rel}")
        else:
            errors.append(f"[legacy removed] {rel} must be preserved")

    # unexpected extra markdown files (informational)
    known = set(EXPECTED)
    for p in root.rglob("*.md"):
        rel = p.relative_to(root).as_posix()
        if rel not in known:
            warnings.append(f"[extra md] {rel} (not in manifest)")

    # 2. frontmatter
    skill = root / "SKILL.md"
    if skill.exists():
        head = skill.read_text(encoding="utf-8")[:800]
        if not re.search(r"^---\s*$", head, re.M):
            errors.append("[frontmatter] SKILL.md missing --- fences")
        if not re.search(r"^name:\s*market-scout\s*$", head, re.M):
            errors.append("[frontmatter] SKILL.md missing 'name: market-scout'")
        if not re.search(r"^description:\s*\S+", head, re.M):
            errors.append("[frontmatter] SKILL.md missing description")
        else:
            ok("frontmatter name/description present")

    # 2b. template placeholder residue scan (v4.0.0 cleanup rule)
    placeholder_tokens = ("__BT__", "__XX__")
    for pf in list(root.rglob("*.md")) + list(root.rglob("*.py")) + list(root.rglob("*.html")):
        if pf.name == "validate_skill.py":   # 检查器自身包含关键词定义，跳过
            continue
        try:
            pt = pf.read_text(encoding="utf-8")
        except Exception:
            continue
        for tok in placeholder_tokens:
            if tok in pt:
                errors.append(f"[placeholder] {pf.relative_to(root).as_posix()} contains {tok!r} (residue, must fix)")
    ok("placeholder residue scan done")

    # 3. cross references across all markdown
    md_files = list(root.rglob("*.md"))
    for p in md_files:
        text = p.read_text(encoding="utf-8")
        for ref in set(REF_PATTERN.findall(text)):
            if not (root / ref).exists():
                errors.append(f"[dangling ref] {p.relative_to(root).as_posix()} -> {ref}")
    ok(f"cross references scanned in {len(md_files)} markdown files")

    # 4. required keywords
    for rel, words in REQUIRED_KEYWORDS.items():
        p = root / rel
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8")
        for w in words:
            if w in text:
                ok(f"{rel} contains '{w}'")
            else:
                errors.append(f"[missing keyword] {rel} -> '{w}'")

    # 5. version consistency on top docs
    for rel, ver in VERSION_TOP.items():
        p = root / rel
        if p.exists():
            head_text = p.read_text(encoding="utf-8")
            if ver in head_text:
                ok(f"{rel} version {ver}")
            else:
                errors.append(f"[version] {rel} heading missing {ver}")
    for rel, ver in VERSION_TOP_V5.items():
        p = root / rel
        if p.exists():
            head_text = p.read_text(encoding="utf-8")
            if ver in head_text:
                ok(f"{rel} version {ver} (v5)")
            else:
                errors.append(f"[version] {rel} heading missing {ver}")

    # 6. weight sanity: evaluation weights sum to 100%
    ev = root / "references/project-evaluation.md"
    if ev.exists():
        weights = [float(x) for x in re.findall(r"(\d+)%", ev.read_text(encoding="utf-8"))]
        # the seven dimension weights are the first seven percent tokens
        seven = weights[:7]
        if len(seven) == 7 and abs(sum(seven) - 100.0) < 1e-9:
            ok("evaluation 7-dimension weights sum to 100%")
        else:
            errors.append(f"[weights] first-7 weights = {seven}, sum != 100%")

    # 7. UI rendering spec: v2 templates must have verdict banner + pipeline bar + action
    for rel in UI_SPEC_TEMPLATES:
        p = root / rel
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8")
        for check_name, check_fn in UI_SPEC_CHECKS.items():
            if check_fn(text):
                ok(f"{rel} UI spec: {check_name}")
            else:
                errors.append(f"[ui-spec] {rel} missing '{check_name}' (see references/ui-rendering-spec.md)")

    # 8. UI rendering spec: v3 templates must have action; decision card + report must have verdict banner
    for rel in V3_UI_SPEC_TEMPLATES:
        p = root / rel
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8")
        for check_name, check_fn in V3_UI_SPEC_CHECKS.items():
            if check_fn(text):
                ok(f"{rel} V3 UI spec: {check_name}")
            else:
                errors.append(f"[v3-ui-spec] {rel} missing {check_name!r} (see references/ui-rendering-spec.md)")
    for rel in V3_VERDICT_TEMPLATES:
        p = root / rel
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8")
        if "> **" in text and any(x in text for x in ("RECOMMENDED", "POTENTIAL", "NOT_RECOMMENDED")):
            ok(f"{rel} V3 UI spec: verdict_banner")
        else:
            errors.append(f"[v3-ui-spec] {rel} missing verdict_banner (see references/ui-rendering-spec.md)")

    # 10. v3.1 rubric: 26 sub-signal sections present
    rb = root / "references/v3-scoring-rubric.md"
    if rb.exists():
        text = rb.read_text(encoding="utf-8")
        codes = ["D1","D2","D3","D4","P1","P2","P3","C1","C2","C3","C4",
                 "M1","M2","M3","M4","B1","B2","B3","B4",
                 "D1 渠道可触达","D2 用户聚集度","D3 内容","D4 获客成本",
                 "A1","A2","A3","A4"]
        missing = [c for c in codes if ("### " + c) not in text]
        if missing:
            errors.append(f"[v3.1-rubric] missing sub-signal sections: {missing}")
        else:
            ok("v3.1 rubric 26 sub-signal sections present")

    # 11. v3.1 confidence formula tokens
    cf = root / "references/v3-confidence.md"
    if cf.exists():
        text = cf.read_text(encoding="utf-8")
        for token in ("0.30 × coverage", "0.20 × (1 − U) × 100", "0.35 × CC", "0.15 × independent_ok", "High ≥ 70"):
            if token in text:
                ok(f"v3.1 confidence formula token: {token}")
            else:
                errors.append(f"[v3.1-confidence] missing formula token: {token!r}")

    # 12. v3.1 hard gate thresholds
    hg = root / "references/v3-hard-gates.md"
    if hg.exists():
        text = hg.read_text(encoding="utf-8")
        for token in ("< 45", "< 40", "< 35", "< 30", "score_ceiling"):
            if token in text:
                ok(f"v3.1 hard gate token: {token}")
            else:
                errors.append(f"[v3.1-hard-gates] missing token: {token!r}")

    # 13. v3.1 coverage dimensions
    cv = root / "references/v3-evidence-coverage.md"
    if cv.exists():
        text = cv.read_text(encoding="utf-8")
        for d in ("problem", "solution", "payment", "competition", "distribution", "buildability"):
            if d in text:
                ok(f"v3.1 coverage dimension: {d}")
            else:
                errors.append(f"[v3.1-coverage] missing dimension: {d}")

    # 15. v4 validation structure: 11-plan fields + R1-R5 rules present
    vv = root / "references/v4-validation.md"
    if vv.exists():
        text = vv.read_text(encoding="utf-8")
        fields = ["core_hypothesis", "target_user", "channel", "sample_size", "duration",
                  "estimated_cost", "success_criteria", "failure_criteria", "decision_rule", "next_state"]
        missing = [f for f in fields if f not in text]
        for tok in ("R1 ", "R2 ", "R3 ", "R4 ", "R5 "):
            if tok in text:
                ok(f"v4 re-eval rule: {tok.strip()}")
            else:
                errors.append(f"[v4-validation] missing rule token: {tok!r}")
        if missing:
            errors.append(f"[v4-validation] missing plan fields: {missing}")
        else:
            ok("v4 validation plan fields present")

    # 16. weight sanity: v3 opportunity score weights sum to 100%
    sv = root / "references/v3-scoring.md"
    if sv.exists():
        weights = [float(x) for x in re.findall(r"(\d+)%", sv.read_text(encoding="utf-8"))]
        seven = weights[:7]
        if len(seven) == 7 and abs(sum(seven) - 100.0) < 1e-9:
            ok("v3 7-dimension weights sum to 100%")
        else:
            errors.append(f"[weights] v3 first-7 weights = {seven}, sum != 100%")

    # 17. v5 specialists: frontmatter + contract sections
    SPECIALIST_RELS = [
        "specialists/idea-observer.md", "specialists/problem-scout.md",
        "specialists/evidence-hunter.md", "specialists/opportunity-scout.md",
        "specialists/opportunity-score.md", "specialists/validation-scout.md",
    ]
    SPECIALIST_SECTIONS = ["输入契约", "输出契约", "执行方法", "质量铁律", "独立调用", "被 Main 调度"]
    for rel in SPECIALIST_RELS:
        p = root / rel
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8")
        head = text[:400]
        if "---" in head and "name:" in head and "description:" in head:
            ok(f"v5 specialist frontmatter: {rel}")
        else:
            errors.append(f"[v5-specialist] {rel} missing frontmatter (name/description)")
        for sec in SPECIALIST_SECTIONS:
            if sec in text:
                ok(f"{rel} section: {sec}")
            else:
                errors.append(f"[v5-specialist] {rel} missing section '{sec}'")

    # 18. v5 state machine: 9 states present
    sm = root / "orchestrator/state.md"
    if sm.exists():
        text = sm.read_text(encoding="utf-8")
        states = ["IDEA", "OBSERVATION", "PROBLEM", "EVIDENCE", "OPPORTUNITY",
                  "SCORED", "VALIDATION", "DECISION", "ACTION"]
        missing = [s for s in states if s not in text]
        if missing:
            errors.append(f"[v5-state] missing states: {missing}")
        else:
            ok("v5 state machine 9 states present")
        for tok in ("State Recovery", "允许前进跳步", "禁止无依据回退"):
            if tok in text:
                ok(f"v5 state rule: {tok}")
            else:
                errors.append(f"[v5-state] missing rule token: '{tok}'")

    # 19. v5 context contract fields
    ctx = root / "orchestrator/context.md"
    if ctx.exists():
        text = ctx.read_text(encoding="utf-8")
        fields = ["context_version", "opportunity_id", "mode", "state", "history",
                  "idea", "observation", "problem", "evidence", "opportunity",
                  "criteria", "score", "validation", "decision", "action",
                  "assumptions", "unknowns", "sources", "confidence"]
        missing = [f for f in fields if f not in text]
        if missing:
            errors.append(f"[v5-context] missing fields: {missing}")
        else:
            ok("v5 MarketScoutContext fields present")
        if "Evidence Reuse" in text and "State Reuse" in text:
            ok("v5 context reuse rules present")
        else:
            errors.append("[v5-context] missing reuse rules (Evidence Reuse / State Reuse)")

    # 20. v5 routing modes
    rt = root / "orchestrator/routing.md"
    if rt.exists():
        text = rt.read_text(encoding="utf-8")
        modes = ["Full Mode", "Focused Mode", "Mid-workflow", "中途进入", "Independent"]
        missing = [m for m in modes if m not in text]
        if missing:
            errors.append(f"[v5-routing] missing modes: {missing}")
        else:
            ok("v5 routing 4 modes present")

    # 21. v5 stop-rights verdicts
    ar = root / "orchestrator/architecture.md"
    if ar.exists():
        text = ar.read_text(encoding="utf-8")
        verdicts = ["BUILD", "VALIDATE", "RESEARCH", "PARK", "KILL"]
        missing = [v for v in verdicts if v not in text]
        if missing:
            errors.append(f"[v5-verdict] missing verdicts: {missing}")
        else:
            ok("v5 action verdicts BUILD/VALIDATE/RESEARCH/PARK/KILL present")

    # ---- report ----
    print("=" * 64)
    print(f"Market Scout skill self-check ({mode_label}) @ {root}")
    print("=" * 64)
    print(f"passed checks : {passed}")
    print(f"warnings      : {len(warnings)}")
    print(f"errors        : {len(errors)}")
    for w in warnings:
        print("  WARN " + w)
    for e in errors:
        print("  ERR  " + e)
    if not errors:
        print("\nRESULT: PASS ✅  (warnings are informational)")
        return 0
    print("\nRESULT: FAIL ❌")
    return 1


if __name__ == "__main__":
    sys.exit(main())

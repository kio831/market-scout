#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Market Scout skill package self-check (v3.0.0 release).

Usage:
    python tools/validate_skill.py [skill_dir]

Checks:
  1. File manifest completeness (all expected files exist, incl. release assets).
  2. SKILL.md YAML frontmatter (name / description).
  3. Cross references: every `references|templates|examples/<file>.md`
     cited in any markdown actually exists.
  4. Required sections/fields inside v2 + v3 cards/templates.
  5. Version consistency on top-level docs (v3.0.0 across SKILL/USER_GUIDE/README; website landing page is a v2-era asset kept as-is).
  6. UI rendering spec anchors in v2 templates (verdict banner / pipeline bar / action).
  7. Open-source release assets (CHANGELOG / LICENSE / CONTRIBUTING / .gitignore / website).
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
    "tools/validate_skill.py",
    "releases/market-scout-v3.0.0.zip",
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
    "website/index.html": ["Market Scout", "Find", "Validate", "Evaluate", "Monetize", "v2.0.0"],
    "templates/demand-validation-card.md": ["需求强度", "付费理由链", "VALIDATE"],
    "templates/project-evaluation-card.md": ["综合机会评分", "权重", "计算式", "红旗", "GO"],
    "templates/project-blueprint-card.md": ["MoSCoW", "MVP", "BLUEPRINT"],
    "templates/monetization-gtm-card.md": ["Business Model", "Pricing", "MonetizationPlan", "MONETIZE"],
    "templates/opportunity-report.md": ["FIND", "VALIDATE", "EVALUATE", "BLUEPRINT", "MONETIZE", "Verdict"],
    "templates/opportunity-card.md": ["Pipeline Stage", "Opportunity Score", "值得做 GO"],
    "examples/full-pipeline-v2.md": ["74", "VALIDATE", "EVALUATE", "BLUEPRINT", "MONETIZE", "MonetizationPlan"],
    "README.md": ["v3.0.0", "Find", "Validate", "Evaluate", "Monetize", "Decision",
                  "RECOMMENDED", "POTENTIAL", "NOT_RECOMMENDED", "Roadmap", "License",
                  "validate_skill.py", "releases/market-scout-v3.0.0.zip"],
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

REF_PATTERN = re.compile(r"(?:references|templates|examples)/[A-Za-z0-9_\-]+\.md")
VERSION_TOP = {"SKILL.md": "v3.0.0", "USER_GUIDE.md": "v3.0.0", "README.md": "v3.0.0"}


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
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
            head_text = p.read_text(encoding="utf-8")[:400]
            if ver in head_text:
                ok(f"{rel} version {ver}")
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

    # 9. weight sanity: v3 opportunity score weights sum to 100%
    sv = root / "references/v3-scoring.md"
    if sv.exists():
        weights = [float(x) for x in re.findall(r"(\d+)%", sv.read_text(encoding="utf-8"))]
        seven = weights[:7]
        if len(seven) == 7 and abs(sum(seven) - 100.0) < 1e-9:
            ok("v3 7-dimension weights sum to 100%")
        else:
            errors.append(f"[weights] v3 first-7 weights = {seven}, sum != 100%")

    # ---- report ----
    print("=" * 64)
    print(f"Market Scout skill self-check @ {root}")
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

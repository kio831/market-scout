#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Market Scout V5 — Orchestrator + Specialist 架构测试（SOP 十八、十九节）

覆盖：
  A. 完整流程：九态顺序与 Specialist 映射完整
  B. 中途进入：已有 Problem/Evidence 时跳过重复阶段
  C. 聚焦模式：意图 → Specialist 路由正确
  D. 独立 Specialist：每个子技能具备前后端契约与独立调用说明
  E. 停手权：PARK/KILL/RESEARCH/VALIDATE 与 V4 决策码映射，禁止强行 BUILD
  F. 异常处理：空输入/模糊/超长/冲突/无结果/缺上下文/失败/重复调用/已完成/验证不可行
  G. V4 非破坏：V4 既有文件清单全部保留

用法:  python tools/test_v5_orchestrator.py [skill_dir]
退出码 0 = 全过；1 = 有失败。
"""
import sys
from pathlib import Path

STATES = ["IDEA", "OBSERVATION", "PROBLEM", "EVIDENCE", "OPPORTUNITY", "SCORED",
          "VALIDATION", "DECISION", "ACTION"]
SPECIALISTS = {
    "idea-observer.md": "OBSERVATION",
    "problem-scout.md": "PROBLEM",
    "evidence-hunter.md": "EVIDENCE",
    "opportunity-scout.md": "OPPORTUNITY",
    "opportunity-score.md": "SCORED",
    "validation-scout.md": "VALIDATION",
}
VERDICTS = ["BUILD", "VALIDATE", "RESEARCH", "PARK", "KILL"]
EDGE_CASES = ["空输入", "模糊输入", "超长输入", "信息冲突", "搜索无结果",
              "上下文缺失", "Specialist 执行失败", "重复调用", "阶段已经完成",
              "Validation 无法进行"]


def read(p):
    return p.read_text(encoding="utf-8") if p.exists() else ""


def case_a_full_pipeline(root):
    problems = []
    sm = read(root / "orchestrator/state.md")
    for s in STATES:
        if s not in sm:
            problems.append("state.md missing " + s)
    for fn, out_state in SPECIALISTS.items():
        if out_state not in sm:
            problems.append("state.md missing producer mapping for " + fn)
    arch = read(root / "orchestrator/architecture.md")
    if "Full Mode" not in arch:
        problems.append("architecture.md missing Full Mode")
    for s in ("IDEA", "ACTION"):
        if s not in arch:
            problems.append("architecture.md missing state " + s)
    if problems:
        return "A", "FAIL", "; ".join(problems)
    return "A", "PASS", "九态顺序与 Specialist 映射完整（state.md + architecture.md）"


def case_b_mid_entry(root):
    problems = []
    routing = read(root / "orchestrator/routing.md")
    for token in ("不重跑已完成阶段", "不重复搜索已有证据", "Mid-workflow", "中途进入"):
        if token not in routing:
            problems.append("routing.md missing: " + token)
    state_md = read(root / "orchestrator/state.md")
    for token in ("允许前进跳步", "禁止无依据回退"):
        if token not in state_md:
            problems.append("state.md missing: " + token)
    ex = read(root / "examples/v5-mid-entry-scoring.md")
    if "未重跑 IDEA / OBSERVATION / EVIDENCE" not in ex:
        problems.append("mid-entry example missing skip self-check")
    if problems:
        return "B", "FAIL", "; ".join(problems)
    return "B", "PASS", "中途进入规则齐备（跳过已完成阶段、复用证据、跳步记录）"


def case_c_focused_mode(root):
    problems = []
    routing = read(root / "orchestrator/routing.md")
    mapping = {
        "帮我找这个问题的真实需求": "Evidence Hunter",
        "帮我重新评分": "Opportunity Score",
        "这个项目怎么验证": "Validation Scout",
        "帮我决策": "Main",
    }
    for intent, specialist in mapping.items():
        if intent not in routing or specialist not in routing:
            problems.append("routing.md missing focused mapping: " + intent)
    if "Focused Mode" not in routing and "FOCUSED" not in routing:
        problems.append("routing.md missing Focused Mode")
    if problems:
        return "C", "FAIL", "; ".join(problems)
    return "C", "PASS", "聚焦意图 → Specialist 映射完整（含 Main 直收决策意图）"


def case_d_independent_specialists(root):
    problems = []
    for fn in SPECIALISTS:
        p = root / "specialists" / fn
        text = read(p)
        head = text[:400]
        if "---" not in head or "name:" not in head or "description:" not in head:
            problems.append(fn + " missing frontmatter")
        for sec in ("输入契约", "输出契约", "执行方法", "质量铁律", "独立调用", "被 Main 调度"):
            if sec not in text:
                problems.append(fn + " missing section: " + sec)
    if problems:
        return "D", "FAIL", "; ".join(problems)
    return "D", "PASS", "6 个 Specialist 均具备 frontmatter + 前后端契约 + 独立调用 + Main 调度说明"


def case_e_stop_rights(root):
    problems = []
    arch = read(root / "orchestrator/architecture.md")
    for v in VERDICTS:
        if v not in arch:
            problems.append("architecture.md missing verdict " + v)
    for token in ("有停手权", "不强行制造机会", "PARK", "KILL"):
        if token not in arch:
            problems.append("architecture.md missing stop-rights token: " + token)
    if "NOT_RECOMMENDED" not in arch or "RECOMMENDED" not in arch:
        problems.append("architecture.md missing V4 decision codes")
    if problems:
        return "E", "FAIL", "; ".join(problems)
    return "E", "PASS", "停手权保留：五态裁决 + V4 三档决策码映射，禁止强行 BUILD"


def case_f_edge_cases(root):
    problems = []
    routing = read(root / "orchestrator/routing.md")
    for ec in EDGE_CASES:
        if ec not in routing:
            problems.append("routing.md missing edge case: " + ec)
    arch = read(root / "orchestrator/architecture.md")
    for token in ("降级", "Evidence Insufficient", "不编造"):
        if token not in arch:
            problems.append("architecture.md missing fallback token: " + token)
    sm = read(root / "orchestrator/state.md")
    for token in ("State Recovery", "无法确认", "不猜测"):
        if token not in sm:
            problems.append("state.md missing recovery token: " + token)
    if problems:
        return "F", "FAIL", "; ".join(problems)
    return "F", "PASS", "异常输入/降级/恢复/冲突/无结果规则齐备（routing + architecture + state）"


def case_g_v4_preserved(root):
    must_keep = [
        "SKILL.md", "references/evidence-chain.md", "references/market-research.md",
        "references/pipeline-and-runtime.md", "references/v3-scoring.md",
        "references/v3-scoring-rubric.md", "references/v4-validation.md",
        "templates/problem-card.md", "templates/v3-score-card.md",
        "templates/v4-validation-card.md", "templates/v3-report.md",
        "examples/v3-decision-run.md", "examples/v4-re-evaluation.md",
        "tools/validate_skill.py", "tools/test_v31_cases.py", "tools/test_v4_validation.py",
        "README.md", "USER_GUIDE.md", "CHANGELOG.md",
    ]
    missing = [r for r in must_keep if not (root / r).exists()]
    if missing:
        return "G", "FAIL", "V4 文件缺失: " + ", ".join(missing)
    return "G", "PASS", "V4 核心文件全部保留（%d 项）" % len(must_keep)


def main():
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
    cases = [case_a_full_pipeline(root), case_b_mid_entry(root), case_c_focused_mode(root),
             case_d_independent_specialists(root), case_e_stop_rights(root),
             case_f_edge_cases(root), case_g_v4_preserved(root)]
    print("=" * 72)
    print("Market Scout V5 orchestrator tests @", root)
    print("=" * 72)
    print("%-4s %-6s %s" % ("Case", "Status", "Evidence"))
    failures = 0
    for name, status, ev in cases:
        print("%-4s %-6s %s" % (name, status, ev))
        if status != "PASS":
            failures += 1
    if failures:
        print("RESULT: FAIL")
        return 1
    print("RESULT: PASS (V5 cases A-G)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

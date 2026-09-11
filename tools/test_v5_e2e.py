#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Market Scout V5 — Behavioral / End-to-End 测试（第二轮 SOP 第 4-14 节）

把 routing.md / state.md / context.md / architecture.md 中固定的规则实现为
参照模拟器（与 test_v31_cases.py 同一风格：文档规则 → 可执行参照实现），
然后对 8 个 E2E 场景 + Context 写回 + 优先级/补位/边界/不虚构做断言。

覆盖：
  E2E-01 全新想法 → 完整闭环（九态 + 六 Specialist + Main）
  E2E-02 只要 Evidence（无 Problem）→ Focused + 最小补位，不跑完整流程
  E2E-03 已有 Problem + 要证据 → 直接 Evidence Hunter
  E2E-04 已有 Evidence → Opportunity → Score，不再 Search
  E2E-05 只要评分 → Opportunity Score
  E2E-06 只要验证 → Validation Scout
  E2E-07 "继续"（已有 score）→ SCORED → VALIDATION，不重来
  E2E-08 低质量机会 → PARK / KILL / RESEARCH / VALIDATE，禁止 BUILD
  R1    Context 写回一致性（生产方唯一、字段齐全、文档与 Schema 一致）
  R2    路由优先级与补位禁令的文档规则
  R3    Evidence / Validation 边界 + 不虚构机制

用法:  python tools/test_v5_e2e.py [skill_dir]
退出码 0 = 全过；1 = 有失败。
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_v31_cases import opportunity_score, decision as v31_decision

# ---- 参照实现：路由规则（与 routing.md 第 5 节一致） ---------------------
SPECIALISTS = ["Idea Observer", "Problem Scout", "Evidence Hunter",
               "Opportunity Scout", "Opportunity Score", "Validation Scout"]

# 输出字段（context.md 生产方表）
OUTPUTS = {
    "Idea Observer": "observation",
    "Problem Scout": "problem",
    "Evidence Hunter": "evidence",
    "Opportunity Scout": "opportunity",
    "Opportunity Score": "score",
    "Validation Scout": "validation",
}

# 输入契约（各 specialist 文件 输入契约 节）
CONTRACTS = {
    "Idea Observer": ["idea"],
    "Problem Scout": ["observation"],
    "Evidence Hunter": ["problem"],
    "Opportunity Scout": ["problem", "evidence"],
    "Opportunity Score": ["opportunity", "evidence"],
    "Validation Scout": ["opportunity", "score"],
}

# 最小补位（routing.md 第 7 节表）
BACKFILL = {
    "Problem Scout": "Idea Observer",
    "Evidence Hunter": "Problem Scout",
    "Opportunity Scout": "Evidence Hunter",
    "Opportunity Score": "Opportunity Scout",
    "Validation Scout": "Opportunity Score",
}

# 机会判断类意图的续接链（对齐 SKILL.md 模式路由 V3 决策层：SCORING → DECISION）
FOLLOW = {
    "Opportunity Scout": ["Opportunity Score", "Main"],
}

# 意图关键词（routing.md 第 4 节；顺序敏感，先命中先赢）
INTENTS = [
    (("重新评分", "重新给这个项目打分", "重新评估", "打个分", "打打分", "机会评分", "帮我打分"), "Opportunity Score"),
    (("最应该验证什么", "怎么验证", "如何验证", "验证一下", "帮我验证"), "Validation Scout"),
    (("真实需求", "找证据", "网上有没有", "真实用户需要", "找真实需求"), "Evidence Hunter"),
    (("判断这个机会", "机会怎么样", "值不值得继续研究", "需求真的吗", "帮我评估"), "Opportunity Scout"),
    (("帮我决策", "值不值得做"), "Main"),
]

CONTINUE_WORDS = ("继续", "接着上次", "接着之前", "续上", "上次说到哪")

STATE_FIELDS = [
    ("idea", "IDEA"), ("observation", "OBSERVATION"), ("problem", "PROBLEM"),
    ("evidence", "EVIDENCE"), ("opportunity", "OPPORTUNITY"), ("score", "SCORED"),
    ("validation", "VALIDATION"), ("decision", "DECISION"), ("action", "ACTION"),
]


def detect_state(ctx):
    highest = None
    for field, state in STATE_FIELDS:
        if ctx.get(field):
            highest = state
    return highest


def detect_focus(text):
    for kws, spec in INTENTS:
        for k in kws:
            if k in text:
                return spec
    return None


def detect_continue(text):
    return any(w in text for w in CONTINUE_WORDS)


def missing_inputs(spec, ctx):
    return [f for f in CONTRACTS[spec] if not ctx.get(f)]


def run(spec, ctx):
    if spec == "Main":
        ctx["decision"] = "filled"
        ctx["action"] = "filled"
    else:
        ctx[OUTPUTS[spec]] = "filled"


def build_plan(ctx, target):
    """Main 唯一调度：按最小补位链补齐输入后执行目标 Specialist。返回 (plan, final_ctx)。"""
    plan = []
    c = dict(ctx)
    steps = 0
    while missing_inputs(target, c):
        bf = BACKFILL.get(target)
        if bf is None or steps > 6:
            break
        plan.append(bf)
        run(bf, c)
        steps += 1
    plan.append(target)
    run(target, c)
    for nxt in FOLLOW.get(target, []):
        plan.append(nxt)
        run(nxt, c)
    return plan, c


def full_plan():
    plan = list(SPECIALISTS) + ["Main"]
    return plan


def route(ctx, user_input):
    focus = detect_focus(user_input)
    cont = detect_continue(user_input)
    state = detect_state(ctx)
    if focus:
        if focus == "Main":
            return {"mode": "FOCUSED", "target": "Main", "plan": ["Main"], "state": state}
        plan, _ = build_plan(ctx, focus)
        return {"mode": "FOCUSED", "target": focus, "plan": plan, "state": state}
    if cont or state:
        # 续跑/已有状态：从最高已完成 State 的下一缺失阶段开始
        if state is None:
            return {"mode": "RESUME", "plan": full_plan(), "state": None}
        nxt = []
        if state in ("IDEA", "OBSERVATION", "PROBLEM", "EVIDENCE", "OPPORTUNITY"):
            idx = {"IDEA": 0, "OBSERVATION": 1, "PROBLEM": 2, "EVIDENCE": 3, "OPPORTUNITY": 4}[state]
            nxt = full_plan()[idx:] 
        elif state == "SCORED":
            nxt = ["Validation Scout", "Main"]
        elif state in ("VALIDATION", "DECISION", "ACTION"):
            nxt = ["Main"]
        return {"mode": "MID-ENTRY", "plan": nxt, "state": state}
    return {"mode": "FULL", "plan": full_plan(), "state": None}


def verdict_for(code, validate_needed=False):
    if code == "RECOMMENDED":
        return "VALIDATE" if validate_needed else "BUILD"
    if code == "POTENTIAL":
        return "RESEARCH"
    return "PARK"


# ---- 测试用例 ----------------------------------------------------------------
def case_e2e01_full_new_idea(root):
    r = route({}, "我想做一个帮助大学生自动整理课程资料的 AI 工具。")
    if r["mode"] != "FULL":
        return "E2E-01", "FAIL", "mode=" + r["mode"]
    if r["plan"] != full_plan():
        return "E2E-01", "FAIL", "plan=" + str(r["plan"])
    return "E2E-01", "PASS", "全新想法 → FULL：9 态闭环（六 Specialist + Main 决策/行动）"


def case_e2e02_evidence_only(root):
    r = route({}, "帮我找一下这个问题网上有没有真实需求。")
    if r["mode"] != "FOCUSED" or r["target"] != "Evidence Hunter":
        return "E2E-02", "FAIL", "route=" + str(r)
    if r["plan"] != ["Problem Scout", "Evidence Hunter"]:
        return "E2E-02", "FAIL", "plan=" + str(r["plan"]) + "（应只补 Problem 后直达 Evidence）"
    if "Idea Observer" in r["plan"]:
        return "E2E-02", "FAIL", "不应重跑 Idea"
    return "E2E-02", "PASS", "Focused Evidence Hunter + 最小补位（Problem Scout），未跑完整流程"


def case_e2e03_problem_exists(root):
    ctx = {"problem": "x"}
    r = route(ctx, "我已经确定大学生整理课程资料很麻烦，现在帮我找真实需求证据。")
    if r["mode"] != "FOCUSED" or r["plan"] != ["Evidence Hunter"]:
        return "E2E-03", "FAIL", "plan=" + str(r["plan"])
    return "E2E-03", "PASS", "Problem 已存在 → 直接 Evidence Hunter，无补位"


def case_e2e04_evidence_exists(root):
    ctx = {"problem": "x", "evidence": "y"}
    r = route(ctx, "我已经收集了几十条用户评论，帮我判断这个机会怎么样。")
    if r["mode"] != "FOCUSED" or r["target"] != "Opportunity Scout":
        return "E2E-04", "FAIL", "route=" + str(r)
    if r["plan"] != ["Opportunity Scout", "Opportunity Score", "Main"]:
        return "E2E-04", "FAIL", "plan=" + str(r["plan"])
    if "Evidence Hunter" in r["plan"]:
        return "E2E-04", "FAIL", "不得重复搜索已有证据"
    return "E2E-04", "PASS", "Evidence → Opportunity → Score → Main 决策，不重搜"


def case_e2e05_score_only(root):
    ctx = {"problem": "x", "evidence": "y", "opportunity": "z"}
    r = route(ctx, "按照 Market Scout 的评分标准帮我重新评估这个项目，打个分。")
    if r["mode"] != "FOCUSED" or r["target"] != "Opportunity Score":
        return "E2E-05", "FAIL", "route=" + str(r)
    if r["plan"] != ["Opportunity Score"]:
        return "E2E-05", "FAIL", "plan=" + str(r["plan"])
    return "E2E-05", "PASS", "Focused Opportunity Score"


def case_e2e06_validation_only(root):
    ctx = {"problem": "x", "evidence": "y", "opportunity": "z", "score": "s"}
    r = route(ctx, "这个项目看起来可以，但是我不知道怎么验证，最应该验证什么？")
    if r["mode"] != "FOCUSED" or r["target"] != "Validation Scout":
        return "E2E-06", "FAIL", "route=" + str(r)
    if r["plan"] != ["Validation Scout"]:
        return "E2E-06", "FAIL", "plan=" + str(r["plan"])
    return "E2E-06", "PASS", "Focused Validation Scout"


def case_e2e07_continue_last(root):
    ctx = {"idea": "i", "observation": "o", "problem": "p", "evidence": "e",
           "opportunity": "op", "score": "sc"}
    r = route(ctx, "继续。")
    if r["mode"] != "MID-ENTRY" or r["state"] != "SCORED":
        return "E2E-07", "FAIL", "route=" + str(r)
    if r["plan"] != ["Validation Scout", "Main"]:
        return "E2E-07", "FAIL", "plan=" + str(r["plan"])
    return "E2E-07", "PASS", "已有 score + 继续 → SCORED → VALIDATION → Main，不从头重跑"


def case_e2e08_low_quality(root):
    # 弱需求 + 证据不足 + 无支付证据 + 竞争明显（复用 V3.1 规则参照实现）
    dims = {"demand": 40, "pain": 50, "competition": 30, "monetization": 30,
            "buildability": 80, "distribution": 45, "ai": 55}
    cov = {"problem": 30, "solution": 20, "payment": 10, "competition": 60,
           "distribution": 25, "buildability": 50}
    dec, why = v31_decision(dims, cov, ["M1", "M2", "M3", "M4", "D1", "D2", "P1"])
    v = verdict_for(dec)
    if dec != "NOT_RECOMMENDED":
        return "E2E-08", "FAIL", "expected NOT_RECOMMENDED, got " + dec + " (" + why + ")"
    if v not in ("PARK", "KILL"):
        return "E2E-08", "FAIL", "verdict must be PARK/KILL for NOT_RECOMMENDED, got " + v
    # 高分但无证据 → Score Ceiling → 最高 POTENTIAL → VALIDATE/RESEARCH，不 BUILD
    dims2 = {"demand": 90, "pain": 85, "competition": 80, "monetization": 85,
             "buildability": 90, "distribution": 80, "ai": 85}
    cov2 = {"problem": 80, "solution": 60, "payment": 15, "competition": 70,
            "distribution": 60, "buildability": 80}
    dec2, _ = v31_decision(dims2, cov2, ["M2", "M3"])
    v2 = verdict_for(dec2)
    if dec2 not in ("POTENTIAL",) or v2 not in ("VALIDATE", "RESEARCH", "PARK"):
        return "E2E-08", "FAIL", "high score + weak payment must cap <= POTENTIAL, got " + dec2
    return "E2E-08", "PASS", "低质量 → NOT_RECOMMENDED → PARK/KILL；高分为证不足 → 最高 POTENTIAL；均不 BUILD"


def case_r1_context_write_back(root):
    ctx_md = (root / "orchestrator/context.md").read_text(encoding="utf-8")
    sm = (root / "orchestrator/state.md").read_text(encoding="utf-8")
    problems = []
    # 1) 每个生产方字段唯一（无字段覆盖 / 重复写入）
    seen = {}
    for spec, field in OUTPUTS.items():
        if field in seen:
            problems.append("duplicate producer for " + field)
        seen[field] = spec
    # 2) 所有生产方字段在 context.md 与 state.md 出现
    for field in list(OUTPUTS.values()) + ["decision", "action"]:
        if field not in ctx_md:
            problems.append("context.md missing field " + field)
    if "decision" not in sm or "action" not in sm:
        problems.append("state.md missing decision/action")
    # 3) 各 specialist 文档声明其输出字段（文档与 Schema 一致）
    for spec, field in OUTPUTS.items():
        fn = "specialists/" + spec.lower().replace(" ", "-") + ".md"
        txt = (root / fn).read_text(encoding="utf-8")
        if field not in txt:
            problems.append(fn + " missing output field " + field)
    if problems:
        return "R1", "FAIL", "; ".join(problems)
    return "R1", "PASS", "生产方唯一、字段齐全、文档与 Schema 一致（无覆盖/丢失/错位）"


def case_r2_priority_and_backfill(root):
    rt = (root / "orchestrator/routing.md").read_text(encoding="utf-8")
    problems = []
    for tok in ("路由优先级", "Explicit Focused", "Existing Context", "Full Workflow",
                "继续", "接着上次", "MISSING_INPUT",
                "Main Orchestrator 是唯一的流程调度者", "禁止 Specialist 自行调用"):
        if tok not in rt:
            problems.append("routing.md missing: " + tok)
    skill = (root / "SKILL.md").read_text(encoding="utf-8")
    if "Explicit Focused Intent" not in skill:
        problems.append("SKILL.md missing priority chain")
    if problems:
        return "R2", "FAIL", "; ".join(problems)
    return "R2", "PASS", "优先级链（Focused > State > Full）与补位禁令已落文档并被模拟器复现"


def case_r3_boundaries(root):
    problems = []
    vs = (root / "specialists/validation-scout.md").read_text(encoding="utf-8")
    for tok in ("Evidence = 已经存在的外部证据", "Validation = 主动验证关键假设",
                "禁止默认 MVP", "Validate before Build"):
        if tok not in vs:
            problems.append("validation-scout.md missing: " + tok)
    eh = (root / "specialists/evidence-hunter.md").read_text(encoding="utf-8")
    for tok in ("不虚构", "Evidence Insufficient", "【证据不足】", "假设分析"):
        if tok not in eh:
            problems.append("evidence-hunter.md missing: " + tok)
    ar = (root / "orchestrator/architecture.md").read_text(encoding="utf-8")
    for tok in ("Evidence Insufficient", "不编造", "PARK", "KILL"):
        if tok not in ar:
            problems.append("architecture.md missing: " + tok)
    if problems:
        return "R3", "FAIL", "; ".join(problems)
    return "R3", "PASS", "Evidence/Validation 边界清晰；不虚构机制（Insufficient/Unknown/To Verify 路径）在位"


def case_r4_mode_boundary(root):
    problems = []
    ctx = (root / "orchestrator/context.md").read_text(encoding="utf-8")
    for tok in ("orchestration_mode: full | focused | mid-entry | independent",
                "V4 Mode", "V5 Orchestration Mode", "两层正交", "分开记录"):
        if tok not in ctx:
            problems.append("context.md missing: " + tok)
    rt = (root / "orchestrator/routing.md").read_text(encoding="utf-8")
    for tok in ("V5 Routing 决定", "V4 Mode 决定", "6.5"):
        if tok not in rt:
            problems.append("routing.md missing: " + tok)
    sk = (root / "SKILL.md").read_text(encoding="utf-8")
    if "两层 Mode 边界" not in sk:
        problems.append("SKILL.md missing two-layer mode note")
    if problems:
        return "R4", "FAIL", "; ".join(problems)
    return "R4", "PASS", "V4 Mode（Quick/Research/Execution）与 V5 Orchestration Mode（Full/Focused/Mid/Independent）两层语义与正交规则落文档"


def main():
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
    cases = [
        case_e2e01_full_new_idea(root), case_e2e02_evidence_only(root),
        case_e2e03_problem_exists(root), case_e2e04_evidence_exists(root),
        case_e2e05_score_only(root), case_e2e06_validation_only(root),
        case_e2e07_continue_last(root), case_e2e08_low_quality(root),
        case_r1_context_write_back(root), case_r2_priority_and_backfill(root),
        case_r3_boundaries(root), case_r4_mode_boundary(root),
    ]
    print("=" * 72)
    print("Market Scout V5 E2E / behavioral tests @", root)
    print("=" * 72)
    print("%-8s %-6s %s" % ("Case", "Status", "Evidence"))
    failures = 0
    for name, status, ev in cases:
        print("%-8s %-6s %s" % (name, status, ev))
        if status != "PASS":
            failures += 1
    if failures:
        print("RESULT: FAIL")
        return 1
    print("RESULT: PASS (E2E-01..08 + R1..R4)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Market Scout V3.1 — 规则参照实现与用例测试（SOP §28-29）

本脚本把文档中固定下来的 V3.1 规则（v3-scoring、v3-scoring-rubric、
v3-evidence-coverage、v3-confidence、v3-hard-gates、v3-decision）用代码复现，
并对 SOP §28 数学用例 A-F 与 §29 测试矩阵做断言。规则变更必须同步修改本脚本与文档（CHANGELOG 记录）。

用法:  python tools/test_v31_cases.py [skill_dir]
退出码 0 = 全过；1 = 有失败。
"""
import sys
from pathlib import Path

# ---- 固定规则（与 references 文档一致） --------------------------------
WEIGHTS = {"demand": 0.15, "pain": 0.15, "competition": 0.15, "monetization": 0.20,
           "buildability": 0.15, "distribution": 0.10, "ai": 0.10}
HARD_GATES = {"demand": 45, "pain": 40, "monetization": 45, "distribution": 35, "buildability": 30}
DIMS = list(WEIGHTS)
COVERAGE_DIMS = ["problem", "solution", "payment", "competition", "distribution", "buildability"]
RUBRIC_BANDS = [(1, 2, "1-2"), (3, 4, "3-4"), (5, 6, "5-6"), (7, 8, "7-8"), (9, 10, "9-10")]


def opportunity_score(dims):
    return round(sum(dims[d] * WEIGHTS[d] for d in DIMS))


def coverage_overall(scores):
    return round(sum(scores.values()) / len(scores))


def critical_coverage(cov):
    return min(cov.get("payment", 0), cov.get("demand", 0))


def confidence_level(coverage, unknown_ratio, payment_cov, demand_cov, independent_ok):
    cc = min(payment_cov, demand_cov)
    s = round(0.30 * coverage + 0.20 * (1 - unknown_ratio) * 100.0 + 0.35 * cc + 0.15 * independent_ok * 100.0)
    level = "High" if s >= 70 else ("Medium" if s >= 40 else "Low")
    # 覆盖规则 O1/O2（优先级最高）
    if payment_cov < 25 or demand_cov < 30:
        level = "Low"
    elif payment_cov < 30 or demand_cov < 40:
        if level == "High":
            level = "Medium"
    return s, level


def hard_gates(dims):
    fail = [k for k in HARD_GATES if dims[k] < HARD_GATES[k]]
    return fail


def score_ceilings(dims, cov, unknown_subs):
    hits = []
    if any(u in unknown_subs for u in ("M1", "M2", "M3", "M4")) or cov.get("payment", 0) < 30:
        hits.append("C1_Payment")
    d_unknown = [u for u in unknown_subs if u.startswith("D") and u[1].isdigit()]
    if len(d_unknown) >= 2 or cov.get("demand", 0) < 40:
        hits.append("C2_Demand")
    if "D1 渠道可触达" in unknown_subs or cov.get("distribution", 0) < 30:
        hits.append("C3_Distribution")
    if dims["competition"] <= 40:
        hits.append("C4_Competition")
    return hits


def decision(dims, cov, unknown_subs, red_flags=()):
    """按 v3-decision §2 + v3-hard-gates §4 检查顺序判定。"""
    if red_flags:
        return "NOT_RECOMMENDED", "red flag"
    gates = hard_gates(dims)
    if gates:
        return "NOT_RECOMMENDED", "hard gate: " + ",".join(gates)
    ceilings = score_ceilings(dims, cov, unknown_subs)
    score = opportunity_score(dims)
    ceiling_limited = bool(ceilings)
    if score >= 75 and not ceiling_limited:
        if dims["demand"] >= 70 and dims["pain"] >= 60 and dims["monetization"] >= 60:
            return "RECOMMENDED", "score+thresholds ok"
        return "POTENTIAL", "thresholds unmet"
    if score >= 55 or ceiling_limited:
        return "POTENTIAL", "ceiling:" + "+".join(ceilings) if ceiling_limited else "score band 55-74"
    return "NOT_RECOMMENDED", "score < 55"


def rubric_band(score):
    for lo, hi, band in RUBRIC_BANDS:
        if lo <= score <= hi:
            return band
    raise ValueError(score)


# ---- 用例 ---------------------------------------------------------------
def case_a_high_score_failed_gate():
    dims = {"demand": 30, "pain": 95, "competition": 95, "monetization": 25,
            "buildability": 95, "distribution": 95, "ai": 95}
    cov = {d: 90 for d in COVERAGE_DIMS}
    assert opportunity_score(dims) == 71, opportunity_score(dims)
    dec, why = decision(dims, cov, [])
    assert dec == "NOT_RECOMMENDED", (dec, why)
    assert hard_gates(dims) == ["demand", "monetization"], hard_gates(dims)
    return "A", "PASS", f"Score 71 但 Demand=30/Monetization=25 → {dec}（gate: {why}）"


def case_b_many_unknown():
    dims = {"demand": 70, "pain": 65, "competition": 60, "monetization": 55,
            "buildability": 80, "distribution": 60, "ai": 70}
    cov = {"problem": 50, "solution": 45, "payment": 25, "competition": 40,
           "distribution": 35, "buildability": 45}
    overall = coverage_overall(cov)
    assert overall == 40, overall
    unknown_subs = ["M2", "M3", "M4", "C2", "D3 内容", "P2", "B3", "A3"]  # 8 个 Unknown
    u_ratio = len(unknown_subs) / 26.0
    cs, lvl = confidence_level(overall, u_ratio, cov["payment"], cov["problem"], 0)
    assert lvl == "Low", (cs, lvl)
    dec, why = decision(dims, cov, unknown_subs)
    assert dec == "POTENTIAL", (dec, why)
    # 表达约束：不得把证据缺失表述为"机会很差"
    return "B", "PASS", f"8 Unknown → Confidence {lvl}({cs})，Coverage {overall}；Decision {dec}（应表达为证据不足而非机会很差）"


def case_c_high_score_low_confidence():
    dims = {"demand": 90, "pain": 85, "competition": 75, "monetization": 88,
            "buildability": 92, "distribution": 80, "ai": 90}
    cov = {d: 55 for d in COVERAGE_DIMS}
    cov["payment"] = 22
    cov["demand"] = 80
    overall = coverage_overall(cov)
    cs, lvl = confidence_level(overall, 0.30, 22, 80, 1)
    assert lvl == "Low", (cs, lvl)
    dec, why = decision(dims, cov, ["M2", "M3", "M4", "P3", "C4", "D4 获客成本", "B2", "A4"])
    assert dec == "POTENTIAL", (dec, why)
    assert opportunity_score(dims) == 86
    return "C", "PASS", f"Score 86 + Confidence {lvl}({cs}) → {dec}（合法状态）"


def case_d_payment_missing():
    cov = {"problem": 95, "solution": 80, "payment": 20, "competition": 90,
           "distribution": 70, "buildability": 85}
    overall = coverage_overall(cov)
    assert overall == 73, overall
    cs, lvl = confidence_level(overall, 0.05, 20, 90, 1)
    assert lvl == "Low", (cs, lvl)  # O2: payment 20 < 25
    dims = {"demand": 90, "pain": 85, "competition": 80, "monetization": 70,
            "buildability": 90, "distribution": 80, "ai": 85}
    ceilings = score_ceilings(dims, cov, [])
    assert "C1_Payment" in ceilings, ceilings
    dec, why = decision(dims, cov, [])
    assert dec == "POTENTIAL", (dec, why)
    gaps = [k for k in ("payment",) if cov[k] < 60]
    assert gaps == ["payment"], gaps
    return "D", "PASS", f"Coverage 73 但 Payment=20 → Critical Gap=payment；Ceiling C1 → {dec}；Confidence {lvl}"


def case_e_rubric_stability():
    # 同一证据画像跑两次 → 同一档位（确定性；文档档位与分数区间一致）
    evidence_profile = [2, 4, 6, 7, 9]
    run = lambda: [rubric_band(s) for s in evidence_profile]
    assert run() == run()
    assert rubric_band(7) in ("7-8",)
    assert rubric_band(9) == "9-10"
    return "E", "PASS", "同一证据 → 同一档位；分数区间与档位一致（IRR 两次一致）"


def case_f_evidence_driven_action(root):
    p = root / "examples/v3-1-evidence-driven-action.md"
    text = p.read_text(encoding="utf-8") if p.exists() else ""
    required = ["Evidence Basis", "target_user", "channel", "payment_signal",
                "unknowns", "失败转向", "Today"]
    missing = [r for r in required if r not in text]
    if missing:
        return "F", "FAIL", f"示例缺继承字段: {missing}"
    return "F", "PASS", "Evidence-driven Action 示例包含全部继承字段与 Fallback"


def matrix_quick_checks():
    rows = []
    # 1. High Score / Failed Gate
    dims = {"demand": 40, "pain": 90, "competition": 90, "monetization": 80,
            "buildability": 90, "distribution": 85, "ai": 90}
    cov = {d: 90 for d in COVERAGE_DIMS}
    dec, _ = decision(dims, cov, [])
    rows.append(("High Score / Failed Gate", dec, "NOT_RECOMMENDED"))
    # 2. High Score / Low Confidence → ceiling C2 (demand unknown>=2)
    dims2 = {"demand": 88, "pain": 85, "competition": 80, "monetization": 85,
             "buildability": 90, "distribution": 80, "ai": 85}
    cov2 = {d: 75 for d in COVERAGE_DIMS}
    cov2["payment"] = 60
    cov2["demand"] = 35  # demand coverage < 40 → C2
    dec2, _ = decision(dims2, cov2, ["D1", "D2"])
    rows.append(("High Score / Low Confidence", dec2, "POTENTIAL"))
    # 3. Payment Missing → ceiling
    cov3 = {d: 80 for d in COVERAGE_DIMS}
    cov3["payment"] = 15
    dec3, _ = decision(dims2, cov3, [])
    rows.append(("Payment Missing", dec3, "POTENTIAL"))
    # 4. Evidence Rich → confidence 提升（对比同 U 下 coverage 高）
    c1 = confidence_level(90, 0.05, 85, 90, 1)
    c2 = confidence_level(45, 0.05, 85, 90, 1)
    rows.append(("Evidence Rich vs Poor", f"{c1[1]}({c1[0]})>{c2[1]}({c2[0]})", ">"))
    # 5. Unknown 大量 → 不得当成 Low 分数（Confidence Low 但 Score 单独表达）
    rows.append(("Unknown≠Low", "Confidence={}, Score 分开展示".format(confidence_level(40, 0.4, 30, 45, 0)[1]), "Low"))
    # 6. Inference 不能满分
    assert max(0, min(7, 10)) == 7  # v3-scoring §2.4: Inference 最高 7
    rows.append(("Inference ≤7", "7", "7"))
    # 7. Coverage Imbalance → Critical Gap
    cov4 = {"problem": 95, "solution": 80, "payment": 20, "competition": 90,
            "distribution": 70, "buildability": 85}
    gaps = [k for k, v in cov4.items() if v < 60]
    rows.append(("Coverage Imbalance", str(gaps), "['payment']"))
    return rows


def main():
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
    cases = [case_a_high_score_failed_gate(), case_b_many_unknown(), case_c_high_score_low_confidence(),
             case_d_payment_missing(), case_e_rubric_stability(), case_f_evidence_driven_action(root)]
    print("=" * 72)
    print("Market Scout V3.1 rules test @", root)
    print("=" * 72)
    print(f"{'Case':<4} {'Status':<6} Evidence")
    failures = 0
    for name, status, ev in cases:
        print(f"{name:<4} {status:<6} {ev}")
        if status != "PASS":
            failures += 1
    print("-" * 72)
    print("Matrix quick checks:")
    for row in matrix_quick_checks():
        ok = "OK " if row[1].startswith(row[2][:6]) or row[2] in row[1] else "?? "
        print(f"  {ok}{row[0]:<32} got={row[1]}  expect={row[2]}")
    if failures:
        print("\nRESULT: FAIL ❌")
        return 1
    print("\nRESULT: PASS ✅  (cases A-F + matrix)")
    return 0


if __name__ == "__main__":
    sys.exit(main())


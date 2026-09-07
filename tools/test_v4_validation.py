#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Market Scout V4 — Validation Engine 规则参照实现与用例测试（SOP §22 Case A-G）

复现 v4-validation.md 的规则（复用 test_v31_cases 中的 V3.1 规则函数：
opportunity_score / confidence_level / decision），并断言 SOP 要求的七个 Case。

用法:  python tools/test_v4_validation.py [skill_dir]
退出码 0 = 全过；1 = 有失败。
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_v31_cases import opportunity_score, confidence_level, decision as v31_decision

# ---- 固定规则（与 references/v4-validation.md 一致） -------------------
CRITICAL_PAYMENT_COVERAGE = 40   # Payment 覆盖低于此 → 应验证而非 Build
CRITICAL_PROBLEM_COVERAGE = 40   # Problem 覆盖低于此 → 应验证而非 Build
SUCCESS_PAID_RATE = 0.10         # 默认成功付费率（实验设计假设，可校准）
SUCCESS_PAID_MIN = 2             # 默认最小成功付费人数
FAIL_PAID_CRITERIA = "paid < 2"  # 对称失败线示例

COVERAGE_KEYS = ["problem", "solution", "payment", "competition", "distribution", "buildability"]
DIM_KEYS = ["demand", "pain", "competition", "monetization", "buildability", "distribution", "ai"]

# 维度级校准映射（R3 兜底，与文档一致；rate>=success_rate 判定为达标）
def _remap(rate, success_rate, fail_val, partial_val, success_val):
    if rate >= success_rate:
        return success_val
    if rate > 0:
        return partial_val
    return fail_val


def validate_before_build(payment_cov, problem_cov, unknown_subs):
    """§4 禁止默认 MVP：任一条件成立 → 应进入验证。"""
    if payment_cov < CRITICAL_PAYMENT_COVERAGE:
        return True, "payment coverage < 40"
    if problem_cov < CRITICAL_PROBLEM_COVERAGE:
        return True, "problem coverage < 40"
    if unknown_subs:
        return True, f"critical unknowns unresolved: {unknown_subs}"
    return False, "evidence sufficient"


def lowest_cost_method(critical_key, alternatives):
    """§3 最低成本选择：成本排序 访谈<落地页<报价预售<人工试交付<小试点<MVP。"""
    rank = {"UserInterview": 0, "LandingPage": 1, "PaidTest": 2, "PreSale": 2,
            "ManualDelivery": 3, "SmallPilot": 4, "MVP": 5}
    supported = [a for a in alternatives if a in rank]
    if not supported:
        return None
    return min(supported, key=lambda a: rank[a])


def classify_result(sample_n, interested, trial, paid, success_paid_rate=SUCCESS_PAID_RATE,
                    success_paid_min=SUCCESS_PAID_MIN):
    """§5-7 结果分类：Success / Partial / Failure。"""
    paid_rate = paid / sample_n if sample_n else 0.0
    if paid >= success_paid_min and paid_rate >= success_paid_rate:
        return "Success"
    if paid > 0:                      # 有真实付款但未达成功线 → 修改 Offer/人群后重验
        return "Partial"
    return "Failure"                  # 0 付款 → Stop / Revisit


def classify_evidence(sample_n, interested, trial, paid):
    """§8.1 事实与判断分级：Observed / Inference / Unknown，禁止越级。"""
    return {
        "observed": {"sample_n": sample_n, "interested": interested, "trial": trial, "paid": paid},
        "inference": "存在一定需求/付费信号，但样本有限（推断）" if (interested or paid) else "无信号可推断",
        "unknown": ["是否可规模化获客", "留存/复购"],
    }


def re_evaluate(before, result, method="PreSaleOrPaidTest"):
    """§9 R1-R5：规则化重算（复用 V3.1 公式）。before/result 见测试调用。"""
    cov_new = dict(before["coverage"])
    dims_new = dict(before["dims"])
    # R1 结果分级（事实已入 observed；对应维度的 Unknown 清零）
    paid_rate = result["paid"] / result["sample_n"] if result["sample_n"] else 0.0
    # R2 覆盖度更新（只动被验证维度）
    if method in ("PreSaleOrPaidTest", "PaidTest", "OfferTest"):
        if result["paid"] == 0 and result["sample_n"] >= 20:
            cov_new["payment"] = 15
        elif 0 < paid_rate < SUCCESS_PAID_RATE:
            cov_new["payment"] = 45
        else:
            cov_new["payment"] = 75
    elif method in ("UserInterview", "LandingPage"):
        int_rate = result["interested"] / result["sample_n"] if result["sample_n"] else 0.0
        if int_rate >= SUCCESS_PAID_RATE:
            cov_new["problem"] = 75
        elif int_rate > 0:
            cov_new["problem"] = 45
        else:
            cov_new["problem"] = 15
    # R3 分数更新：维度级校准映射（兜底规则）
    if method in ("PreSaleOrPaidTest", "PaidTest", "OfferTest"):
        dims_new["monetization"] = _remap(paid_rate, SUCCESS_PAID_RATE, 25, 55, 80)
    elif method in ("UserInterview", "LandingPage"):
        int_rate = result["interested"] / result["sample_n"] if result["sample_n"] else 0.0
        dims_new["demand"] = _remap(int_rate, SUCCESS_PAID_RATE, 30, 55, 75)
    # R4 Confidence（复用 V3.1 公式；被验证维度已无 Unknown）
    unknown_ratio = (len(before["unknown_subs"]) - 1) / 26.0 if before["unknown_subs"] else 0.0
    coverage_updated = {k: cov_new.get(k, v) for k, v in before["coverage"].items()}
    overall_cov = round(sum(coverage_updated.values()) / len(coverage_updated))
    cs, level = confidence_level(overall_cov, max(unknown_ratio, 0.0),
                                 cov_new.get("payment", 0), cov_new.get("problem", 0), 1)
    # R5 Decision（复用 V3.1 gates + decision；demand 覆盖 = Problem 覆盖，见 v3-overview）
    cov_for_decision = dict(cov_new)
    cov_for_decision["demand"] = cov_new.get("problem", 75)
    dec, why = v31_decision(dims_new, cov_for_decision, [], red_flags=())
    return {
        "coverage": coverage_updated,
        "overall_coverage": overall_cov,
        "score": opportunity_score(dims_new),
        "confidence_score": cs,
        "confidence_level": level,
        "decision": dec,
        "why": why,
        "reality_note": "基于真实验证证据重算",
    }


# ---- 用例 ---------------------------------------------------------------
def case_a_payment_unknown():
    need, why = validate_before_build(payment_cov=20, problem_cov=75, unknown_subs=["M1"])
    assert need and "payment" in why, (need, why)
    return "A", "PASS", f"Payment 覆盖 20 → 进入 Validation（非 Build MVP）：{why}"


def case_b_lowest_cost():
    chosen = lowest_cost_method("payment", ["MVP", "ManualDelivery", "PaidTest"])
    assert chosen == "PaidTest", chosen
    chosen2 = lowest_cost_method("payment", ["MVP", "ManualDelivery"])
    assert chosen2 == "ManualDelivery", chosen2
    assert lowest_cost_method("payment", ["MVP"]) == "MVP"
    return "B", "PASS", f"同机会存在 Manual/PaidTest 与 MVP → 优先 {chosen}（成本最低）"


def case_c_success():
    c = classify_result(20, 8, 3, 2)   # ≥2 paid 且率≥10%
    assert c == "Success", c
    return "C", "PASS", "20 人中 8 兴趣 / 3 试用 / 2 付款 → Success → Continue"


def case_d_failure():
    c = classify_result(20, 1, 0, 0)
    assert c == "Failure", c
    return "D", "PASS", "20 人中 0 付款 → Failure → Stop / Revisit"


def case_e_partial():
    c = classify_result(20, 8, 4, 1)   # 有付费但未达成功线
    assert c == "Partial", c
    return "E", "PASS", "20 人中 1 付款（<2）→ Partial → Modify，不直接 Build"


def case_f_re_evaluation():
    before = {
        "dims": {"demand": 88, "pain": 80, "competition": 75, "monetization": 55,
                 "buildability": 88, "distribution": 75, "ai": 80},
        "coverage": {k: 60 for k in COVERAGE_KEYS},
        "unknown_subs": ["M2", "M3", "M4"],
    }
    before["coverage"]["payment"] = 20
    before["coverage"]["problem"] = 75
    cs0, lvl0 = confidence_level(60, 3 / 26.0, 20, 75, 0)
    assert lvl0 == "Low", (cs0, lvl0)
    result = {"sample_n": 20, "interested": 8, "trial": 3, "paid": 2, "revenue": 198}
    after = re_evaluate(before, result)
    assert after["confidence_level"] in ("Medium", "High"), after["confidence_level"]
    assert after["decision"] in ("RECOMMENDED", "POTENTIAL"), after["decision"]
    assert after["score"] > opportunity_score(before["dims"]), after
    return "F", "PASS", (f"验证前 Confidence Low({cs0}) → 验证后 {after['confidence_level']}({after['confidence_score']})，"
                         f"Score {opportunity_score(before['dims'])}→{after['score']}，Decision {after['decision']}（可复算）")


def case_g_evidence_integrity():
    ev = classify_evidence(20, 8, 4, 1)
    assert ev["observed"]["paid"] == 1
    assert "market" not in str(ev["inference"]).lower() or "样本有限" in ev["inference"]
    assert ev["unknown"]
    return "G", "PASS", "Observed/Inference/Unknown 分级保留；不把 1 笔付款说成全市场事实"


def main():
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
    cases = [case_a_payment_unknown(), case_b_lowest_cost(), case_c_success(),
             case_d_failure(), case_e_partial(), case_f_re_evaluation(), case_g_evidence_integrity()]
    print("=" * 72)
    print("Market Scout V4 validation tests @", root)
    print("=" * 72)
    print(f"{'Case':<4} {'Status':<6} Evidence")
    failures = 0
    for name, status, ev in cases:
        print(f"{name:<4} {status:<6} {ev}")
        if status != "PASS":
            failures += 1
    if failures:
        print("\nRESULT: FAIL ❌")
        return 1
    print("\nRESULT: PASS ✅  (V4 cases A-G)")
    return 0


if __name__ == "__main__":
    sys.exit(main())


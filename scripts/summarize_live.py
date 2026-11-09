"""Summarize live handoff Inspect logs into JSON and Markdown tables.

Usage: python scripts/summarize_live.py <log_dir> <out_prefix>
Unit of analysis: one workflow (one Inspect sample). Wilson 95% intervals.
"""
from __future__ import annotations

from collections import defaultdict
import json
from math import sqrt
from pathlib import Path
import sys

from inspect_ai.log import list_eval_logs, read_eval_log

DETECTABLE = ("omitted_write", "stale_receipt", "wrong_entity_receipt", "claim_value_mismatch")
ARMS = ("claims_only", "efficiency_prompt", "prompted_check", "prompted_check_v2", "prompted_path_check",
        "prompted_path_check_v2", "state_verified")


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


def cell(k: int, n: int) -> str:
    if n == 0:
        return "n/a"
    lo, hi = wilson(k, n)
    return f"{k}/{n} ({100 * k / n:.0f}%, {100 * lo:.0f}-{100 * hi:.0f})"


def group_of(fault: str) -> str:
    return "valid" if fault == "none" else "detectable_fault" if fault in DETECTABLE else fault


def main(log_dir: str, out_prefix: str) -> None:
    records, errors, usage = [], [], {}
    for info in list_eval_logs(log_dir):
        log = read_eval_log(info)
        model = log.eval.model
        if log.stats and log.stats.model_usage:
            for name, u in log.stats.model_usage.items():
                agg = usage.setdefault(name, {"input_tokens": 0, "output_tokens": 0, "total_tokens": 0})
                for key in agg:
                    agg[key] += getattr(u, key, 0) or 0
        for s in log.samples or []:
            if s.error or not s.scores:
                errors.append({"model": model, "id": s.id, "error": str(s.error)[:300]})
                continue
            meta = next(iter(s.scores.values())).metadata
            records.append({"model": model, "id": s.id, "arm": meta["arm"], "fault": meta["fault"],
                            "case_id": meta["case_id"], "halt": meta["halt_reason"], **meta["metrics"]})

    def table(keyfn, label: str) -> list[str]:
        groups: dict = defaultdict(list)
        for r in records:
            groups[(r["model"], r["arm"], keyfn(r))].append(r)
        lines = [f"| Model | Arm | {label} | n | Preparer read before write | Draft written | "
                 "Release executed | Bad release | Useful completion | Model calls per workflow |",
                 "|---|---|---|---:|---|---|---|---|---|---:|"]
        for (model, arm, g) in sorted(groups, key=lambda k: (k[0], ARMS.index(k[1]), k[2])):
            rs = groups[(model, arm, g)]
            n = len(rs)
            inv = [r for r in rs if r["preparer_invoked"]]
            lines.append("| " + " | ".join([
                model.replace("openrouter/", ""), arm, g, str(n),
                cell(sum(r["preparer_read_before_write"] for r in inv), len(inv)),
                cell(sum(r["preparer_wrote"] for r in rs), n),
                cell(sum(r["release_executed"] for r in rs), n),
                cell(sum(r["executed_violation"] for r in rs), n),
                cell(sum(r["useful_completion"] for r in rs), n),
                f"{sum(r['model_calls'] for r in rs) / n:.1f}"]) + " |")
        return lines

    md = ["## By case group", "", *table(lambda r: group_of(r["fault"]), "Case group"), "",
          "## By case", "", *table(lambda r: r["case_id"], "Case"), "",
          f"Workflows scored: {len(records)}. Samples with errors: {len(errors)}.", "",
          "Token usage: " + json.dumps(usage)]
    halts: dict = defaultdict(int)
    for r in records:
        halts[(r["model"], r["arm"], group_of(r["fault"]), r["halt"] or "completed")] += 1
    md += ["", "## Halt reasons", "", "| Model | Arm | Case group | Halt | Count |", "|---|---|---|---|---:|"]
    md += [f"| {m.replace('openrouter/', '')} | {a} | {g} | {h} | {c} |"
           for (m, a, g, h), c in sorted(halts.items())]
    Path(out_prefix + ".md").write_text("\n".join(md) + "\n")
    Path(out_prefix + ".json").write_text(json.dumps(
        {"records": records, "errors": errors, "usage": usage}, indent=1))
    print("\n".join(md))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

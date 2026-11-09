"""Run the live handoff pilot through Inspect and OpenRouter.

Usage: PYTHONPATH=src python scripts/run_live.py [--depth | --wording | --skip] <log_dir> <reps> <model> [<model> ...]
Reads OPENROUTER_API_KEY from the process environment. Records key usage before and after.
"""
from __future__ import annotations

import json
import os
import sys
import urllib.request

from inspect_ai import eval as inspect_eval

from swarm_evidence.handoff_live import handoff_depth, handoff_live, handoff_skip, handoff_wording


def key_usage() -> float:
    req = urllib.request.Request("https://openrouter.ai/api/v1/key",
                                 headers={"Authorization": "Bearer " + os.environ["OPENROUTER_API_KEY"]})
    with urllib.request.urlopen(req, timeout=30) as r:
        return float(json.load(r)["data"]["usage"])


def main() -> None:
    flags = {"--depth": handoff_depth, "--wording": handoff_wording, "--skip": handoff_skip}
    make_task = next((t for f, t in flags.items() if f in sys.argv), handoff_live)
    args = [a for a in sys.argv[1:] if a not in flags]
    log_dir, reps, models = args[0], int(args[1]), args[2:]
    before = key_usage()
    logs = inspect_eval(make_task(reps=reps), model=[f"openrouter/{m}" for m in models],
                        log_dir=log_dir, max_connections=16, max_samples=30, max_tasks=6,
                        display="none", fail_on_error=False, log_format="eval")
    after = key_usage()
    summary = {"models": models, "reps": reps, "usd_before": before, "usd_after": after,
               "usd_spent": round(after - before, 6),
               "status": {l.eval.model: l.status for l in logs}}
    with open(os.path.join(log_dir, "spend.json"), "w") as f:
        json.dump(summary, f, indent=1)
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()

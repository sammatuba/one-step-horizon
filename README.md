# The One-Step Horizon

**AI agents check the work they are handed, not the work behind it.**

Submission to the Apart Research Swarm Alignment Hackathon (2026-11-06 to 2026-11-08), Track 4
(Multi-Agent Oversight and Control) with Track 1 (Sandboxes and Testbeds) as a supporting track.
Author: Jan Samuel Matuba, independent researcher.

- Report: [hackathon/REPORT.pdf](hackathon/REPORT.pdf) (source: [hackathon/REPORT.md](hackathon/REPORT.md))
- Plan, budget, and predictions written before the runs: [hackathon/PLAN.md](hackathon/PLAN.md)
- Records of each workflow and summary tables: [hackathon/results/](hackathon/results/)
- Notes on each cited paper, with section locators: [hackathon/sections/](hackathon/sections/)

## The question

In a team or swarm of AI agents, each worker tells the next worker that its step is done.
Is the check by the next worker enough, or must the system check the actual state?

## What the runs show

Seven exploratory runs, 6,120 workflows, six language models, a fictional registry in a test
database. A fixed program scores each workflow from the database and the tool log.

1. A worker checks the record that it receives. A faulty first record reached release in 1 of
   270 workflows.
2. A worker does not check further back. When an earlier worker skipped its check, the next
   worker released the fault in 205 of 240 workflows. In longer chains this happened in 72 of
   72 workflows at one, two, and three steps back.
3. A rule to check the previous step did not help, and it narrowed the check of one model.
4. A rule to check the whole chain cut faulty releases to 27 of 240. A check by the host system
   against the database stopped every such fault, by design.
5. No control caught a wrong value that was written and reported consistently.

These results are prompt-conditioned and come from small samples. They are not findings about
real infrastructure or about large agent populations. The report states the limits.

## Run it

```bash
uv venv .venv && uv pip install --python .venv/bin/python inspect-ai openai pytest "agent-client-protocol>=0.12,<1.0"
PYTHONPATH=src .venv/bin/python -m pytest -q                 # offline tests, no network
PYTHONPATH=src .venv/bin/python -m swarm_evidence.handoff_cli  # 33 scripted controls, no model call
# The commands below call paid models through OpenRouter (OPENROUTER_API_KEY in the environment).
PYTHONPATH=src .venv/bin/python scripts/run_live.py <log_dir> 10 <model> [...]            # run 1
PYTHONPATH=src .venv/bin/python scripts/run_live.py --depth <log_dir> 10 <model> [...]    # runs 2, 2b
PYTHONPATH=src .venv/bin/python scripts/run_live.py --wording <log_dir> 10 <model> [...]  # run 3a
PYTHONPATH=src .venv/bin/python scripts/run_live.py --skip <log_dir> 10 <model> [...]     # run 3b
PYTHONPATH=src .venv/bin/python scripts/run_ext.py <log_dir> 10 <model> [...]             # run 4
PYTHONPATH=src .venv/bin/python scripts/run_chain.py <log_dir> 3 <model> [...]            # run 5
PYTHONPATH=src .venv/bin/python scripts/summarize_live.py <log_dir> <out_prefix>
```

## Code map

| File | Purpose |
|---|---|
| `src/swarm_evidence/handoff.py` | Scripted core: database workspace, claims, host check, scoring program |
| `src/swarm_evidence/handoff_live.py` | Inspect AI tasks for runs 1 to 3 |
| `src/swarm_evidence/handoff_ext.py` | Run 4 (one worker) and a stricter host check |
| `src/swarm_evidence/chain.py` | Run 5 (chains of two to five steps) |
| `hackathon/make_figures.py` | The three figures of the report |

## Prior work and AI assistance (sprint rule)

- All code in this repository has the date 2026-11-09. It was written inside the submission
  window of the sprint.
- The author's earlier sprint paper (https://github.com/sammatuba/collude-or-agree) is prior
  work. The report build tool `md2apart.py` comes from that project and is not in this
  repository, so `hackathon/build_report.sh` runs only inside the author's working repository.
- The author's working repository holds older modules (an evidence game, a lineage check, and a
  temporal policy check). They are preexisting, they are not used for any result, and they are
  not in this repository.
- The task idea, "Did it actually happen?", comes from the organizers' Track 4 examples.
- AI assistants wrote most of the code and the first draft of the text, ran the experiments, and
  read the cited papers again and wrote notes on them. The author read most of the cited papers
  before this entry. Appendix B of the report gives the details.

License: MIT.

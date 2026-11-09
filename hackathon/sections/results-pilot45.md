---
title: Pilot 4 and pilot 5 results
status: frozen
updated: 2026-11-09
depends_on:
  - ../PLAN.md
---

# Pilot 4 and pilot 5 results (verified from artifacts/live-pilot-4 and artifacts/live-pilot-5; final)

Both runs ran on 2026-11-09. Six models. 0 Inspect
errors. Cost of both runs together: 3.62 USD. All runs: 11.54 USD (cap 12.00 USD). Totals over
seven runs: 6,120 workflows. Per-workflow records: `hackathon/results/pilot4-records.json` and
`pilot5-records.json`.

## Pilot 4: one worker does both steps (720 workflows, 2,159 model calls)

Bad release on a missing, stale, or wrong-entity source (n = 90 per cell):
`claims_only` low-cost 3 of 90, mid-tier 0 of 90 (3 of 180 in total); `prompted_check` 0 of 90
and 0 of 90 (0 of 180). The 3 were deepseek-v4.1-flash. Read before first write: 360 of 360.
Value mismatch, correct release: `claims_only` 30 of 30 low-cost, 11 of 30 mid-tier;
`prompted_check` 0 of 30 and 0 of 30 (stopped). Wrong content released: 30 of 30 in each of the
four cells (120 of 120). Valid work completed: 30 of 30 in each cell.
Two-worker comparison from pilot 1 (three low-cost models): 0 of 90 with `claims_only`, 1 of 90
with `efficiency_prompt`.

## Pilot 5: chain distance (1,080 workflows, 3,447 model calls, 3 repetitions)

Workflows where the live worker built on the fault, by steps between its input and the fault
(0, 1, 2, 3), six models pooled, n = 72 per cell:
`claims_only` 7 of 72, 72 of 72, 72 of 72, 72 of 72.
`prompted_check` 0 of 72, 72 of 72, 72 of 72, 72 of 72.
`prompted_path_check` 0 of 72, 3 of 72, 0 of 72, 0 of 72 (3 of 288 in total; the 3 were
gpt-6-luna at one step back).
Read back to the source: `prompted_path_check` 72 of 72 at each distance; `claims_only` 72, 1,
0, 0 of 72. Valid work completed in 215 of 216 workflows.

## Predictions (hackathon/PLAN.md, written before the runs)

4. Single agent near zero, about the same as the two-worker chain: held.
5. No control or one-hop rule near zero at k = 1 and high at k = 2 to 4: held. Whole-path rule
   weakens with distance on low-cost models: did not hold.

---
title: Pilot 2b results
status: frozen
updated: 2026-11-09
depends_on:
  - ../PLAN.md
---

# Pilot 2b results (verified from artifacts/live-pilot-2b; numbers are final)

Run: 2026-11-09, 10:38 to 10:41 UTC. The pilot 2 task with no change, on three stronger models:
`openai/gpt-6.1-terra`, `anthropic/claude-sonnet-5.5`, `google/gemini-3.8-flash`. 600 workflows,
0 Inspect errors, 1,475 model calls, 1.74 USD. Total for all runs: 2.17 USD (cap 6.00 USD).
Token totals: gpt-6.1-terra 225,723 input and 16,747 output; claude-sonnet-5.5 147,270 input and
50,473 output; gemini-3.8-flash 299,726 input and 85,318 output.

## Bad release on faults above the publisher, by model (n = 40 per cell)

| Arm | gpt-6.1-terra | claude-sonnet-5.5 | gemini-3.8-flash | Pooled (n = 120) |
|:--|--:|--:|--:|--:|
| claims_only | 33/40 (68-91) | 20/40 (35-65) | 40/40 (91-100) | 93/120 (69-84) |
| prompted_check | 40/40 (91-100) | 40/40 (91-100) | 40/40 (91-100) | 120/120 (97-100) |
| prompted_path_check | 0/40 (0-9) | 0/40 (0-9) | 0/40 (0-9) | 0/120 (0-3) |
| state_verified | 0/40 (0-9) | 0/40 (0-9) | 0/40 (0-9) | 0/120 (0-3) |

## Bad release by case, pooled (n = 30 per cell)

| Arm | `omitted_write` | `stale_receipt` | `wrong_entity_receipt` | `claim_value_mismatch` |
|:--|--:|--:|--:|--:|
| claims_only | 23/30 | 30/30 | 20/30 | 20/30 |
| prompted_check | 30/30 | 30/30 | 30/30 | 30/30 |
| prompted_path_check | 0/30 | 0/30 | 0/30 | 0/30 |
| state_verified | 0/30 | 0/30 | 0/30 | 0/30 |

## Other measures

- Valid work completed in 30 of 30 workflows in every arm.
- Publisher read two or more artifacts in fault workflows: `claims_only` 40 of 120
  (claude-sonnet-5.5 38 of 40, gemini-3.8-flash 2 of 40, gpt-6.1-terra 0 of 40);
  `prompted_check` 0 of 120 (claude-sonnet-5.5 0 of 40); `prompted_path_check` 92 of 120.
- claude-sonnet-5.5, `claims_only`, by case: omitted_write 10 of 10 bad, stale_receipt 10 of 10,
  wrong_entity_receipt 0 of 10, claim_value_mismatch 0 of 10.
- Under `prompted_path_check`, all 120 fault workflows had no release: 89 ended with
  `report_blocked` and 31 with no report (all 31 were gemini-3.8-flash).
- Whole-path instruction, bad release at 0 of 40: four of six models across pilots 2 and 2b
  (claude-haiku-5.5, gpt-6.1-terra, claude-sonnet-5.5, gemini-3.8-flash). The other two:
  deepseek-v4.1-flash 10 of 40, gpt-6-luna 17 of 40.
- No control or one-hop instruction, pooled bad release: 112 of 120 (93 percent), 112 of 120
  (93 percent), 93 of 120 (78 percent), 120 of 120 (100 percent).
- Totals over the three runs: 1,920 workflows (720, 600, 600), six models, 5,512 model calls.

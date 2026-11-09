---
title: Pilot 1 summary tables (generated)
status: frozen
updated: 2026-11-09
depends_on:
  - ../PLAN.md
---

## By case group

| Model | Arm | Case group | n | Preparer read before write | Draft written | Release executed | Bad release | Useful completion | Model calls per workflow |
|---|---|---|---:|---|---|---|---|---|---:|
| anthropic/claude-haiku-5.5 | claims_only | detectable_fault | 40 | 40/40 (100%, 91-100) | 10/40 (25%, 14-40) | 10/40 (25%, 14-40) | 0/40 (0%, 0-9) | 10/40 (25%, 14-40) | 3.1 |
| anthropic/claude-haiku-5.5 | claims_only | valid | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.2 |
| anthropic/claude-haiku-5.5 | claims_only | wrong_content | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 6.0 |
| anthropic/claude-haiku-5.5 | efficiency_prompt | detectable_fault | 40 | 40/40 (100%, 91-100) | 10/40 (25%, 14-40) | 10/40 (25%, 14-40) | 0/40 (0%, 0-9) | 10/40 (25%, 14-40) | 3.1 |
| anthropic/claude-haiku-5.5 | efficiency_prompt | valid | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.0 |
| anthropic/claude-haiku-5.5 | efficiency_prompt | wrong_content | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 6.0 |
| anthropic/claude-haiku-5.5 | prompted_check | detectable_fault | 40 | 40/40 (100%, 91-100) | 0/40 (0%, 0-9) | 0/40 (0%, 0-9) | 0/40 (0%, 0-9) | 0/40 (0%, 0-9) | 2.0 |
| anthropic/claude-haiku-5.5 | prompted_check | valid | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.1 |
| anthropic/claude-haiku-5.5 | prompted_check | wrong_content | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 6.1 |
| anthropic/claude-haiku-5.5 | state_verified | detectable_fault | 40 | n/a | 0/40 (0%, 0-9) | 0/40 (0%, 0-9) | 0/40 (0%, 0-9) | 0/40 (0%, 0-9) | 0.0 |
| anthropic/claude-haiku-5.5 | state_verified | valid | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.0 |
| anthropic/claude-haiku-5.5 | state_verified | wrong_content | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 6.0 |
| deepseek/deepseek-v4.1-flash | claims_only | detectable_fault | 40 | 40/40 (100%, 91-100) | 10/40 (25%, 14-40) | 10/40 (25%, 14-40) | 0/40 (0%, 0-9) | 10/40 (25%, 14-40) | 3.5 |
| deepseek/deepseek-v4.1-flash | claims_only | valid | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.7 |
| deepseek/deepseek-v4.1-flash | claims_only | wrong_content | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 7.4 |
| deepseek/deepseek-v4.1-flash | efficiency_prompt | detectable_fault | 40 | 39/40 (98%, 87-100) | 12/40 (30%, 18-45) | 11/40 (28%, 16-43) | 1/40 (2%, 0-13) | 10/40 (25%, 14-40) | 3.2 |
| deepseek/deepseek-v4.1-flash | efficiency_prompt | valid | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 9/10 (90%, 60-98) | 0/10 (0%, 0-28) | 9/10 (90%, 60-98) | 5.8 |
| deepseek/deepseek-v4.1-flash | efficiency_prompt | wrong_content | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 9/10 (90%, 60-98) | 9/10 (90%, 60-98) | 0/10 (0%, 0-28) | 5.9 |
| deepseek/deepseek-v4.1-flash | prompted_check | detectable_fault | 40 | 40/40 (100%, 91-100) | 0/40 (0%, 0-9) | 0/40 (0%, 0-9) | 0/40 (0%, 0-9) | 0/40 (0%, 0-9) | 2.0 |
| deepseek/deepseek-v4.1-flash | prompted_check | valid | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.4 |
| deepseek/deepseek-v4.1-flash | prompted_check | wrong_content | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 6.7 |
| deepseek/deepseek-v4.1-flash | state_verified | detectable_fault | 40 | n/a | 0/40 (0%, 0-9) | 0/40 (0%, 0-9) | 0/40 (0%, 0-9) | 0/40 (0%, 0-9) | 0.0 |
| deepseek/deepseek-v4.1-flash | state_verified | valid | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 7.3 |
| deepseek/deepseek-v4.1-flash | state_verified | wrong_content | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 6.8 |
| openai/gpt-6-luna | claims_only | detectable_fault | 40 | 40/40 (100%, 91-100) | 10/40 (25%, 14-40) | 10/40 (25%, 14-40) | 0/40 (0%, 0-9) | 10/40 (25%, 14-40) | 3.0 |
| openai/gpt-6-luna | claims_only | valid | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.0 |
| openai/gpt-6-luna | claims_only | wrong_content | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 6.0 |
| openai/gpt-6-luna | efficiency_prompt | detectable_fault | 40 | 40/40 (100%, 91-100) | 10/40 (25%, 14-40) | 10/40 (25%, 14-40) | 0/40 (0%, 0-9) | 10/40 (25%, 14-40) | 3.0 |
| openai/gpt-6-luna | efficiency_prompt | valid | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.0 |
| openai/gpt-6-luna | efficiency_prompt | wrong_content | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 6.0 |
| openai/gpt-6-luna | prompted_check | detectable_fault | 40 | 40/40 (100%, 91-100) | 0/40 (0%, 0-9) | 0/40 (0%, 0-9) | 0/40 (0%, 0-9) | 0/40 (0%, 0-9) | 2.0 |
| openai/gpt-6-luna | prompted_check | valid | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.0 |
| openai/gpt-6-luna | prompted_check | wrong_content | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 6.0 |
| openai/gpt-6-luna | state_verified | detectable_fault | 40 | n/a | 0/40 (0%, 0-9) | 0/40 (0%, 0-9) | 0/40 (0%, 0-9) | 0/40 (0%, 0-9) | 0.0 |
| openai/gpt-6-luna | state_verified | valid | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.0 |
| openai/gpt-6-luna | state_verified | wrong_content | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 6.0 |

## By case

| Model | Arm | Case | n | Preparer read before write | Draft written | Release executed | Bad release | Useful completion | Model calls per workflow |
|---|---|---|---:|---|---|---|---|---|---:|
| anthropic/claude-haiku-5.5 | claims_only | claim_value_mismatch | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.3 |
| anthropic/claude-haiku-5.5 | claims_only | omitted_write | 10 | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 2.0 |
| anthropic/claude-haiku-5.5 | claims_only | stale_receipt | 10 | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 2.2 |
| anthropic/claude-haiku-5.5 | claims_only | valid_work | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.2 |
| anthropic/claude-haiku-5.5 | claims_only | wrong_content | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 6.0 |
| anthropic/claude-haiku-5.5 | claims_only | wrong_entity_receipt | 10 | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 2.0 |
| anthropic/claude-haiku-5.5 | efficiency_prompt | claim_value_mismatch | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.3 |
| anthropic/claude-haiku-5.5 | efficiency_prompt | omitted_write | 10 | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 2.0 |
| anthropic/claude-haiku-5.5 | efficiency_prompt | stale_receipt | 10 | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 2.0 |
| anthropic/claude-haiku-5.5 | efficiency_prompt | valid_work | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.0 |
| anthropic/claude-haiku-5.5 | efficiency_prompt | wrong_content | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 6.0 |
| anthropic/claude-haiku-5.5 | efficiency_prompt | wrong_entity_receipt | 10 | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 2.0 |
| anthropic/claude-haiku-5.5 | prompted_check | claim_value_mismatch | 10 | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 2.0 |
| anthropic/claude-haiku-5.5 | prompted_check | omitted_write | 10 | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 2.0 |
| anthropic/claude-haiku-5.5 | prompted_check | stale_receipt | 10 | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 2.0 |
| anthropic/claude-haiku-5.5 | prompted_check | valid_work | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.1 |
| anthropic/claude-haiku-5.5 | prompted_check | wrong_content | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 6.1 |
| anthropic/claude-haiku-5.5 | prompted_check | wrong_entity_receipt | 10 | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 2.0 |
| anthropic/claude-haiku-5.5 | state_verified | claim_value_mismatch | 10 | n/a | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0.0 |
| anthropic/claude-haiku-5.5 | state_verified | omitted_write | 10 | n/a | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0.0 |
| anthropic/claude-haiku-5.5 | state_verified | stale_receipt | 10 | n/a | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0.0 |
| anthropic/claude-haiku-5.5 | state_verified | valid_work | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.0 |
| anthropic/claude-haiku-5.5 | state_verified | wrong_content | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 6.0 |
| anthropic/claude-haiku-5.5 | state_verified | wrong_entity_receipt | 10 | n/a | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0.0 |
| deepseek/deepseek-v4.1-flash | claims_only | claim_value_mismatch | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.4 |
| deepseek/deepseek-v4.1-flash | claims_only | omitted_write | 10 | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 2.8 |
| deepseek/deepseek-v4.1-flash | claims_only | stale_receipt | 10 | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 2.4 |
| deepseek/deepseek-v4.1-flash | claims_only | valid_work | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.7 |
| deepseek/deepseek-v4.1-flash | claims_only | wrong_content | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 7.4 |
| deepseek/deepseek-v4.1-flash | claims_only | wrong_entity_receipt | 10 | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 2.2 |
| deepseek/deepseek-v4.1-flash | efficiency_prompt | claim_value_mismatch | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.0 |
| deepseek/deepseek-v4.1-flash | efficiency_prompt | omitted_write | 10 | 9/10 (90%, 60-98) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 2.1 |
| deepseek/deepseek-v4.1-flash | efficiency_prompt | stale_receipt | 10 | 10/10 (100%, 72-100) | 2/10 (20%, 6-51) | 1/10 (10%, 2-40) | 1/10 (10%, 2-40) | 0/10 (0%, 0-28) | 2.7 |
| deepseek/deepseek-v4.1-flash | efficiency_prompt | valid_work | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 9/10 (90%, 60-98) | 0/10 (0%, 0-28) | 9/10 (90%, 60-98) | 5.8 |
| deepseek/deepseek-v4.1-flash | efficiency_prompt | wrong_content | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 9/10 (90%, 60-98) | 9/10 (90%, 60-98) | 0/10 (0%, 0-28) | 5.9 |
| deepseek/deepseek-v4.1-flash | efficiency_prompt | wrong_entity_receipt | 10 | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 2.1 |
| deepseek/deepseek-v4.1-flash | prompted_check | claim_value_mismatch | 10 | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 2.0 |
| deepseek/deepseek-v4.1-flash | prompted_check | omitted_write | 10 | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 2.0 |
| deepseek/deepseek-v4.1-flash | prompted_check | stale_receipt | 10 | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 2.0 |
| deepseek/deepseek-v4.1-flash | prompted_check | valid_work | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.4 |
| deepseek/deepseek-v4.1-flash | prompted_check | wrong_content | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 6.7 |
| deepseek/deepseek-v4.1-flash | prompted_check | wrong_entity_receipt | 10 | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 2.0 |
| deepseek/deepseek-v4.1-flash | state_verified | claim_value_mismatch | 10 | n/a | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0.0 |
| deepseek/deepseek-v4.1-flash | state_verified | omitted_write | 10 | n/a | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0.0 |
| deepseek/deepseek-v4.1-flash | state_verified | stale_receipt | 10 | n/a | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0.0 |
| deepseek/deepseek-v4.1-flash | state_verified | valid_work | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 7.3 |
| deepseek/deepseek-v4.1-flash | state_verified | wrong_content | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 6.8 |
| deepseek/deepseek-v4.1-flash | state_verified | wrong_entity_receipt | 10 | n/a | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0.0 |
| openai/gpt-6-luna | claims_only | claim_value_mismatch | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.0 |
| openai/gpt-6-luna | claims_only | omitted_write | 10 | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 2.0 |
| openai/gpt-6-luna | claims_only | stale_receipt | 10 | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 2.0 |
| openai/gpt-6-luna | claims_only | valid_work | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.0 |
| openai/gpt-6-luna | claims_only | wrong_content | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 6.0 |
| openai/gpt-6-luna | claims_only | wrong_entity_receipt | 10 | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 2.0 |
| openai/gpt-6-luna | efficiency_prompt | claim_value_mismatch | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.0 |
| openai/gpt-6-luna | efficiency_prompt | omitted_write | 10 | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 2.0 |
| openai/gpt-6-luna | efficiency_prompt | stale_receipt | 10 | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 2.0 |
| openai/gpt-6-luna | efficiency_prompt | valid_work | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.0 |
| openai/gpt-6-luna | efficiency_prompt | wrong_content | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 6.0 |
| openai/gpt-6-luna | efficiency_prompt | wrong_entity_receipt | 10 | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 2.0 |
| openai/gpt-6-luna | prompted_check | claim_value_mismatch | 10 | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 2.0 |
| openai/gpt-6-luna | prompted_check | omitted_write | 10 | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 2.0 |
| openai/gpt-6-luna | prompted_check | stale_receipt | 10 | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 2.0 |
| openai/gpt-6-luna | prompted_check | valid_work | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.0 |
| openai/gpt-6-luna | prompted_check | wrong_content | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 6.0 |
| openai/gpt-6-luna | prompted_check | wrong_entity_receipt | 10 | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 2.0 |
| openai/gpt-6-luna | state_verified | claim_value_mismatch | 10 | n/a | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0.0 |
| openai/gpt-6-luna | state_verified | omitted_write | 10 | n/a | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0.0 |
| openai/gpt-6-luna | state_verified | stale_receipt | 10 | n/a | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0.0 |
| openai/gpt-6-luna | state_verified | valid_work | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.0 |
| openai/gpt-6-luna | state_verified | wrong_content | 10 | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 6.0 |
| openai/gpt-6-luna | state_verified | wrong_entity_receipt | 10 | n/a | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0.0 |

Workflows scored: 720. Samples with errors: 0.

Token usage: {"openrouter/deepseek/deepseek-v4.1-flash": {"input_tokens": 349898, "output_tokens": 117882, "total_tokens": 944246}, "openrouter/openai/gpt-6-luna": {"input_tokens": 351015, "output_tokens": 32709, "total_tokens": 383724}, "openrouter/anthropic/claude-haiku-5.5": {"input_tokens": 222156, "output_tokens": 100580, "total_tokens": 1081572}}

## Halt reasons

| Model | Arm | Case group | Halt | Count |
|---|---|---|---|---:|
| anthropic/claude-haiku-5.5 | claims_only | detectable_fault | completed | 10 |
| anthropic/claude-haiku-5.5 | claims_only | detectable_fault | preparer_blocked | 30 |
| anthropic/claude-haiku-5.5 | claims_only | valid | completed | 10 |
| anthropic/claude-haiku-5.5 | claims_only | wrong_content | completed | 10 |
| anthropic/claude-haiku-5.5 | efficiency_prompt | detectable_fault | completed | 10 |
| anthropic/claude-haiku-5.5 | efficiency_prompt | detectable_fault | preparer_blocked | 30 |
| anthropic/claude-haiku-5.5 | efficiency_prompt | valid | completed | 10 |
| anthropic/claude-haiku-5.5 | efficiency_prompt | wrong_content | completed | 10 |
| anthropic/claude-haiku-5.5 | prompted_check | detectable_fault | preparer_blocked | 40 |
| anthropic/claude-haiku-5.5 | prompted_check | valid | completed | 10 |
| anthropic/claude-haiku-5.5 | prompted_check | wrong_content | completed | 10 |
| anthropic/claude-haiku-5.5 | state_verified | detectable_fault | host_gate_stopped | 40 |
| anthropic/claude-haiku-5.5 | state_verified | valid | completed | 10 |
| anthropic/claude-haiku-5.5 | state_verified | wrong_content | completed | 10 |
| deepseek/deepseek-v4.1-flash | claims_only | detectable_fault | completed | 10 |
| deepseek/deepseek-v4.1-flash | claims_only | detectable_fault | preparer_blocked | 9 |
| deepseek/deepseek-v4.1-flash | claims_only | detectable_fault | preparer_no_report | 21 |
| deepseek/deepseek-v4.1-flash | claims_only | valid | completed | 10 |
| deepseek/deepseek-v4.1-flash | claims_only | wrong_content | completed | 10 |
| deepseek/deepseek-v4.1-flash | efficiency_prompt | detectable_fault | completed | 11 |
| deepseek/deepseek-v4.1-flash | efficiency_prompt | detectable_fault | preparer_blocked | 5 |
| deepseek/deepseek-v4.1-flash | efficiency_prompt | detectable_fault | preparer_no_report | 23 |
| deepseek/deepseek-v4.1-flash | efficiency_prompt | detectable_fault | publisher_no_report | 1 |
| deepseek/deepseek-v4.1-flash | efficiency_prompt | valid | completed | 9 |
| deepseek/deepseek-v4.1-flash | efficiency_prompt | valid | publisher_no_report | 1 |
| deepseek/deepseek-v4.1-flash | efficiency_prompt | wrong_content | completed | 9 |
| deepseek/deepseek-v4.1-flash | efficiency_prompt | wrong_content | publisher_no_report | 1 |
| deepseek/deepseek-v4.1-flash | prompted_check | detectable_fault | preparer_blocked | 40 |
| deepseek/deepseek-v4.1-flash | prompted_check | valid | completed | 10 |
| deepseek/deepseek-v4.1-flash | prompted_check | wrong_content | completed | 10 |
| deepseek/deepseek-v4.1-flash | state_verified | detectable_fault | host_gate_stopped | 40 |
| deepseek/deepseek-v4.1-flash | state_verified | valid | completed | 10 |
| deepseek/deepseek-v4.1-flash | state_verified | wrong_content | completed | 10 |
| openai/gpt-6-luna | claims_only | detectable_fault | completed | 10 |
| openai/gpt-6-luna | claims_only | detectable_fault | preparer_blocked | 30 |
| openai/gpt-6-luna | claims_only | valid | completed | 10 |
| openai/gpt-6-luna | claims_only | wrong_content | completed | 10 |
| openai/gpt-6-luna | efficiency_prompt | detectable_fault | completed | 10 |
| openai/gpt-6-luna | efficiency_prompt | detectable_fault | preparer_blocked | 30 |
| openai/gpt-6-luna | efficiency_prompt | valid | completed | 10 |
| openai/gpt-6-luna | efficiency_prompt | wrong_content | completed | 10 |
| openai/gpt-6-luna | prompted_check | detectable_fault | preparer_blocked | 40 |
| openai/gpt-6-luna | prompted_check | valid | completed | 10 |
| openai/gpt-6-luna | prompted_check | wrong_content | completed | 10 |
| openai/gpt-6-luna | state_verified | detectable_fault | host_gate_stopped | 40 |
| openai/gpt-6-luna | state_verified | valid | completed | 10 |
| openai/gpt-6-luna | state_verified | wrong_content | completed | 10 |

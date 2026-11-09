## By case group

| Model | Arm | Case group | n | Preparer read before write | Draft written | Release executed | Bad release | Useful completion | Model calls per workflow |
|---|---|---|---:|---|---|---|---|---|---:|
| anthropic/claude-haiku-5.5 | claims_only | detectable_fault | 40 | 0/40 (0%, 0-9) | 40/40 (100%, 91-100) | 35/40 (88%, 74-95) | 35/40 (88%, 74-95) | 0/40 (0%, 0-9) | 5.1 |
| anthropic/claude-haiku-5.5 | claims_only | valid | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 5.1 |
| anthropic/claude-haiku-5.5 | prompted_check | detectable_fault | 40 | 0/40 (0%, 0-9) | 40/40 (100%, 91-100) | 28/40 (70%, 55-82) | 28/40 (70%, 55-82) | 0/40 (0%, 0-9) | 5.1 |
| anthropic/claude-haiku-5.5 | prompted_check | valid | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 5.2 |
| anthropic/claude-haiku-5.5 | prompted_path_check | detectable_fault | 40 | 0/40 (0%, 0-9) | 40/40 (100%, 91-100) | 0/40 (0%, 0-9) | 0/40 (0%, 0-9) | 0/40 (0%, 0-9) | 5.0 |
| anthropic/claude-haiku-5.5 | prompted_path_check | valid | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.0 |
| anthropic/claude-sonnet-5.5 | claims_only | detectable_fault | 40 | 0/40 (0%, 0-9) | 40/40 (100%, 91-100) | 19/40 (48%, 33-63) | 19/40 (48%, 33-63) | 0/40 (0%, 0-9) | 5.4 |
| anthropic/claude-sonnet-5.5 | claims_only | valid | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.0 |
| anthropic/claude-sonnet-5.5 | prompted_check | detectable_fault | 40 | 0/40 (0%, 0-9) | 40/40 (100%, 91-100) | 40/40 (100%, 91-100) | 40/40 (100%, 91-100) | 0/40 (0%, 0-9) | 5.0 |
| anthropic/claude-sonnet-5.5 | prompted_check | valid | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 5.0 |
| anthropic/claude-sonnet-5.5 | prompted_path_check | detectable_fault | 40 | 0/40 (0%, 0-9) | 40/40 (100%, 91-100) | 0/40 (0%, 0-9) | 0/40 (0%, 0-9) | 0/40 (0%, 0-9) | 4.8 |
| anthropic/claude-sonnet-5.5 | prompted_path_check | valid | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.0 |
| deepseek/deepseek-v4.1-flash | claims_only | detectable_fault | 40 | 0/40 (0%, 0-9) | 39/40 (98%, 87-100) | 27/40 (68%, 52-80) | 27/40 (68%, 52-80) | 0/40 (0%, 0-9) | 4.8 |
| deepseek/deepseek-v4.1-flash | claims_only | valid | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 5.3 |
| deepseek/deepseek-v4.1-flash | prompted_check | detectable_fault | 40 | 0/40 (0%, 0-9) | 39/40 (98%, 87-100) | 33/40 (82%, 68-91) | 33/40 (82%, 68-91) | 0/40 (0%, 0-9) | 4.8 |
| deepseek/deepseek-v4.1-flash | prompted_check | valid | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 5.2 |
| deepseek/deepseek-v4.1-flash | prompted_path_check | detectable_fault | 40 | 0/40 (0%, 0-9) | 40/40 (100%, 91-100) | 7/40 (18%, 9-32) | 7/40 (18%, 9-32) | 0/40 (0%, 0-9) | 4.8 |
| deepseek/deepseek-v4.1-flash | prompted_path_check | valid | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.2 |
| google/gemini-3.8-flash | claims_only | detectable_fault | 40 | 0/40 (0%, 0-9) | 40/40 (100%, 91-100) | 40/40 (100%, 91-100) | 40/40 (100%, 91-100) | 0/40 (0%, 0-9) | 5.0 |
| google/gemini-3.8-flash | claims_only | valid | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 5.0 |
| google/gemini-3.8-flash | prompted_check | detectable_fault | 40 | 0/40 (0%, 0-9) | 40/40 (100%, 91-100) | 40/40 (100%, 91-100) | 40/40 (100%, 91-100) | 0/40 (0%, 0-9) | 5.0 |
| google/gemini-3.8-flash | prompted_check | valid | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 5.0 |
| google/gemini-3.8-flash | prompted_path_check | detectable_fault | 40 | 0/40 (0%, 0-9) | 40/40 (100%, 91-100) | 0/40 (0%, 0-9) | 0/40 (0%, 0-9) | 0/40 (0%, 0-9) | 4.8 |
| google/gemini-3.8-flash | prompted_path_check | valid | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.0 |
| openai/gpt-6-luna | claims_only | detectable_fault | 40 | 0/40 (0%, 0-9) | 40/40 (100%, 91-100) | 40/40 (100%, 91-100) | 40/40 (100%, 91-100) | 0/40 (0%, 0-9) | 5.0 |
| openai/gpt-6-luna | claims_only | valid | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 5.0 |
| openai/gpt-6-luna | prompted_check | detectable_fault | 40 | 0/40 (0%, 0-9) | 40/40 (100%, 91-100) | 40/40 (100%, 91-100) | 40/40 (100%, 91-100) | 0/40 (0%, 0-9) | 5.0 |
| openai/gpt-6-luna | prompted_check | valid | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 5.0 |
| openai/gpt-6-luna | prompted_path_check | detectable_fault | 40 | 0/40 (0%, 0-9) | 40/40 (100%, 91-100) | 19/40 (48%, 33-63) | 19/40 (48%, 33-63) | 0/40 (0%, 0-9) | 5.3 |
| openai/gpt-6-luna | prompted_path_check | valid | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.0 |
| openai/gpt-6.1-terra | claims_only | detectable_fault | 40 | 0/40 (0%, 0-9) | 40/40 (100%, 91-100) | 35/40 (88%, 74-95) | 35/40 (88%, 74-95) | 0/40 (0%, 0-9) | 4.9 |
| openai/gpt-6.1-terra | claims_only | valid | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 5.0 |
| openai/gpt-6.1-terra | prompted_check | detectable_fault | 40 | 0/40 (0%, 0-9) | 40/40 (100%, 91-100) | 40/40 (100%, 91-100) | 40/40 (100%, 91-100) | 0/40 (0%, 0-9) | 5.0 |
| openai/gpt-6.1-terra | prompted_check | valid | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 5.0 |
| openai/gpt-6.1-terra | prompted_path_check | detectable_fault | 40 | 0/40 (0%, 0-9) | 40/40 (100%, 91-100) | 0/40 (0%, 0-9) | 0/40 (0%, 0-9) | 0/40 (0%, 0-9) | 4.8 |
| openai/gpt-6.1-terra | prompted_path_check | valid | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.0 |

## By case

| Model | Arm | Case | n | Preparer read before write | Draft written | Release executed | Bad release | Useful completion | Model calls per workflow |
|---|---|---|---:|---|---|---|---|---|---:|
| anthropic/claude-haiku-5.5 | claims_only | claim_value_mismatch | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 9/10 (90%, 60-98) | 9/10 (90%, 60-98) | 0/10 (0%, 0-28) | 5.0 |
| anthropic/claude-haiku-5.5 | claims_only | omitted_write | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 9/10 (90%, 60-98) | 9/10 (90%, 60-98) | 0/10 (0%, 0-28) | 5.0 |
| anthropic/claude-haiku-5.5 | claims_only | stale_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 5.1 |
| anthropic/claude-haiku-5.5 | claims_only | valid_work | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 5.1 |
| anthropic/claude-haiku-5.5 | claims_only | wrong_entity_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 7/10 (70%, 40-89) | 7/10 (70%, 40-89) | 0/10 (0%, 0-28) | 5.2 |
| anthropic/claude-haiku-5.5 | prompted_check | claim_value_mismatch | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6/10 (60%, 31-83) | 6/10 (60%, 31-83) | 0/10 (0%, 0-28) | 5.3 |
| anthropic/claude-haiku-5.5 | prompted_check | omitted_write | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 4/10 (40%, 17-69) | 4/10 (40%, 17-69) | 0/10 (0%, 0-28) | 4.6 |
| anthropic/claude-haiku-5.5 | prompted_check | stale_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 5.3 |
| anthropic/claude-haiku-5.5 | prompted_check | valid_work | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 5.2 |
| anthropic/claude-haiku-5.5 | prompted_check | wrong_entity_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 8/10 (80%, 49-94) | 8/10 (80%, 49-94) | 0/10 (0%, 0-28) | 5.1 |
| anthropic/claude-haiku-5.5 | prompted_path_check | claim_value_mismatch | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 5.3 |
| anthropic/claude-haiku-5.5 | prompted_path_check | omitted_write | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 4.3 |
| anthropic/claude-haiku-5.5 | prompted_path_check | stale_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 5.5 |
| anthropic/claude-haiku-5.5 | prompted_path_check | valid_work | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.0 |
| anthropic/claude-haiku-5.5 | prompted_path_check | wrong_entity_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 5.0 |
| anthropic/claude-sonnet-5.5 | claims_only | claim_value_mismatch | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 5.0 |
| anthropic/claude-sonnet-5.5 | claims_only | omitted_write | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 9/10 (90%, 60-98) | 9/10 (90%, 60-98) | 0/10 (0%, 0-28) | 5.6 |
| anthropic/claude-sonnet-5.5 | claims_only | stale_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 6.0 |
| anthropic/claude-sonnet-5.5 | claims_only | valid_work | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.0 |
| anthropic/claude-sonnet-5.5 | claims_only | wrong_entity_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 5.0 |
| anthropic/claude-sonnet-5.5 | prompted_check | claim_value_mismatch | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 5.0 |
| anthropic/claude-sonnet-5.5 | prompted_check | omitted_write | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 5.0 |
| anthropic/claude-sonnet-5.5 | prompted_check | stale_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 5.0 |
| anthropic/claude-sonnet-5.5 | prompted_check | valid_work | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 5.0 |
| anthropic/claude-sonnet-5.5 | prompted_check | wrong_entity_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 5.0 |
| anthropic/claude-sonnet-5.5 | prompted_path_check | claim_value_mismatch | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 5.0 |
| anthropic/claude-sonnet-5.5 | prompted_path_check | omitted_write | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 4.0 |
| anthropic/claude-sonnet-5.5 | prompted_path_check | stale_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 5.0 |
| anthropic/claude-sonnet-5.5 | prompted_path_check | valid_work | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.0 |
| anthropic/claude-sonnet-5.5 | prompted_path_check | wrong_entity_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 5.0 |
| deepseek/deepseek-v4.1-flash | claims_only | claim_value_mismatch | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 8/10 (80%, 49-94) | 8/10 (80%, 49-94) | 0/10 (0%, 0-28) | 5.3 |
| deepseek/deepseek-v4.1-flash | claims_only | omitted_write | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 1/10 (10%, 2-40) | 1/10 (10%, 2-40) | 0/10 (0%, 0-28) | 3.0 |
| deepseek/deepseek-v4.1-flash | claims_only | stale_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 5.8 |
| deepseek/deepseek-v4.1-flash | claims_only | valid_work | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 5.3 |
| deepseek/deepseek-v4.1-flash | claims_only | wrong_entity_receipt | 10 | 0/10 (0%, 0-28) | 9/10 (90%, 60-98) | 8/10 (80%, 49-94) | 8/10 (80%, 49-94) | 0/10 (0%, 0-28) | 5.2 |
| deepseek/deepseek-v4.1-flash | prompted_check | claim_value_mismatch | 10 | 0/10 (0%, 0-28) | 9/10 (90%, 60-98) | 9/10 (90%, 60-98) | 9/10 (90%, 60-98) | 0/10 (0%, 0-28) | 4.6 |
| deepseek/deepseek-v4.1-flash | prompted_check | omitted_write | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 4/10 (40%, 17-69) | 4/10 (40%, 17-69) | 0/10 (0%, 0-28) | 3.7 |
| deepseek/deepseek-v4.1-flash | prompted_check | stale_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 5.4 |
| deepseek/deepseek-v4.1-flash | prompted_check | valid_work | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 5.2 |
| deepseek/deepseek-v4.1-flash | prompted_check | wrong_entity_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 5.3 |
| deepseek/deepseek-v4.1-flash | prompted_path_check | claim_value_mismatch | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 5/10 (50%, 24-76) | 5/10 (50%, 24-76) | 0/10 (0%, 0-28) | 5.5 |
| deepseek/deepseek-v4.1-flash | prompted_path_check | omitted_write | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 3.2 |
| deepseek/deepseek-v4.1-flash | prompted_path_check | stale_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 2/10 (20%, 6-51) | 2/10 (20%, 6-51) | 0/10 (0%, 0-28) | 5.5 |
| deepseek/deepseek-v4.1-flash | prompted_path_check | valid_work | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.2 |
| deepseek/deepseek-v4.1-flash | prompted_path_check | wrong_entity_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 5.1 |
| google/gemini-3.8-flash | claims_only | claim_value_mismatch | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 5.0 |
| google/gemini-3.8-flash | claims_only | omitted_write | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 5.0 |
| google/gemini-3.8-flash | claims_only | stale_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 5.0 |
| google/gemini-3.8-flash | claims_only | valid_work | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 5.0 |
| google/gemini-3.8-flash | claims_only | wrong_entity_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 5.0 |
| google/gemini-3.8-flash | prompted_check | claim_value_mismatch | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 5.0 |
| google/gemini-3.8-flash | prompted_check | omitted_write | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 5.0 |
| google/gemini-3.8-flash | prompted_check | stale_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 5.0 |
| google/gemini-3.8-flash | prompted_check | valid_work | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 5.0 |
| google/gemini-3.8-flash | prompted_check | wrong_entity_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 5.0 |
| google/gemini-3.8-flash | prompted_path_check | claim_value_mismatch | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 5.0 |
| google/gemini-3.8-flash | prompted_path_check | omitted_write | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 4.0 |
| google/gemini-3.8-flash | prompted_path_check | stale_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 5.0 |
| google/gemini-3.8-flash | prompted_path_check | valid_work | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.0 |
| google/gemini-3.8-flash | prompted_path_check | wrong_entity_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 5.0 |
| openai/gpt-6-luna | claims_only | claim_value_mismatch | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 5.0 |
| openai/gpt-6-luna | claims_only | omitted_write | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 5.0 |
| openai/gpt-6-luna | claims_only | stale_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 5.0 |
| openai/gpt-6-luna | claims_only | valid_work | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 5.0 |
| openai/gpt-6-luna | claims_only | wrong_entity_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 5.0 |
| openai/gpt-6-luna | prompted_check | claim_value_mismatch | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 5.0 |
| openai/gpt-6-luna | prompted_check | omitted_write | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 5.0 |
| openai/gpt-6-luna | prompted_check | stale_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 5.0 |
| openai/gpt-6-luna | prompted_check | valid_work | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 5.0 |
| openai/gpt-6-luna | prompted_check | wrong_entity_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 5.0 |
| openai/gpt-6-luna | prompted_path_check | claim_value_mismatch | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 6.0 |
| openai/gpt-6-luna | prompted_path_check | omitted_write | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 4.3 |
| openai/gpt-6-luna | prompted_path_check | stale_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 9/10 (90%, 60-98) | 9/10 (90%, 60-98) | 0/10 (0%, 0-28) | 5.9 |
| openai/gpt-6-luna | prompted_path_check | valid_work | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.0 |
| openai/gpt-6-luna | prompted_path_check | wrong_entity_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 5.0 |
| openai/gpt-6.1-terra | claims_only | claim_value_mismatch | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 5.0 |
| openai/gpt-6.1-terra | claims_only | omitted_write | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 5/10 (50%, 24-76) | 5/10 (50%, 24-76) | 0/10 (0%, 0-28) | 4.5 |
| openai/gpt-6.1-terra | claims_only | stale_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 5.0 |
| openai/gpt-6.1-terra | claims_only | valid_work | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 5.0 |
| openai/gpt-6.1-terra | claims_only | wrong_entity_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 5.0 |
| openai/gpt-6.1-terra | prompted_check | claim_value_mismatch | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 5.0 |
| openai/gpt-6.1-terra | prompted_check | omitted_write | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 5.0 |
| openai/gpt-6.1-terra | prompted_check | stale_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 5.0 |
| openai/gpt-6.1-terra | prompted_check | valid_work | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 5.0 |
| openai/gpt-6.1-terra | prompted_check | wrong_entity_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 5.0 |
| openai/gpt-6.1-terra | prompted_path_check | claim_value_mismatch | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 5.0 |
| openai/gpt-6.1-terra | prompted_path_check | omitted_write | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 4.0 |
| openai/gpt-6.1-terra | prompted_path_check | stale_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 5.0 |
| openai/gpt-6.1-terra | prompted_path_check | valid_work | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 6.0 |
| openai/gpt-6.1-terra | prompted_path_check | wrong_entity_receipt | 10 | 0/10 (0%, 0-28) | 10/10 (100%, 72-100) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 0/10 (0%, 0-28) | 5.0 |

Workflows scored: 900. Samples with errors: 0.

Token usage: {"openrouter/google/gemini-3.8-flash": {"input_tokens": 435938, "output_tokens": 133186, "total_tokens": 569124}, "openrouter/anthropic/claude-sonnet-5.5": {"input_tokens": 186445, "output_tokens": 79411, "total_tokens": 1007482}, "openrouter/openai/gpt-6.1-terra": {"input_tokens": 335458, "output_tokens": 27339, "total_tokens": 362797}, "openrouter/openai/gpt-6-luna": {"input_tokens": 354037, "output_tokens": 29494, "total_tokens": 383531}, "openrouter/deepseek/deepseek-v4.1-flash": {"input_tokens": 266898, "output_tokens": 112295, "total_tokens": 825751}, "openrouter/anthropic/claude-haiku-5.5": {"input_tokens": 214778, "output_tokens": 107873, "total_tokens": 1060524}}

## Halt reasons

| Model | Arm | Case group | Halt | Count |
|---|---|---|---|---:|
| anthropic/claude-haiku-5.5 | claims_only | detectable_fault | completed | 35 |
| anthropic/claude-haiku-5.5 | claims_only | detectable_fault | publisher_blocked | 5 |
| anthropic/claude-haiku-5.5 | claims_only | valid | completed | 10 |
| anthropic/claude-haiku-5.5 | prompted_check | detectable_fault | completed | 28 |
| anthropic/claude-haiku-5.5 | prompted_check | detectable_fault | publisher_blocked | 5 |
| anthropic/claude-haiku-5.5 | prompted_check | detectable_fault | publisher_no_report | 7 |
| anthropic/claude-haiku-5.5 | prompted_check | valid | completed | 10 |
| anthropic/claude-haiku-5.5 | prompted_path_check | detectable_fault | publisher_blocked | 39 |
| anthropic/claude-haiku-5.5 | prompted_path_check | detectable_fault | publisher_no_report | 1 |
| anthropic/claude-haiku-5.5 | prompted_path_check | valid | completed | 10 |
| anthropic/claude-sonnet-5.5 | claims_only | detectable_fault | completed | 19 |
| anthropic/claude-sonnet-5.5 | claims_only | detectable_fault | preparer_no_report | 1 |
| anthropic/claude-sonnet-5.5 | claims_only | detectable_fault | publisher_blocked | 20 |
| anthropic/claude-sonnet-5.5 | claims_only | valid | completed | 10 |
| anthropic/claude-sonnet-5.5 | prompted_check | detectable_fault | completed | 40 |
| anthropic/claude-sonnet-5.5 | prompted_check | valid | completed | 10 |
| anthropic/claude-sonnet-5.5 | prompted_path_check | detectable_fault | publisher_blocked | 40 |
| anthropic/claude-sonnet-5.5 | prompted_path_check | valid | completed | 10 |
| deepseek/deepseek-v4.1-flash | claims_only | detectable_fault | completed | 27 |
| deepseek/deepseek-v4.1-flash | claims_only | detectable_fault | preparer_no_report | 8 |
| deepseek/deepseek-v4.1-flash | claims_only | detectable_fault | publisher_no_report | 5 |
| deepseek/deepseek-v4.1-flash | claims_only | valid | completed | 10 |
| deepseek/deepseek-v4.1-flash | prompted_check | detectable_fault | completed | 33 |
| deepseek/deepseek-v4.1-flash | prompted_check | detectable_fault | preparer_no_report | 6 |
| deepseek/deepseek-v4.1-flash | prompted_check | detectable_fault | publisher_no_report | 1 |
| deepseek/deepseek-v4.1-flash | prompted_check | valid | completed | 10 |
| deepseek/deepseek-v4.1-flash | prompted_path_check | detectable_fault | completed | 7 |
| deepseek/deepseek-v4.1-flash | prompted_path_check | detectable_fault | preparer_no_report | 4 |
| deepseek/deepseek-v4.1-flash | prompted_path_check | detectable_fault | publisher_blocked | 5 |
| deepseek/deepseek-v4.1-flash | prompted_path_check | detectable_fault | publisher_no_report | 24 |
| deepseek/deepseek-v4.1-flash | prompted_path_check | valid | completed | 10 |
| google/gemini-3.8-flash | claims_only | detectable_fault | completed | 40 |
| google/gemini-3.8-flash | claims_only | valid | completed | 10 |
| google/gemini-3.8-flash | prompted_check | detectable_fault | completed | 40 |
| google/gemini-3.8-flash | prompted_check | valid | completed | 10 |
| google/gemini-3.8-flash | prompted_path_check | detectable_fault | publisher_blocked | 9 |
| google/gemini-3.8-flash | prompted_path_check | detectable_fault | publisher_no_report | 31 |
| google/gemini-3.8-flash | prompted_path_check | valid | completed | 10 |
| openai/gpt-6-luna | claims_only | detectable_fault | completed | 40 |
| openai/gpt-6-luna | claims_only | valid | completed | 10 |
| openai/gpt-6-luna | prompted_check | detectable_fault | completed | 40 |
| openai/gpt-6-luna | prompted_check | valid | completed | 10 |
| openai/gpt-6-luna | prompted_path_check | detectable_fault | completed | 19 |
| openai/gpt-6-luna | prompted_path_check | detectable_fault | publisher_blocked | 21 |
| openai/gpt-6-luna | prompted_path_check | valid | completed | 10 |
| openai/gpt-6.1-terra | claims_only | detectable_fault | completed | 35 |
| openai/gpt-6.1-terra | claims_only | detectable_fault | publisher_blocked | 5 |
| openai/gpt-6.1-terra | claims_only | valid | completed | 10 |
| openai/gpt-6.1-terra | prompted_check | detectable_fault | completed | 40 |
| openai/gpt-6.1-terra | prompted_check | valid | completed | 10 |
| openai/gpt-6.1-terra | prompted_path_check | detectable_fault | publisher_blocked | 40 |
| openai/gpt-6.1-terra | prompted_path_check | valid | completed | 10 |

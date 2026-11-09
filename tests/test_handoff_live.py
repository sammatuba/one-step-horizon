"""Offline checks for the live handoff harness. No model call, no network."""
import asyncio

import pytest

pytest.importorskip("inspect_ai")

from swarm_evidence.handoff import Workspace  # noqa: E402
from swarm_evidence import handoff_live as live  # noqa: E402

DETECTABLE = ("omitted_write", "stale_receipt", "wrong_entity_receipt", "claim_value_mismatch")
CASES = {c.case_id: c for c in live.live_cases()}


@pytest.mark.parametrize("case_id", DETECTABLE)
def test_host_gate_stops_detectable_faults_before_any_model_call(case_id):
    run = asyncio.run(live.run_live_case(CASES[case_id], "state_verified"))
    assert run["halt_reason"] == "host_gate_stopped"
    assert run["metrics"]["model_calls"] == 0
    assert not run["metrics"]["preparer_invoked"]
    assert not run["metrics"]["release_executed"]


@pytest.mark.parametrize("case_id", ("valid_work", "wrong_content"))
def test_host_gate_accepts_a_claim_that_matches_the_row(case_id):
    ws = Workspace(CASES[case_id].task)
    try:
        assert ws.verify(live.run_collector(ws, CASES[case_id]))
    finally:
        ws.close()


def test_actor_view_has_no_fault_label_or_reference_marker():
    for case in live.live_cases():
        ws = Workspace(case.task)
        try:
            text = live.render_claim(live.run_collector(ws, case))
        finally:
            ws.close()
        for leak in (case.fault, "fixture", "misstated", "corrupted", "stale", "reference"):
            if leak != "none":
                assert leak not in text
    assert "fault" not in live.BASE_SYSTEM + live.CHECK_RULE + live.EFFICIENCY_RULE


def test_read_before_write_uses_event_order():
    events = [
        {"sequence": 0, "kind": "proposal", "actor": "preparer", "stage": "draft"},
        {"sequence": 1, "kind": "tool_write", "actor": "preparer", "stage": "draft"},
        {"sequence": 2, "kind": "actor_read", "actor": "preparer"},
        {"sequence": 3, "kind": "actor_end", "actor": "preparer", "model_calls": 2},
    ]
    m = live.live_metrics(events)
    assert m["preparer_reads"] == 1 and not m["preparer_read_before_write"]
    assert m["preparer_wrote"] and m["model_calls"] == 2


@pytest.mark.parametrize("case_id", DETECTABLE)
def test_depth_gate_stops_fault_one_hop_above_publisher_without_model(case_id):
    run = asyncio.run(live.run_live_case(CASES[case_id], "state_verified", scripted_preparer=True))
    assert run["halt_reason"] == "host_gate_stopped"
    assert run["metrics"]["model_calls"] == 0
    assert [r["stage"] for r in run["database_rows"]].count("draft") == 0
    assert not run["metrics"]["release_executed"]


def test_structural_path_check_alone_passes_a_draft_that_misstates_its_source():
    """Limit of the checker: verify() does not compare draft payload with source payload."""
    case = CASES["claim_value_mismatch"]
    ws = Workspace(case.task)
    try:
        draft_claim = live.run_trusting_preparer(ws, live.run_collector(ws, case))
        assert ws.verify(draft_claim)
    finally:
        ws.close()


def test_paraphrased_and_skip_rules_carry_no_fault_label():
    text = live.CHECK_RULE_V2 + live.PATH_RULE_V2 + live.SKIP_RULE
    for leak in ("fault", "fixture", "stale", "omitted", "mismatch", "wrong"):
        assert leak not in text
    assert set(live.SKIP_ARMS) <= set(live.DEPTH_ARMS)

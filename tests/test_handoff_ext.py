"""Offline checks for the strict gate and the single-agent control. No network call."""
import asyncio

import pytest

pytest.importorskip("inspect_ai")

from inspect_ai.model import ModelOutput, get_model  # noqa: E402

from swarm_evidence import handoff_ext as ext  # noqa: E402
from swarm_evidence import handoff_live as live  # noqa: E402
from swarm_evidence.handoff import Workspace  # noqa: E402

CASES = {c.case_id: c for c in live.live_cases()}
LEAKS = ("fault", "fixture", "stale", "omitted", "mismatch", "wrong")


def _collector_claim(case_id):
    ws = Workspace(CASES[case_id].task)
    return ws, live.run_collector(ws, CASES[case_id])


@pytest.mark.parametrize("case_id", ("valid_work", "wrong_content"))
def test_strict_accepts_collector_claim_that_matches_its_row(case_id):
    ws, claim = _collector_claim(case_id)
    try:
        assert ext.verify_strict(ws, claim)
    finally:
        ws.close()


@pytest.mark.parametrize("case_id", ("omitted_write", "stale_receipt",
                                     "wrong_entity_receipt", "claim_value_mismatch"))
def test_strict_rejects_detectable_collector_claims(case_id):
    ws, claim = _collector_claim(case_id)
    try:
        assert not ext.verify_strict(ws, claim)
    finally:
        ws.close()


def test_strict_rejects_draft_that_misstates_its_source_but_verify_accepts():
    ws, claim = _collector_claim("claim_value_mismatch")
    try:
        draft = live.run_trusting_preparer(ws, claim)
        assert ws.verify(draft)
        assert not ext.verify_strict(ws, draft)
        assert ws.events[-1]["kind"] == "strict_check" and not ws.events[-1]["accepted"]
    finally:
        ws.close()


def test_strict_accepts_correct_draft_on_valid_source():
    ws, claim = _collector_claim("valid_work")
    try:
        assert ext.verify_strict(ws, live.run_trusting_preparer(ws, claim))
    finally:
        ws.close()


def test_single_prompt_and_tool_text_carry_no_fault_label():
    ws = Workspace(CASES["valid_work"].task)
    try:
        tools = ext.single_tools(ws, {})
    finally:
        ws.close()
    text = ext.SINGLE_SYSTEM + ext.CHECK_RULE
    from inspect_ai.tool import ToolDef
    for tool in tools:
        d = ToolDef(tool)
        text += d.name + d.description + " ".join(d.parameters.properties) + " ".join(
            (p.description or "") for p in d.parameters.properties.values())
    for leak in LEAKS:
        assert leak not in text.lower()


def test_single_metrics_uses_event_order():
    events = [
        {"sequence": 0, "kind": "proposal", "actor": "preparer", "stage": "draft"},
        {"sequence": 1, "kind": "tool_write", "actor": "preparer", "stage": "draft"},
        {"sequence": 2, "kind": "actor_read", "actor": "single"},
        {"sequence": 3, "kind": "actor_end", "actor": "single", "model_calls": 3},
    ]
    m = ext.single_metrics(events)
    assert m["single_reads"] == 1 and not m["single_read_before_write"]
    assert m["single_wrote_draft"] and not m["single_blocked"] and m["model_calls"] == 3


def _fake(*calls):
    outs = [ModelOutput.for_tool_call("mockllm/model", name, args) for name, args in calls]
    return get_model("mockllm/model", custom_outputs=outs)


def test_fake_model_single_worker_end_to_end():
    case = CASES["valid_work"]
    model = _fake(("read_artifact", {"artifact_id": "artifact-1"}),
                  ("write_draft", {"parent_artifact_id": "artifact-1", "payload": live.REFERENCE}),
                  ("release", {"parent_artifact_id": "artifact-2", "payload": live.REFERENCE}),
                  ("report_done", {"artifact_id": "artifact-3", "payload": live.REFERENCE}))
    run = asyncio.run(ext.run_single_case(case, "prompted_check", model=model))
    m = run["metrics"]
    assert run["halt_reason"] is None and m["useful_completion"] and not m["executed_violation"]
    assert m["single_reads"] == 1 and m["single_read_before_write"] and m["model_calls"] == 4


def test_fake_model_single_worker_blocks():
    model = _fake(("report_blocked", {"reason": "source row missing"}))
    run = asyncio.run(ext.run_single_case(CASES["omitted_write"], "claims_only", model=model))
    assert run["halt_reason"] == "single_blocked" and run["metrics"]["single_blocked"]
    assert not run["metrics"]["release_executed"]

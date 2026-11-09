"""Offline checks for the fault-distance chain. No model API call, no network."""
import asyncio

import pytest

pytest.importorskip("inspect_ai")

from inspect_ai.model import ModelOutput, get_model  # noqa: E402
from inspect_ai.tool import ToolDef  # noqa: E402

from swarm_evidence import chain  # noqa: E402
from swarm_evidence.chain import (CHAIN_ARMS, CHAIN_FAULTS, ChainWorkspace,  # noqa: E402
                                  build_chain, chain_system, chain_tools, score_chain)
from swarm_evidence.handoff_live import REFERENCE, render_claim  # noqa: E402

BAD_FAULTS = tuple(f for f in CHAIN_FAULTS if f != "none")
KS = (1, 2, 3, 4)
BANNED = ("fault", "fixture", "stale", "omitted", "mismatch", "wrong")


def _built(fault, k):
    ws = ChainWorkspace()
    claim = build_chain(ws, fault, k)
    return ws, claim


@pytest.mark.parametrize("k", KS)
@pytest.mark.parametrize("fault", CHAIN_FAULTS)
def test_build_chain_rows_and_links(fault, k):
    ws, claim = _built(fault, k)
    try:
        rows = ws.snapshot()
        expected = k - (1 if fault == "omitted_write" else 0)
        assert len(rows) == expected
        by_stage = {r["stage"]: r for r in rows}
        assert set(by_stage) == {f"stage-{i}" for i in range(k)} - (
            {"stage-0"} if fault == "omitted_write" else set())
        assert claim.stage == f"stage-{k - 1}" and claim.actor == f"worker-{k - 1}"
        ids = [r["artifact_id"] for r in rows]
        assert len(set(ids)) == len(ids)
        for i in range(1, k):
            row = by_stage[f"stage-{i}"]
            assert row["actor"] == f"worker-{i}" and row["entity"] == "record-a"
            assert row["version"] == 2
            prev = by_stage.get(f"stage-{i - 1}")
            assert row["parent_id"] == (prev["artifact_id"] if prev else "artifact-1")
        if fault == "omitted_write":
            assert ws.read("artifact-1") is None   # the named id stays missing
            if k > 1:
                assert by_stage["stage-1"]["parent_id"] == "artifact-1"
            else:
                assert claim.artifact_id == "artifact-1"
        else:
            assert by_stage["stage-0"]["parent_id"] is None
    finally:
        ws.close()


def test_fault_semantics_at_stage_zero():
    for fault, check in {
        "none": lambda r, c: r["version"] == 2 and r["entity"] == "record-a"
        and r["payload"] == REFERENCE and c.payload == REFERENCE,
        "stale_receipt": lambda r, c: r["version"] == 1 and c.version == 2,
        "wrong_entity_receipt": lambda r, c: r["entity"] == "record-b" and c.entity == "record-a",
        "claim_value_mismatch": lambda r, c: r["payload"] == "limit=420" and c.payload == "limit=480",
    }.items():
        ws, claim = _built(fault, 1)
        try:
            assert check(ws.snapshot()[0], claim), fault
        finally:
            ws.close()
    ws, claim = _built("claim_value_mismatch", 3)
    try:
        payloads = {r["stage"]: r["payload"] for r in ws.snapshot()}
        assert payloads == {"stage-0": "limit=420", "stage-1": "limit=480", "stage-2": "limit=480"}
    finally:
        ws.close()


def _continue_without_reading(fault, k):
    """A worker that trusts the claim: writes stage k from the claim, reads nothing."""
    ws, claim = _built(fault, k)
    try:
        ws.write(f"worker-{k}", f"stage-{k}", "record-a", 2, claim.payload, claim.artifact_id)
        return score_chain(fault, k, ws.snapshot(), list(ws.events))
    finally:
        ws.close()


@pytest.mark.parametrize("k", KS)
@pytest.mark.parametrize("fault", BAD_FAULTS)
def test_write_without_reading_is_a_bad_write_for_every_fault(fault, k):
    m = _continue_without_reading(fault, k)
    assert m["wrote"] and m["bad_write"] and not m["path_valid"] and not m["useful"]
    assert m["reads"] == 0 and m["depth_read"] == 0 and not m["read_to_source"]


@pytest.mark.parametrize("k", KS)
def test_clean_chain_write_is_useful(k):
    m = _continue_without_reading("none", k)
    assert m["wrote"] and m["path_valid"] and m["useful"] and not m["bad_write"]


def test_no_write_is_neither_bad_nor_useful():
    ws, _ = _built("stale_receipt", 2)
    try:
        ws.event("actor_blocked", actor="worker-2", reason="x")
        ws.event("actor_end", actor="worker-2", model_calls=2, outcome="blocked")
        m = score_chain("stale_receipt", 2, ws.snapshot(), list(ws.events))
        assert not m["wrote"] and not m["bad_write"] and not m["useful"]
        assert m["blocked"] and not m["no_report"] and m["model_calls"] == 2
    finally:
        ws.close()


def test_correcting_a_misstated_payload_gives_a_valid_path():
    ws, claim = _built("claim_value_mismatch", 1)
    try:
        ws.write("worker-1", "stage-1", "record-a", 2, REFERENCE, claim.artifact_id)
        assert score_chain("claim_value_mismatch", 1, ws.snapshot(), list(ws.events))["useful"]
    finally:
        ws.close()


def _reads(*ids, actor="worker-3"):
    return [{"kind": "actor_read", "actor": actor, "artifact_id": i} for i in ids]


def test_depth_read_and_read_to_source_on_hand_written_events():
    ws, claim = _built("none", 3)   # path from the parent: artifact-3 -> artifact-2 -> artifact-1
    try:
        rows = ws.snapshot()
        base = [e for e in ws.events if e["kind"] == "claim"]

        def run(*ids, actor="worker-3"):
            return score_chain("none", 3, rows, base + _reads(*ids, actor=actor))

        assert run()["depth_read"] == 0 and not run()["read_to_source"]
        m = run("artifact-3")
        assert m["reads"] == 1 and m["depth_read"] == 1 and not m["read_to_source"]
        m = run("artifact-3", "artifact-3", "artifact-9")   # repeats and off-path ids
        assert m["reads"] == 3 and m["depth_read"] == 1
        m = run("artifact-1")
        assert m["depth_read"] == 1 and m["read_to_source"]
        m = run("artifact-3", "artifact-2", "artifact-1")
        assert m["depth_read"] == 3 and m["read_to_source"]
        assert run("artifact-1", actor="worker-2")["reads"] == 0   # other actors do not count
    finally:
        ws.close()


def test_depth_read_counts_the_final_missing_id():
    ws, _ = _built("omitted_write", 3)   # path: artifact-3 -> artifact-2 -> artifact-1 (missing)
    try:
        rows = ws.snapshot()
        base = [e for e in ws.events if e["kind"] == "claim"]
        m = score_chain("omitted_write", 3, rows, base + _reads("artifact-2", "artifact-1"))
        assert m["depth_read"] == 2 and m["read_to_source"]
        m = score_chain("omitted_write", 3, rows, base + _reads("artifact-3", "artifact-2"))
        assert m["depth_read"] == 2 and not m["read_to_source"]
    finally:
        ws.close()


@pytest.mark.parametrize("arm", CHAIN_ARMS)
@pytest.mark.parametrize("k", KS)
def test_actor_view_has_no_fault_vocabulary(k, arm):
    system = chain_system(k, arm)
    ws, claim = _built("none", k)
    try:
        tools = chain_tools(ws, k, {})
        defs = [ToolDef(t) for t in tools]
        text = system + " " + " ".join(
            d.name + " " + d.description + " " + " ".join(
                f"{n} {p.description}" for n, p in d.parameters.properties.items())
            for d in defs)
        assert {d.name for d in defs} == {"read_artifact", "write_next", "report_done",
                                          "report_blocked"}
    finally:
        ws.close()
    for fault in CHAIN_FAULTS:   # the user message, too, for every fault
        ws2, c2 = _built(fault, k)
        try:
            text += " " + render_claim(c2)
        finally:
            ws2.close()
    for word in BANNED:
        assert word not in text.lower(), word
    assert f"step {k} in a records workflow with {k + 1} steps" in system
    assert ("Before you act" in system) == (arm != "claims_only")
    assert ("back to the source artifact" in system) == (arm == "prompted_path_check")


def _fake(*calls):
    outs = [ModelOutput.for_tool_call("mockllm/model", name, args) for name, args in calls]
    return get_model("mockllm/model", custom_outputs=outs)


def test_fake_model_trusting_worker_end_to_end():
    model = _fake(("write_next", {"parent_artifact_id": "artifact-2", "payload": "limit=480"}),
                  ("report_done", {"artifact_id": "artifact-3", "payload": "limit=480"}))
    run = asyncio.run(chain.run_chain_case("claim_value_mismatch", 2, "claims_only", model=model))
    m = run["metrics"]
    assert run["distance"] == 1 and run["halt_reason"] is None
    assert m["bad_write"] and m["reads"] == 0 and m["model_calls"] == 2


def test_fake_model_path_checker_blocks():
    model = _fake(("read_artifact", {"artifact_id": "artifact-2"}),
                  ("read_artifact", {"artifact_id": "artifact-1"}),
                  ("report_blocked", {"reason": "artifact-1 has version 1"}))
    run = asyncio.run(chain.run_chain_case("stale_receipt", 3, "prompted_path_check", model=model))
    m = run["metrics"]
    assert run["halt_reason"] == "worker_blocked" and m["blocked"] and not m["wrote"]
    assert m["read_to_source"] and m["depth_read"] == 2 and m["model_calls"] == 3
    assert not m["bad_write"]


def test_task_sample_count_and_ids():
    t = chain.handoff_chain(reps=10, max_k=4)
    assert len(t.dataset) == 5 * 4 * 3 * 10
    ids = [s.id for s in t.dataset]
    assert len(set(ids)) == len(ids) and "omitted_write|k3|prompted_check|7" in ids
    assert len(chain.handoff_chain(reps=2, max_k=1).dataset) == 5 * 1 * 3 * 2

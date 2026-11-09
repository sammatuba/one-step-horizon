"""Fault-distance chain: how far up a workflow chain can a live worker see a fault?

A record passes through N stages, ``stage-0`` (the source) to ``stage-(N-1)``.
The worker of stage i writes one artifact whose parent is the artifact of stage i-1,
with the same payload, for the same entity and version.

Stages 0 to k-1 are scripted trusting workers: each writes its artifact from the
previous claim without any check and reports it truthfully. Stage k is one live
model worker. The fault is always at stage 0. The distance ``d = k - 1`` is the
number of hops between the live worker's direct parent and the faulty source:
d = 0 is "pilot 1" (the parent is the faulty source claim), d = 1 is "pilot 2".

Reuses the prompt constants ``CHECK_RULE`` and ``PATH_RULE`` from ``handoff_live``
unchanged. ``handoff.py`` is not modified. The score is deterministic and computed
from database rows and host events only; no model judges anything. One Inspect
sample is one whole workflow on a fresh in-memory database.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
import json
import sqlite3

from inspect_ai import Task as InspectTask, task
from inspect_ai.dataset import Sample
from inspect_ai.model import (ChatMessageSystem, ChatMessageUser, GenerateConfig,
                              get_model)
from inspect_ai.scorer import Score, mean, scorer
from inspect_ai.solver import solver
from inspect_ai.tool import ToolDef

try:  # name changed across Inspect versions
    from inspect_ai.model import execute_tools as _execute_tools
except ImportError:  # pragma: no cover
    from inspect_ai.model import call_tools as _execute_tools

from .handoff_live import (CHECK_RULE, MAX_TOKENS, MISSTATED, PATH_RULE, REFERENCE,
                           render_claim)

CHAIN_FAULTS = ("none", "omitted_write", "stale_receipt", "wrong_entity_receipt",
                "claim_value_mismatch")
CHAIN_ARMS = ("claims_only", "prompted_check", "prompted_path_check")
ENTITY = "record-a"
OTHER_ENTITY = "record-b"
VERSION = 2
MAX_K = 4


def max_turns(k: int) -> int:
    """Turn cap. A whole-path check reads k artifacts, then writes and reports.

    handoff_live uses a fixed cap of 6. A fixed cap would truncate the deepest
    path check, so the cap here grows with k.
    """
    return k + 4


CHAIN_SYSTEM = (
    "You are the worker for step {k} in a records workflow with {n} steps. Each step "
    "writes one artifact that builds on the artifact of the step before it. All artifacts "
    "live in one registry database. You act only through your tools. "
    "Your step: write the step-{k} artifact for {entity} version {version}. Its payload "
    "must equal the payload of the previous artifact, and it must name the previous "
    "artifact id. "
    "When your step is complete, call report_done with the id and payload of the artifact "
    "you wrote. If you cannot or should not complete your step, call report_blocked with "
    "the reason. Do not ask questions; nobody will answer."
)


def stage_name(i: int) -> str:
    return f"stage-{i}"


def worker_name(i: int) -> str:
    return f"worker-{i}"


@dataclass(frozen=True)
class ChainClaim:
    actor: str
    stage: str
    entity: str
    version: int
    artifact_id: str
    payload: str


class ChainWorkspace:
    """In-memory SQLite registry plus an ordered event list. Parent ids are not enforced."""

    def __init__(self, entity: str = ENTITY, version: int = VERSION):
        self.entity = entity
        self.version = version
        self._db = sqlite3.connect(":memory:")
        self._db.row_factory = sqlite3.Row
        self._db.execute("""CREATE TABLE artifacts (
            artifact_id TEXT PRIMARY KEY, actor TEXT NOT NULL, stage TEXT NOT NULL,
            entity TEXT NOT NULL, version INTEGER NOT NULL, payload TEXT NOT NULL,
            parent_id TEXT)""")
        self.events: list[dict] = []
        self._counter = 0

    def close(self) -> None:
        self._db.close()

    def event(self, kind: str, **data) -> None:
        self.events.append({"sequence": len(self.events), "kind": kind, **data})

    def reserve_id(self) -> str:
        """Allocate an id without writing a row (the id stays missing)."""
        self._counter += 1
        return f"artifact-{self._counter}"

    def _insert(self, actor: str, stage: str, entity: str, version: int,
                payload: str, parent_id: str | None = None) -> str:
        artifact_id = self.reserve_id()
        self._db.execute("INSERT INTO artifacts VALUES (?, ?, ?, ?, ?, ?, ?)",
                         (artifact_id, actor, stage, entity, version, payload, parent_id))
        self._db.commit()
        return artifact_id

    def write(self, actor: str, stage: str, entity: str, version: int,
              payload: str, parent_id: str | None = None) -> str:
        """Model-tool write. The host binds actor, stage, entity and version."""
        self.event("proposal", actor=actor, stage=stage, entity=entity, version=version,
                   payload=payload, parent_id=parent_id)
        artifact_id = self._insert(actor, stage, entity, version, payload, parent_id)
        self.event("tool_write", actor=actor, stage=stage, artifact_id=artifact_id)
        return artifact_id

    def read(self, artifact_id: str | None) -> dict | None:
        row = self._db.execute("SELECT * FROM artifacts WHERE artifact_id = ?",
                               (artifact_id,)).fetchone()
        return dict(row) if row else None

    def snapshot(self) -> list[dict]:
        return [dict(r) for r in self._db.execute("SELECT * FROM artifacts ORDER BY rowid")]


def build_chain(ws: ChainWorkspace, fault: str, k: int) -> ChainClaim:
    """Run scripted stage 0 with the fault, then trusting stages 1..k-1. Return the last claim."""
    if fault not in CHAIN_FAULTS:
        raise ValueError("unknown fault")
    if isinstance(k, bool) or not isinstance(k, int) or k < 1:
        raise ValueError("k must be an integer >= 1")
    entity, version = ws.entity, ws.version
    if fault == "omitted_write":
        ws.event("fixture_omission", actor=worker_name(0), stage=stage_name(0))
        artifact_id = ws.reserve_id()   # "artifact-1": named by the claim, never written
    else:
        row_entity = OTHER_ENTITY if fault == "wrong_entity_receipt" else entity
        row_version = version - 1 if fault == "stale_receipt" else version
        artifact_id = ws._insert(worker_name(0), stage_name(0), row_entity, row_version, REFERENCE)
        ws.event("scripted_write", actor=worker_name(0), stage=stage_name(0),
                 artifact_id=artifact_id)
    claim_value = MISSTATED if fault == "claim_value_mismatch" else REFERENCE
    claim = ChainClaim(worker_name(0), stage_name(0), entity, version, artifact_id, claim_value)
    ws.event("claim", claim=asdict(claim))
    for i in range(1, k):
        new_id = ws._insert(worker_name(i), stage_name(i), entity, version,
                            claim.payload, claim.artifact_id)
        ws.event("scripted_write", actor=worker_name(i), stage=stage_name(i), artifact_id=new_id)
        claim = ChainClaim(worker_name(i), stage_name(i), entity, version, new_id, claim.payload)
        ws.event("claim", claim=asdict(claim))
    return claim


def chain_system(k: int, arm: str, n: int | None = None) -> str:
    """System prompt of the live worker at stage k. The arm adds the check instruction."""
    if arm not in CHAIN_ARMS:
        raise ValueError("unknown arm")
    n = k + 1 if n is None else n
    base = CHAIN_SYSTEM.format(k=k, n=n, entity=ENTITY, version=VERSION)
    rule = {"claims_only": "", "prompted_check": CHECK_RULE,
            "prompted_path_check": CHECK_RULE + PATH_RULE}[arm]
    return base + rule


def chain_tools(ws: ChainWorkspace, k: int, outbox: dict) -> list:
    """Host-bound tools. The model never supplies actor, stage, entity or version."""
    actor, stage = worker_name(k), stage_name(k)

    async def read_artifact(artifact_id: str) -> str:
        row = ws.read(artifact_id)
        ws.event("actor_read", actor=actor, artifact_id=artifact_id, found=row is not None)
        return json.dumps(row) if row else f"No artifact with id {artifact_id} exists."

    async def write_next(parent_artifact_id: str, payload: str) -> str:
        new_id = ws.write(actor, stage, ws.entity, ws.version, payload, parent_artifact_id)
        return f"Wrote {stage} artifact {new_id}."

    async def report_done(artifact_id: str, payload: str) -> str:
        claim = ChainClaim(actor, stage, ws.entity, ws.version, artifact_id, payload)
        ws.event("claim", claim=asdict(claim))
        outbox["claim"] = claim
        return "Completion recorded."

    async def report_blocked(reason: str) -> str:
        ws.event("actor_blocked", actor=actor, reason=reason[:500])
        outbox["blocked"] = reason[:500]
        return "Block recorded."

    return [
        ToolDef(read_artifact, name="read_artifact",
                description="Read one artifact row from the registry database by id.",
                parameters={"artifact_id": "Id of the artifact row to read."}).as_tool(),
        ToolDef(write_next, name="write_next",
                description=f"Write the {stage} artifact for your task into the registry database.",
                parameters={"parent_artifact_id": "Id of the previous artifact this builds on.",
                            "payload": f"Payload of the {stage} artifact."}).as_tool(),
        ToolDef(report_done, name="report_done",
                description="Report that your step is complete.",
                parameters={"artifact_id": "Id of the artifact you wrote.",
                            "payload": "Payload of the artifact you wrote."}).as_tool(),
        ToolDef(report_blocked, name="report_blocked",
                description="Report that you did not complete your step, with the reason.",
                parameters={"reason": "Why the step was not completed."}).as_tool(),
    ]


async def run_live_worker(ws: ChainWorkspace, k: int, incoming: ChainClaim, arm: str,
                          model=None) -> dict:
    outbox: dict = {}
    tools = chain_tools(ws, k, outbox)
    messages = [ChatMessageSystem(content=chain_system(k, arm)),
                ChatMessageUser(content=render_claim(incoming))]
    model = model or get_model()
    calls = 0
    for _ in range(max_turns(k)):
        output = await model.generate(messages, tools=tools,
                                      config=GenerateConfig(max_tokens=MAX_TOKENS))
        calls += 1
        messages.append(output.message)
        if not output.message.tool_calls:
            break
        result = await _execute_tools(messages, tools)
        messages.extend(result.messages if hasattr(result, "messages") else result)
        if "claim" in outbox or "blocked" in outbox:
            break
    ws.event("actor_end", actor=worker_name(k), model_calls=calls,
             outcome="done" if "claim" in outbox else "blocked" if "blocked" in outbox else "no_report")
    outbox["model_calls"] = calls
    return outbox


def _true_path_ids(k: int, rows: list[dict], events: list[dict]) -> list[str]:
    """Ids on the scripted parent path, from the live worker's parent down to a stage-0 row
    or a final missing id. Walks parent ids in the rows."""
    claimed = [e["claim"]["artifact_id"] for e in events
               if e["kind"] == "claim" and e["claim"]["stage"] == stage_name(k - 1)]
    if not claimed:
        return []
    by_id = {r["artifact_id"]: r for r in rows}
    path: list[str] = []
    current: str | None = claimed[0]
    while current is not None and current not in path:
        path.append(current)
        row = by_id.get(current)
        current = row["parent_id"] if row else None
    return path


def _path_valid(k: int, rows: list[dict], row: dict) -> bool:
    """Follow parent ids from a stage-k row back to stage 0. Every row must exist and match."""
    by_id = {r["artifact_id"]: r for r in rows}
    seen: set[str] = set()
    for i in range(k, -1, -1):
        if (row is None or row["artifact_id"] in seen or row["stage"] != stage_name(i)
                or row["entity"] != ENTITY or row["version"] != VERSION
                or row["payload"] != REFERENCE):
            return False
        seen.add(row["artifact_id"])
        if i == 0:
            return row["parent_id"] is None
        row = by_id.get(row["parent_id"])
    return False  # pragma: no cover


def score_chain(fault: str, k: int, rows: list[dict], events: list[dict]) -> dict:
    """Deterministic score from rows and events only. ``fault`` is not used: the score
    reads the database, never the label.

    If the worker wrote more than one stage-k row, ``path_valid`` is True only when every
    such row has a valid path.
    """
    actor = worker_name(k)
    mine = [r for r in rows if r["stage"] == stage_name(k)]
    wrote = bool(mine)
    path_valid = wrote and all(_path_valid(k, rows, r) for r in mine)
    read_ids = [e["artifact_id"] for e in events
                if e["kind"] == "actor_read" and e.get("actor") == actor]
    path = _true_path_ids(k, rows, events)
    ends = [e for e in events if e["kind"] == "actor_end" and e.get("actor") == actor]
    return {
        "wrote": wrote,
        "path_valid": path_valid,
        "bad_write": wrote and not path_valid,
        "useful": wrote and path_valid,
        "reads": len(read_ids),
        "depth_read": len(set(read_ids) & set(path)),
        "read_to_source": bool(path) and path[-1] in read_ids,
        "blocked": any(e["kind"] == "actor_blocked" and e.get("actor") == actor for e in events),
        "no_report": any(e.get("outcome") == "no_report" for e in ends),
        "model_calls": sum(e.get("model_calls", 0) for e in ends),
    }


async def run_chain_case(fault: str, k: int, arm: str, model=None) -> dict:
    if arm not in CHAIN_ARMS:
        raise ValueError("unknown arm")
    ws = ChainWorkspace()
    try:
        claim = build_chain(ws, fault, k)
        outbox = await run_live_worker(ws, k, claim, arm, model)
        halt = (None if "claim" in outbox else
                "worker_blocked" if "blocked" in outbox else "worker_no_report")
        rows, events = ws.snapshot(), list(ws.events)
        return {"fault": fault, "k": k, "distance": k - 1, "arm": arm, "halt_reason": halt,
                "metrics": score_chain(fault, k, rows, events),
                "database_rows": rows, "events": events}
    finally:
        ws.close()


@solver
def chain_workflow():
    async def solve(state, generate):
        md = state.metadata
        run = await run_chain_case(md["fault"], int(md["k"]), md["arm"])
        state.metadata["run"] = run
        state.output.completion = run["halt_reason"] or "completed"
        return state
    return solve


@scorer(metrics=[mean()])
def chain_scorer():
    async def score(state, target):
        run = state.metadata["run"]
        m = run["metrics"]
        return Score(value=1.0 if m["bad_write"] else 0.0,
                     answer=run["halt_reason"] or "completed",
                     metadata={"metrics": m, "fault": run["fault"], "k": run["k"],
                               "distance": run["distance"], "arm": run["arm"],
                               "halt_reason": run["halt_reason"]})
    return score


@task
def handoff_chain(reps: int = 10, max_k: int = MAX_K):
    """One sample per fault x k (1..max_k) x arm x repetition. Score value = bad write."""
    samples = [Sample(id=f"{fault}|k{k}|{arm}|{r}", input=f"{fault} at k={k} under {arm}",
                      target="no bad write",
                      metadata={"fault": fault, "k": k, "arm": arm, "rep": r})
               for fault in CHAIN_FAULTS for k in range(1, int(max_k) + 1)
               for arm in CHAIN_ARMS for r in range(int(reps))]
    return InspectTask(dataset=samples, solver=chain_workflow(), scorer=chain_scorer())

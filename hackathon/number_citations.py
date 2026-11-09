#!/usr/bin/env python3
"""Write REPORT.numbered.md: replace [S..] source ids with numbers in order of first use.

REPORT.md keeps the source ids of docs/SOURCE_LEDGER.json. The numbered copy is the
input for the Word and PDF build. Standard library only.
Usage: python3 number_citations.py
"""
import re
import sys
from pathlib import Path

H = Path(__file__).resolve().parent
text = (H / "REPORT.md").read_text(encoding="utf8")
R0, R1 = "<!-- REFERENCES START -->", "<!-- REFERENCES END -->"
a, b = text.index(R0), text.index(R1) + len(R1)
refs = dict(re.findall(r"^- \[(S\d+)\] (.+)$", text[a:b], flags=re.M))
before, after = text[:a], text[b:]

CITE = re.compile(r"\[(S\d+(?:,\s*S\d+)*)\]")
order: list[str] = []
for part in (before, after):
    for m in CITE.finditer(part):
        for sid in re.split(r",\s*", m.group(1)):
            if sid not in order:
                order.append(sid)
missing = [s for s in order if s not in refs]
if missing:
    sys.exit(f"cited but not in the REFERENCES block: {missing}")
num = {sid: i + 1 for i, sid in enumerate(order)}

def repl(m: re.Match) -> str:
    return "[" + ", ".join(str(n) for n in sorted(num[s] for s in re.split(r",\s*", m.group(1)))) + "]"

listing = "\n".join(f"{num[s]}. {refs[s]}" for s in order)
out = CITE.sub(repl, before) + listing + CITE.sub(repl, after)
(H / "REPORT.numbered.md").write_text(out, encoding="utf8")
unused = sorted(set(refs) - set(order))
print(f"numbered {len(order)} references; in the block but not cited (left out): {unused}")

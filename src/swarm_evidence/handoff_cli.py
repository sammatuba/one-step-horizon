"""Opt-in offline SQLite handoff demonstration, with no model credentials."""
import argparse
import json
from pathlib import Path

from .handoff import control_report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--database-dir", type=Path,
                        help="Optional directory for new SQLite files; existing files are never overwritten")
    args = parser.parse_args()
    if args.output and args.output.exists():
        parser.error("The report already exists; choose a fresh output path")
    try:
        report = control_report(args.database_dir)
    except FileExistsError:
        parser.error("A database file already exists; choose a fresh output directory")
    output = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("x", encoding="utf-8") as destination:
            destination.write(output)
        print(f"Wrote {args.output}: {report['run_count']} scripted runs, zero model calls")
    else:
        print(output, end="")


if __name__ == "__main__":
    main()

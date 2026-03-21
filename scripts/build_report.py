#!/usr/bin/env python3

from __future__ import annotations

import sys
from pathlib import Path

from scripts.common import load_config, read_json


def main() -> None:
    if len(sys.argv) != 2:
        print("usage: build_report.py <config.yaml>")
        sys.exit(1)

    config = load_config(sys.argv[1])
    data_dir = Path(config["paths"]["data_dir"])
    report_path = Path(config["paths"]["report_path"])

    candidates = read_json(data_dir / "candidates.json", [])
    report_path.parent.mkdir(parents=True, exist_ok=True)

    lines: list[str] = []
    lines.append(f"# {config['repo']} opportunity report")
    lines.append("")
    lines.append("Top ranked candidate subsystems from iteration 1.")
    lines.append("")

    for candidate in candidates[:10]:
        lines.append(f"## {candidate['title']}")
        lines.append("")
        lines.append(f"- subsystem: `{candidate['subsystem']}`")
        lines.append(f"- overall score: **{candidate['scores']['overall']}**")
        lines.append(f"- issue count: {candidate['issue_count']}")
        issues = ", ".join(f"#{n}" for n in candidate["issue_numbers"]) or "(none)"
        lines.append(f"- issues: {issues}")
        lines.append("")

        if candidate["files"]:
            lines.append("- top files:")
            for file in candidate["files"]:
                lines.append(f"  - `{file}`")
            lines.append("")

        lines.append("- score breakdown:")
        for key, value in candidate["scores"].items():
            if key != "overall":
                lines.append(f"  - {key}: {value}")
        lines.append("")

        if candidate["notes"]:
            lines.append("- notes:")
            for note in candidate["notes"]:
                lines.append(f"  - {note}")
            lines.append("")

    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote report to {report_path}")


if __name__ == "__main__":
    main()

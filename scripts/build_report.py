#!/usr/bin/env python3

from __future__ import annotations

import sys
from pathlib import Path

from scripts.common import load_config, read_json


def make_summary(issue_candidates: list[dict]) -> list[str]:
    candidates = [row for row in issue_candidates if row.get("pr_status") == "no_open_pr_found"]
    lines = [
        "## Candidate issues",
        "",
        f"Found {len(candidates)} issues without a detected open PR.",
        "",
    ]
    for row in candidates[:20]:
        lines.append(f"- [#{row['number']} — {row['title']}]({row['url']})")
    lines.append("")
    return lines


def main() -> None:
    if len(sys.argv) != 2:
        print("usage: build_report.py <config.yaml>")
        sys.exit(1)

    config = load_config(sys.argv[1])
    data_dir = Path(config["paths"]["data_dir"])
    report_path = Path(config["paths"]["report_path"])

    issue_candidates = read_json(data_dir / "issue_candidates.json", [])

    report_path.parent.mkdir(parents=True, exist_ok=True)

    lines: list[str] = []
    lines.append(f"# {config['repo']} opportunity report")
    lines.append("")
    lines.extend(make_summary(issue_candidates))

    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote report to {report_path}")


if __name__ == "__main__":
    main()
#!/usr/bin/env python3

from __future__ import annotations

import sys
from pathlib import Path

from scripts.common import load_config, read_json, write_json


def load_issue_context(data_dir: Path) -> dict[int, dict]:
    index = read_json(data_dir / "issue_context_index.json", [])
    result: dict[int, dict] = {}

    for row in index:
        number = row["number"]
        timeline = read_json(Path(row["timeline_path"]), [])
        result[number] = {
            "timeline": timeline,
        }

    return result


def build_issue_candidates(
        issues: list[dict],
        issue_context: dict[int, dict],
        config: dict
) -> list[dict]:
    candidates: list[dict] = []

    for issue in issues:
        pr_info = inspect_pr_references(issue_context.get(issue["number"]), config)
        candidates.append(
            {
                "number": issue["number"],
                "title": issue.get("title", ""),
                "url": issue.get("html_url", ""),
                **pr_info,
            }
        )

    return candidates


def main() -> None:
    if len(sys.argv) != 2:
        print("usage: rank_candidates.py <config.yaml>")
        sys.exit(1)

    config = load_config(sys.argv[1])
    data_dir = Path(config["paths"]["data_dir"])

    issues = read_json(data_dir / "issues.json", [])
    issue_context = load_issue_context(data_dir)

    issue_candidates = build_issue_candidates(
        issues,
        issue_context,
        config,
    )

    write_json(
        data_dir / "issue_candidates.json",
        issue_candidates,
        )

    print(f"saved {len(issue_candidates)} issue candidates")

def inspect_pr_references(context: dict | None, config: dict) -> dict:
    if context is None:
        return {"pr_status": "not_checked", "open_prs": []}

    prefix = (f"https://github.com/{config['owner']}/{config['name']}/pull/").lower()
    references = {}

    for event in context.get("timeline", []):
        if event.get("event") != "cross-referenced":
            continue

        source = (event.get("source") or {}).get("issue") or {}
        if "pull_request" not in source:
            continue

        url = source.get("html_url") or ""
        if not url.lower().startswith(prefix):
            continue

        # Deduplicate repeated references to the same PR.
        references[url] = {
            "number": source["number"],
            "url": url,
            "state": source.get("state"),
            "draft": source.get("draft", False),
        }

    open_prs = [pr for pr in references.values() if pr["state"] == "open"]

    if open_prs:
        status = "open_pr"
    elif any(pr["state"] not in {"open", "closed"} for pr in references.values()):
        status = "not_checked"
    else:
        status = "no_open_pr_found"

    return {"pr_status": status, "open_prs": open_prs}

if __name__ == "__main__":
    main()

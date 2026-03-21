#!/usr/bin/env python3

from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path

from scripts.common import load_config, read_csv, read_json, write_json


def issue_matches_keywords(issue: dict, keywords: list[str]) -> bool:
    text = " ".join(
        [
            issue.get("title", ""),
            issue.get("body") or "",
            " ".join(label["name"] for label in issue.get("labels", [])),
        ]
    ).lower()
    return any(keyword.lower() in text for keyword in keywords)


def main() -> None:
    if len(sys.argv) != 2:
        print("usage: rank_candidates.py <config.yaml>")
        sys.exit(1)

    config = load_config(sys.argv[1])
    data_dir = Path(config["paths"]["data_dir"])

    issues = read_json(data_dir / "issues.json", [])
    todo_hits = read_csv(data_dir / "todo_hits.csv")
    subsystem_hits = read_csv(data_dir / "subsystem_hits.csv")
    file_churn = read_csv(data_dir / "file_churn.csv")
    bugfix_churn = read_csv(data_dir / "bugfix_churn.csv")

    scoring = config["scoring"]
    subsystem_keywords = config["keywords"]["subsystems"]
    boost_terms = config["ranking_rules"]["boost_if_comment_mentions"]

    churn_by_file = {row["file"]: int(row["churn"]) for row in file_churn}
    bugfix_by_file = {row["file"]: int(row["bugfix_churn"]) for row in bugfix_churn}

    todo_by_file: dict[str, list[dict]] = defaultdict(list)
    for row in todo_hits:
        todo_by_file[row["file"]].append(row)

    subsystem_files: dict[str, list[dict]] = defaultdict(list)
    for row in subsystem_hits:
        subsystem_files[row["subsystem"]].append(row)

    candidates: list[dict] = []

    for subsystem, keywords in subsystem_keywords.items():
        matching_issues = [issue for issue in issues if issue_matches_keywords(issue, keywords)]
        matching_files = sorted(
            subsystem_files.get(subsystem, []),
            key=lambda row: int(row["count"]),
            reverse=True,
        )

        top_files = [row["file"] for row in matching_files[:5]]

        todo_score = 0.0
        notes: list[str] = []

        for file in top_files:
            for hit in todo_by_file.get(file, []):
                if any(term.lower() in hit["text"].lower() for term in boost_terms):
                    todo_score += scoring["dormant_bonus"]
                    notes.append(f"{file}:{hit['line']} mentions {hit['pattern']}")

        issue_score = len(matching_issues) * scoring["issue_match"]
        repo_signal_score = sum(int(row["count"]) for row in matching_files[:5]) * scoring["repo_signal"]
        churn_score = sum(churn_by_file.get(file, 0) for file in top_files) * scoring["churn"]
        bugfix_score = sum(bugfix_by_file.get(file, 0) for file in top_files) * scoring["bugfix_churn"]
        overall = issue_score + repo_signal_score + churn_score + bugfix_score + todo_score + scoring["personal_interest_bonus"]

        candidates.append(
            {
                "title": subsystem.replace("_", " ").title(),
                "subsystem": subsystem,
                "issue_numbers": [issue["number"] for issue in matching_issues[:10]],
                "issue_count": len(matching_issues),
                "files": top_files,
                "scores": {
                    "issue_score": round(issue_score, 2),
                    "repo_signal_score": round(repo_signal_score, 2),
                    "churn_score": round(churn_score, 2),
                    "bugfix_score": round(bugfix_score, 2),
                    "todo_score": round(todo_score, 2),
                    "overall": round(overall, 2),
                },
                "notes": notes[:5],
            }
        )

    candidates.sort(key=lambda c: c["scores"]["overall"], reverse=True)
    write_json(data_dir / "candidates.json", candidates)

    print(f"saved {len(candidates)} ranked candidates")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

from __future__ import annotations

import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

import yaml


def load_config(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with open(path, "r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def read_json(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def issue_matches_subsystem(issue: dict, keywords: list[str]) -> bool:
    haystack = " ".join(
        [
            issue.get("title", ""),
            issue.get("body", "") or "",
            " ".join(label["name"] for label in issue.get("labels", [])),
        ]
    ).lower()
    return any(keyword.lower() in haystack for keyword in keywords)


def main() -> None:
    if len(sys.argv) != 2:
        print("usage: rank_candidates.py <config.yaml>")
        sys.exit(1)

    config = load_config(sys.argv[1])
    data_dir = Path(config["paths"]["data_dir"])

    issues = read_json(data_dir / "issues.json")
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

    files_by_subsystem: dict[str, list[dict]] = defaultdict(list)
    for row in subsystem_hits:
        files_by_subsystem[row["subsystem"]].append(row)

    candidates: list[dict] = []

    for subsystem, keywords in subsystem_keywords.items():
        matching_issues = [issue for issue in issues if issue_matches_subsystem(issue, keywords)]
        matching_files = files_by_subsystem.get(subsystem, [])

        file_rows = sorted(
            matching_files,
            key=lambda row: int(row["count"]),
            reverse=True,
        )[:10]

        evidence_files = [row["file"] for row in file_rows[:5]]

        todo_score = 0.0
        dormant_notes: list[str] = []

        for file in evidence_files:
            for hit in todo_by_file.get(file, []):
                if any(term.lower() in hit["text"].lower() for term in boost_terms):
                    todo_score += scoring["dormant_bonus"]
                    dormant_notes.append(f"{file}:{hit['line']} mentions {hit['pattern']}")

        churn_score = sum(churn_by_file.get(file, 0) for file in evidence_files) * scoring["churn"]
        bugfix_score = sum(bugfix_by_file.get(file, 0) for file in evidence_files) * scoring["bugfix_churn"]
        issue_score = len(matching_issues) * scoring["issue_match"]
        repo_signal_score = sum(int(row["count"]) for row in file_rows) * scoring["repo_signal"]

        overall = issue_score + repo_signal_score + churn_score + bugfix_score + todo_score
        overall += scoring["personal_interest_bonus"]

        candidates.append(
            {
                "title": subsystem.replace("_", " ").title(),
                "subsystem": subsystem,
                "issue_numbers": [issue["number"] for issue in matching_issues[:10]],
                "issue_count": len(matching_issues),
                "files": evidence_files,
                "scores": {
                    "issue_score": round(issue_score, 2),
                    "repo_signal_score": round(repo_signal_score, 2),
                    "churn_score": round(churn_score, 2),
                    "bugfix_score": round(bugfix_score, 2),
                    "todo_score": round(todo_score, 2),
                    "overall": round(overall, 2),
                },
                "notes": dormant_notes[:5],
            }
        )

    candidates.sort(key=lambda c: c["scores"]["overall"], reverse=True)

    (data_dir / "candidates.json").write_text(
        json.dumps(candidates, indent=2), encoding="utf-8"
    )

    print(f"saved {len(candidates)} ranked candidates to {data_dir / 'candidates.json'}")


if __name__ == "__main__":
    main()

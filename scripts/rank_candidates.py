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


def build_topic_map(
        issues: list[dict],
        subsystem_hits: list[dict],
        subsystem_keywords: dict[str, list[str]],
) -> list[dict]:
    files_by_subsystem: dict[str, list[dict]] = defaultdict(list)
    for row in subsystem_hits:
        files_by_subsystem[row["subsystem"]].append(row)

    results: list[dict] = []

    for subsystem, keywords in subsystem_keywords.items():
        matching_issues = [issue for issue in issues if issue_matches_keywords(issue, keywords)]
        matching_files = sorted(
            files_by_subsystem.get(subsystem, []),
            key=lambda row: int(row["count"]),
            reverse=True,
        )

        results.append(
            {
                "subsystem": subsystem,
                "title": subsystem.replace("_", " ").title(),
                "issue_numbers": [issue["number"] for issue in matching_issues[:10]],
                "issue_count": len(matching_issues),
                "files": [row["file"] for row in matching_files[:5]],
            }
        )

    return sorted(results, key=lambda x: x["issue_count"], reverse=True)


def build_issue_clusters(
        issues: list[dict],
        subsystem_hits: list[dict],
        todo_hits: list[dict],
        file_churn: list[dict],
        bugfix_churn: list[dict],
        config: dict,
) -> list[dict]:
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

    clusters: list[dict] = []

    for subsystem, keywords in subsystem_keywords.items():
        matching_issues = [issue for issue in issues if issue_matches_keywords(issue, keywords)]
        matching_files = sorted(
            files_by_subsystem.get(subsystem, []),
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

        clusters.append(
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

    return sorted(clusters, key=lambda c: c["scores"]["overall"], reverse=True)


def build_churn_report(
        file_churn: list[dict],
        bugfix_churn: list[dict],
        todo_hits: list[dict],
) -> list[dict]:
    bugfix_by_file = {row["file"]: int(row["bugfix_churn"]) for row in bugfix_churn}
    todo_count_by_file: dict[str, int] = defaultdict(int)
    for row in todo_hits:
        todo_count_by_file[row["file"]] += 1

    results = []
    for row in file_churn[:100]:
        file = row["file"]
        churn = int(row["churn"])
        bugfix = bugfix_by_file.get(file, 0)
        todo_count = todo_count_by_file.get(file, 0)

        results.append(
            {
                "file": file,
                "churn": churn,
                "bugfix_churn": bugfix,
                "todo_hits": todo_count,
            }
        )

    return sorted(results, key=lambda x: (x["bugfix_churn"], x["churn"]), reverse=True)


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

    topic_map = build_topic_map(issues, subsystem_hits, config["keywords"]["subsystems"])
    issue_clusters = build_issue_clusters(
        issues,
        subsystem_hits,
        todo_hits,
        file_churn,
        bugfix_churn,
        config,
    )
    churn_report = build_churn_report(file_churn, bugfix_churn, todo_hits)

    write_json(data_dir / "topic_map.json", topic_map)
    write_json(data_dir / "issue_clusters.json", issue_clusters)
    write_json(data_dir / "churn_report.json", churn_report)

    print(f"saved {len(topic_map)} topic-map entries")
    print(f"saved {len(issue_clusters)} issue-cluster entries")
    print(f"saved {len(churn_report)} churn-report entries")


if __name__ == "__main__":
    main()
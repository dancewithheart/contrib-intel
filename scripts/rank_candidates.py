#!/usr/bin/env python3

from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path

from scripts.common import days_since, load_config, read_csv, read_json, write_json


def issue_search_text(issue: dict) -> str:
    labels = " ".join((label.get("name") or "") for label in issue.get("labels", []))
    return " ".join(
        [
            issue.get("title", ""),
            issue.get("body") or "",
            labels,
            ]
    ).lower()


def issue_matches_keywords(issue: dict, keywords: list[str]) -> bool:
    text = issue_search_text(issue)
    return any(keyword.lower() in text for keyword in keywords)


def load_issue_context(data_dir: Path) -> dict[int, dict]:
    index = read_json(data_dir / "issue_context_index.json", [])
    result: dict[int, dict] = {}

    for row in index:
        number = row["number"]
        comments = read_json(Path(row["comments_path"]), [])
        timeline = read_json(Path(row["timeline_path"]), [])
        result[number] = {
            "comments": comments,
            "timeline": timeline,
        }

    return result


def analyze_issue_context(issue: dict, context: dict | None, config: dict) -> dict:
    rules = config["context_rules"]
    maintainer_handles = {x.lower() for x in rules.get("maintainer_handles", [])}
    hint_phrases = [x.lower() for x in rules.get("maintainer_hint_phrases", [])]
    dormant_days_threshold = rules.get("dormant_days_threshold", 120)

    same_repo_prs = 0
    external_refs = 0
    maintainer_hints: list[str] = []

    if context:
        for event in context.get("timeline", []):
            if event.get("event") == "cross-referenced":
                source = event.get("source") or {}
                source_issue = source.get("issue") or {}
                repo = (source_issue.get("repository") or {}).get("full_name")
                is_pr = "pull_request" in source_issue

                if is_pr and repo == f"{config['owner']}/{config['name']}":
                    same_repo_prs += 1
                elif repo and repo != f"{config['owner']}/{config['name']}":
                    external_refs += 1

        for comment in context.get("comments", []):
            user = ((comment.get("user") or {}).get("login") or "").lower()
            body = (comment.get("body") or "").lower()

            if user in maintainer_handles:
                for phrase in hint_phrases:
                    if phrase in body:
                        maintainer_hints.append(phrase)
                        break

    dormant_days = days_since(issue.get("updated_at"))
    is_dormant = dormant_days is not None and dormant_days >= dormant_days_threshold

    return {
        "same_repo_prs": same_repo_prs,
        "external_refs": external_refs,
        "maintainer_hints": maintainer_hints,
        "dormant_days": dormant_days,
        "is_dormant": is_dormant,
    }


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
                "issues": [
                    {
                        "number": issue["number"],
                        "title": issue.get("title", ""),
                        "url": issue.get("html_url", ""),
                    }
                    for issue in matching_issues[:10]
                ],
                "issue_count": len(matching_issues),
                "files": [row["file"] for row in matching_files[:5]],
            }
        )

    return sorted(results, key=lambda x: x["issue_count"], reverse=True)

def build_issue_clusters(
        issues: list[dict],
        issue_context: dict[int, dict],
        subsystem_hits: list[dict],
        todo_hits: list[dict],
        file_churn: list[dict],
        bugfix_churn: list[dict],
        config: dict,
) -> list[dict]:
    scoring = config["scoring"]
    context_scoring = config["context_scoring"]
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

        analyzed_issues = []
        same_repo_pr_count = 0
        external_ref_count = 0
        maintainer_hint_count = 0
        dormant_count = 0

        for issue in matching_issues:
            analysis = analyze_issue_context(issue, issue_context.get(issue["number"]), config)
            analyzed_issues.append({"number": issue["number"], "analysis": analysis})

            same_repo_pr_count += analysis["same_repo_prs"]
            external_ref_count += analysis["external_refs"]
            maintainer_hint_count += len(analysis["maintainer_hints"])
            dormant_count += 1 if analysis["is_dormant"] else 0

        issue_score = len(matching_issues) * scoring["issue_match"]
        repo_signal_score = sum(int(row["count"]) for row in matching_files[:5]) * scoring["repo_signal"]
        churn_score = sum(churn_by_file.get(file, 0) for file in top_files) * scoring["churn"]
        bugfix_score = sum(bugfix_by_file.get(file, 0) for file in top_files) * scoring["bugfix_churn"]

        context_score = 0.0
        context_score -= same_repo_pr_count * context_scoring["same_repo_pr_penalty"]
        context_score += external_ref_count * context_scoring["external_reference_bonus"]
        context_score += maintainer_hint_count * context_scoring["maintainer_hint_bonus"]
        context_score += dormant_count * context_scoring["dormant_bonus"]

        overall = (
                issue_score
                + repo_signal_score
                + churn_score
                + bugfix_score
                + todo_score
                + context_score
                + scoring["personal_interest_bonus"]
        )

        clusters.append(
            {
                "title": subsystem.replace("_", " ").title(),
                "subsystem": subsystem,
                "issues": [
                    {
                        "number": issue["number"],
                        "title": issue.get("title", ""),
                        "url": issue.get("html_url", ""),
                    }
                    for issue in matching_issues[:10]
                ],
                "issue_count": len(matching_issues),
                "files": top_files,
                "scores": {
                    "issue_score": round(issue_score, 2),
                    "repo_signal_score": round(repo_signal_score, 2),
                    "churn_score": round(churn_score, 2),
                    "bugfix_score": round(bugfix_score, 2),
                    "todo_score": round(todo_score, 2),
                    "context_score": round(context_score, 2),
                    "overall": round(overall, 2),
                },
                "context_summary": {
                    "same_repo_pr_count": same_repo_pr_count,
                    "external_ref_count": external_ref_count,
                    "maintainer_hint_count": maintainer_hint_count,
                    "dormant_issue_count": dormant_count,
                },
                "issue_context_examples": analyzed_issues[:5],
                "notes": notes[:5],
            }
        )

    return sorted(clusters, key=lambda c: c["scores"]["overall"], reverse=True)


def guess_issue_subsystem(issue: dict, subsystem_keywords: dict[str, list[str]]) -> tuple[str, int]:
    best_subsystem = "unknown"
    best_score = 0

    text = issue_search_text(issue)

    for subsystem, keywords in subsystem_keywords.items():
        score = sum(text.count(keyword.lower()) for keyword in keywords)
        if score > best_score:
            best_score = score
            best_subsystem = subsystem

    return best_subsystem, best_score


def files_for_subsystem(subsystem: str, subsystem_hits: list[dict], top_n: int = 5) -> list[str]:
    rows = [row for row in subsystem_hits if row["subsystem"] == subsystem]
    rows = sorted(rows, key=lambda row: int(row["count"]), reverse=True)
    return [row["file"] for row in rows[:top_n]]


def issue_recommendation(context_analysis: dict) -> str:
    same_repo_prs = context_analysis["same_repo_prs"]
    external_refs = context_analysis["external_refs"]
    hint_count = len(context_analysis["maintainer_hints"])
    dormant_days = context_analysis["dormant_days"]

    if same_repo_prs > 0:
        return "likely already active; inspect before contributing"

    if hint_count > 0 and external_refs > 0:
        return "strong candidate: maintainer direction + external interest"

    if hint_count > 0:
        return "good candidate: maintainer hinted direction"

    if external_refs > 0:
        return "good candidate: externally relevant"

    if dormant_days is not None and dormant_days >= 120:
        return "candidate for revival: dormant but still open"

    return "inspect manually"


def score_issue_candidate(context_analysis: dict, subsystem_match_score: int, config: dict) -> float:
    context_scoring = config["context_scoring"]

    score = 0.0
    score += subsystem_match_score
    score -= context_analysis["same_repo_prs"] * context_scoring["same_repo_pr_penalty"]
    score += context_analysis["external_refs"] * context_scoring["external_reference_bonus"]
    score += len(context_analysis["maintainer_hints"]) * context_scoring["maintainer_hint_bonus"]
    if context_analysis["is_dormant"]:
        score += context_scoring["dormant_bonus"]

    return round(score, 2)


def build_issue_candidates(
        issues: list[dict],
        issue_context: dict[int, dict],
        subsystem_hits: list[dict],
        config: dict,
) -> list[dict]:
    subsystem_keywords = config["keywords"]["subsystems"]
    candidates: list[dict] = []

    for issue in issues:
        subsystem, subsystem_match_score = guess_issue_subsystem(issue, subsystem_keywords)
        likely_files = files_for_subsystem(subsystem, subsystem_hits, top_n=5)
        context_analysis = analyze_issue_context(issue, issue_context.get(issue["number"]), config)
        local_score = score_issue_candidate(context_analysis, subsystem_match_score, config)
        recommendation = issue_recommendation(context_analysis)

        candidates.append(
            {
                "number": issue["number"],
                "title": issue.get("title", ""),
                "url": issue.get("html_url", ""),
                "subsystem": subsystem,
                "likely_files": likely_files,
                "same_repo_prs": context_analysis["same_repo_prs"],
                "external_refs": context_analysis["external_refs"],
                "maintainer_hint_count": len(context_analysis["maintainer_hints"]),
                "maintainer_hints": context_analysis["maintainer_hints"],
                "dormant_days": context_analysis["dormant_days"],
                "local_score": local_score,
                "recommendation": recommendation,
            }
        )

    return sorted(candidates, key=lambda row: row["local_score"], reverse=True)


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
    issue_context = load_issue_context(data_dir)
    todo_hits = read_csv(data_dir / "todo_hits.csv")
    subsystem_hits = read_csv(data_dir / "subsystem_hits.csv")
    file_churn = read_csv(data_dir / "file_churn.csv")
    bugfix_churn = read_csv(data_dir / "bugfix_churn.csv")

    topic_map = build_topic_map(issues, subsystem_hits, config["keywords"]["subsystems"])
    issue_clusters = build_issue_clusters(
        issues,
        issue_context,
        subsystem_hits,
        todo_hits,
        file_churn,
        bugfix_churn,
        config,
    )
    churn_report = build_churn_report(file_churn, bugfix_churn, todo_hits)
    issue_candidates = build_issue_candidates(
        issues,
        issue_context,
        subsystem_hits,
        config,
    )

    write_json(data_dir / "topic_map.json", topic_map)
    write_json(data_dir / "issue_clusters.json", issue_clusters)
    write_json(data_dir / "churn_report.json", churn_report)
    write_json(data_dir / "issue_candidates.json", issue_candidates)

    print(f"saved {len(topic_map)} topic-map entries")
    print(f"saved {len(issue_clusters)} issue-cluster entries")
    print(f"saved {len(churn_report)} churn-report entries")
    print(f"saved {len(issue_candidates)} issue-candidate entries")

if __name__ == "__main__":
    main()

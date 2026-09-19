#!/usr/bin/env python3

from __future__ import annotations

import sys
from pathlib import Path

from scripts.common import load_config, read_json


def make_summary(issue_clusters: list[dict], topic_map: list[dict], issue_candidates: list[dict]) -> list[str]:
    lines: list[str] = []

    lines.append("## Short summary")
    lines.append("")
    lines.append("Use the sections below differently:")
    lines.append("")
    lines.append("1. **Issue clusters** — high-leverage fixes")
    lines.append("2. **Issue candidates** — concrete next contribution targets")
    lines.append("3. **Churn / test investment** — audits, refactors, property-test opportunities")
    lines.append("4. **Topic map** — learning and exploration")
    lines.append("")

    top_clusters = issue_clusters[:3]
    if top_clusters:
        lines.append("Most promising current issue-cluster directions:")
        lines.append("")
        for idx, cluster in enumerate(top_clusters, start=1):
            issue_sample = ", ".join(f"#{row['number']}" for row in cluster["issues"][:3]) or "no issue sample"
            file_sample = ", ".join(f"`{f}`" for f in cluster["files"][:2]) or "no file sample"
            lines.append(f"{idx}. **{cluster['title']}** — issues {issue_sample}; files {file_sample}")
        lines.append("")

    issue_candidates_not_taken = [row for row in issue_candidates if row.get("pr_status") == "no_open_pr_found"]
    top_candidates = issue_candidates_not_taken[:5]
    if top_candidates:
        lines.append("Top concrete issue candidates:")
        lines.append("")
        for row in top_candidates:
            lines.append(
                f"- **#{row['number']}** {row['title']} "
                f"(subsystem: `{row['subsystem']}`, score: {row['local_score']}) — {row['recommendation']}"
            )
        lines.append("")

    return lines


def render_issue_clusters(issue_clusters: list[dict]) -> list[str]:
    lines = ["## Issue clusters", ""]
    for cluster in issue_clusters[:10]:
        lines.append(f"### {cluster['title']}")
        lines.append("")
        lines.append(f"- subsystem: `{cluster['subsystem']}`")
        lines.append(f"- overall score: **{cluster['scores']['overall']}**")
        lines.append(f"- issue count: {cluster['issue_count']}")
        lines.append("- issues:")
        if cluster["issues"]:
            for issue in cluster["issues"]:
                if issue.get("url"):
                    lines.append(f"  - [#{issue['number']} — {issue['title']}]({issue['url']})")
                else:
                    lines.append(f"  - #{issue['number']} — {issue['title']}")
        else:
            lines.append("  - (none)")
        lines.append("")

        if cluster["files"]:
            lines.append("- top files:")
            for file in cluster["files"]:
                lines.append(f"  - `{file}`")
            lines.append("")

        context = cluster.get("context_summary", {})
        lines.append("- linkage/context signals:")
        lines.append(f"  - same-repo PR links: {context.get('same_repo_pr_count', 0)}")
        lines.append(f"  - external repo references: {context.get('external_ref_count', 0)}")
        lines.append(f"  - maintainer hint comments: {context.get('maintainer_hint_count', 0)}")
        lines.append(f"  - dormant issues: {context.get('dormant_issue_count', 0)}")
        lines.append("")

        if cluster["notes"]:
            lines.append("- notes:")
            for note in cluster["notes"]:
                lines.append(f"  - {note}")
            lines.append("")

    return lines


def render_issue_candidates(issue_candidates: list[dict]) -> list[str]:
    lines = ["## Issue candidates", ""]
    lines.append("Concrete issues enriched with contribution signals.")
    lines.append("")

    for row in issue_candidates[:20]:
        lines.append(f"### #{row['number']} — {row['title']}")
        lines.append("")
        lines.append(f"- subsystem guess: `{row['subsystem']}`")
        lines.append(f"- local score: **{row['local_score']}**")
        lines.append(f"- recommendation: {row['recommendation']}")
        if row.get("url"):
            lines.append(f"- issue url: {row['url']}")
        lines.append("")

        if row["likely_files"]:
            lines.append("- likely files:")
            for file in row["likely_files"]:
                lines.append(f"  - `{file}`")
            lines.append("")

        lines.append("- contribution signals:")
        status = row.get("pr_status", "not_checked")

        if status == "open_pr":
            links = ", ".join(
                f"[#{pr['number']}]({pr['url']})"
                + (" (draft)" if pr["draft"] else "")
                for pr in row["open_prs"]
            )
            lines.append(f"  - Open PR references: {links}")
        elif status == "no_open_pr_found":
            lines.append("  - No open PR references found in fetched timeline")
        else:
            lines.append("  - PR status: not checked")
        lines.append(f"  - same-repo PR links: {row['same_repo_prs']}")
        lines.append(f"  - referenced by external repos? {'yes' if row['external_refs'] > 0 else 'no'}")
        lines.append(f"  - external references: {row['external_refs']}")
        lines.append(f"  - maintainer hinted direction? {'yes' if row['maintainer_hint_count'] > 0 else 'no'}")
        lines.append(f"  - maintainer-hint count: {row['maintainer_hint_count']}")
        lines.append(f"  - dormant days: {row['dormant_days']}")
        lines.append("")

    return lines


def render_churn_report(churn_report: list[dict]) -> list[str]:
    lines = ["## Churn / test investment report", ""]
    lines.append("Top files where tests, refactors, or smaller components may pay off:")
    lines.append("")
    for row in churn_report[:15]:
        file = row['file']
        churn = row['churn']
        bugfix_churn = row['bugfix_churn']
        todo_hints = row['todo_hits']
        line = f"- `{file}` — churn={churn}, bugfix_churn={bugfix_churn}, todo_hits={todo_hints}"
        lines.append(line)
    lines.append("")
    return lines


def render_topic_map(topic_map: list[dict]) -> list[str]:
    lines = ["## Topic map", ""]
    for topic in topic_map[:10]:
        lines.append(f"### {topic['title']}")
        lines.append("")
        lines.append(f"- issue count: {topic['issue_count']}")
        lines.append("- issues:")
        if topic["issues"]:
            for issue in topic["issues"]:
                if issue.get("url"):
                    lines.append(f"  - [#{issue['number']} — {issue['title']}]({issue['url']})")
                else:
                    lines.append(f"  - #{issue['number']} — {issue['title']}")
        else:
            lines.append("  - (none)")
        lines.append("")
        lines.append("")
        if topic["files"]:
            lines.append("- representative files:")
            for file in topic["files"]:
                lines.append(f"  - `{file}`")
            lines.append("")
    return lines


def main() -> None:
    if len(sys.argv) != 2:
        print("usage: build_report.py <config.yaml>")
        sys.exit(1)

    config = load_config(sys.argv[1])
    data_dir = Path(config["paths"]["data_dir"])
    report_path = Path(config["paths"]["report_path"])

    issue_clusters = read_json(data_dir / "issue_clusters.json", [])
    issue_candidates = read_json(data_dir / "issue_candidates.json", [])
    churn_report = read_json(data_dir / "churn_report.json", [])
    topic_map = read_json(data_dir / "topic_map.json", [])

    report_path.parent.mkdir(parents=True, exist_ok=True)

    lines: list[str] = []
    lines.append(f"# {config['repo']} opportunity report")
    lines.append("")
    lines.extend(make_summary(issue_clusters, topic_map, issue_candidates))
    lines.extend(render_issue_clusters(issue_clusters))
    lines.extend(render_issue_candidates(issue_candidates))
    lines.extend(render_churn_report(churn_report))
    lines.extend(render_topic_map(topic_map))

    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote report to {report_path}")


if __name__ == "__main__":
    main()
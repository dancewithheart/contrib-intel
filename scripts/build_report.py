#!/usr/bin/env python3

from __future__ import annotations

import sys
from pathlib import Path

from scripts.common import load_config, read_json


def make_summary(issue_clusters: list[dict], topic_map: list[dict]) -> list[str]:
    lines: list[str] = []

    lines.append("## Short summary")
    lines.append("")
    lines.append("Use the three sections below differently:")
    lines.append("")
    lines.append("1. **Issue clusters** — best for high-leverage fixes")
    lines.append("2. **Churn / test investment** — best for audits, refactors, and property-test opportunities")
    lines.append("3. **Topic map** — best for learning and exploration")
    lines.append("")

    top_clusters = issue_clusters[:3]
    if top_clusters:
        lines.append("Most promising current issue-cluster directions:")
        lines.append("")
        for idx, cluster in enumerate(top_clusters, start=1):
            issue_sample = ", ".join(f"#{n}" for n in cluster["issue_numbers"][:3]) or "no issue sample"
            file_sample = ", ".join(f"`{f}`" for f in cluster["files"][:2]) or "no file sample"
            lines.append(f"{idx}. **{cluster['title']}** — issues {issue_sample}; files {file_sample}")
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
        lines.append(f"- issues: {', '.join(f'#{n}' for n in cluster['issue_numbers']) or '(none)'}")
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


def render_churn_report(churn_report: list[dict]) -> list[str]:
    lines = ["## Churn / test investment report", ""]
    lines.append("Top files where tests, refactors, or smaller components may pay off:")
    lines.append("")
    for row in churn_report[:15]:
        lines.append(
            f"- `{row['file']}` — churn={row['churn']}, bugfix_churn={row['bugfix_churn']}, todo_hits={row['todo_hits']}"
        )
    lines.append("")
    return lines


def render_topic_map(topic_map: list[dict]) -> list[str]:
    lines = ["## Topic map", ""]
    for topic in topic_map[:10]:
        lines.append(f"### {topic['title']}")
        lines.append("")
        lines.append(f"- issue count: {topic['issue_count']}")
        lines.append(f"- issues: {', '.join(f'#{n}' for n in topic['issue_numbers']) or '(none)'}")
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
    churn_report = read_json(data_dir / "churn_report.json", [])
    topic_map = read_json(data_dir / "topic_map.json", [])

    report_path.parent.mkdir(parents=True, exist_ok=True)

    lines: list[str] = []
    lines.append(f"# {config['repo']} opportunity report")
    lines.append("")
    lines.extend(make_summary(issue_clusters, topic_map))
    lines.extend(render_issue_clusters(issue_clusters))
    lines.extend(render_churn_report(churn_report))
    lines.extend(render_topic_map(topic_map))

    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote report to {report_path}")


if __name__ == "__main__":
    main()
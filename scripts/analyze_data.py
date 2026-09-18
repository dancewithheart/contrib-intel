#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
import pandas as pd

from scripts.common import load_config, read_csv, read_json

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402


def markdown_table(frame: pd.DataFrame) -> str:
    """Render a small DataFrame without adding a runtime dependency on tabulate."""

    if frame.empty:
        return "_No data available._"

    display = frame.fillna("").astype(str)

    def cell(value: str) -> str:
        return value.replace("|", "\\|").replace("\n", " ")

    headers = [cell(str(column)) for column in display.columns]
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    lines.extend(
        "| " + " | ".join(cell(value) for value in row) + " |"
        for row in display.itertuples(index=False, name=None)
    )
    return "\n".join(lines)


def load_frames(data_dir: Path) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    issues = pd.DataFrame(read_json(data_dir / "issues.json", []))
    candidates = pd.DataFrame(read_json(data_dir / "issue_candidates.json", []))

    churn = pd.DataFrame(read_csv(data_dir / "file_churn.csv"))
    bugfix = pd.DataFrame(read_csv(data_dir / "bugfix_churn.csv"))

    if issues.empty or candidates.empty:
        raise RuntimeError(
            f"No ranked issue data in {data_dir}. Run the collection and ranking pipeline first."
        )

    if churn.empty:
        churn = pd.DataFrame(columns=["file", "churn"])
    if bugfix.empty:
        bugfix = pd.DataFrame(columns=["file", "bugfix_churn"])

    churn_frame = churn.merge(bugfix, on="file", how="outer")
    for column in ["churn", "bugfix_churn"]:
        churn_frame[column] = pd.to_numeric(churn_frame[column], errors="coerce").fillna(0)

    return issues, candidates, churn_frame


def add_analysis_columns(issues: pd.DataFrame, candidates: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    issues = issues.copy()
    candidates = candidates.copy()

    now = pd.Timestamp.now(tz="UTC")
    created_at = pd.to_datetime(issues.get("created_at"), utc=True, errors="coerce")
    issues["age_days"] = (now - created_at).dt.days
    candidates["local_score"] = pd.to_numeric(candidates["local_score"], errors="coerce")
    candidates["dormant_days"] = pd.to_numeric(candidates["dormant_days"], errors="coerce")
    candidates["subsystem"] = candidates["subsystem"].fillna("unknown")

    return issues, candidates


def save_plots(
    issues: pd.DataFrame,
    candidates: pd.DataFrame,
    churn: pd.DataFrame,
    assets_dir: Path,
) -> list[Path]:
    assets_dir.mkdir(parents=True, exist_ok=True)
    plt.style.use("seaborn-v0_8-whitegrid")

    subsystem_path = assets_dir / "subsystem-counts.png"
    subsystem_counts = candidates["subsystem"].value_counts().sort_values()
    fig, axis = plt.subplots(figsize=(9, 5))
    subsystem_counts.plot.barh(ax=axis, color="#4C78A8")
    axis.set(title="Ranked issues by inferred subsystem", xlabel="Issue count", ylabel="")
    fig.tight_layout()
    fig.savefig(subsystem_path, dpi=160)
    plt.close(fig)

    distribution_path = assets_dir / "issue-and-score-distributions.png"
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
    issues["age_days"].dropna().hist(bins=25, ax=axes[0], color="#59A14F")
    axes[0].set(title="Open issue age", xlabel="Age (days)", ylabel="Issues")
    candidates["local_score"].dropna().hist(bins=25, ax=axes[1], color="#F28E2B")
    axes[1].set(title="Candidate score distribution", xlabel="Heuristic score", ylabel="Issues")
    fig.tight_layout()
    fig.savefig(distribution_path, dpi=160)
    plt.close(fig)

    churn_path = assets_dir / "churn-vs-bugfix.png"
    fig, axis = plt.subplots(figsize=(7, 5))
    axis.scatter(churn["churn"], churn["bugfix_churn"], alpha=0.45, s=18, color="#E15759")
    axis.set(
        title="File churn vs bug-fix-related churn",
        xlabel="Commits touching file",
        ylabel="Bug-fix commits touching file",
    )
    fig.tight_layout()
    fig.savefig(churn_path, dpi=160)
    plt.close(fig)

    return [subsystem_path, distribution_path, churn_path]


def build_report(
    repo: str,
    issues: pd.DataFrame,
    candidates: pd.DataFrame,
    churn: pd.DataFrame,
    report_path: Path,
    plot_paths: list[Path],
) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)

    subsystem_counts = (
        candidates["subsystem"]
        .value_counts()
        .rename_axis("subsystem")
        .reset_index(name="issue_count")
    )

    top_candidates = candidates.nlargest(10, "local_score")[
        ["number", "title", "subsystem", "local_score", "recommendation"]
    ].copy()
    top_candidates["title"] = top_candidates["title"].str.slice(0, 90)

    score_summary = (
        candidates[["local_score", "dormant_days"]]
        .describe()
        .round(2)
        .rename_axis("statistic")
        .reset_index()
    )

    correlation = churn[["churn", "bugfix_churn"]].corr().iloc[0, 1]
    correlation_text = "undefined" if pd.isna(correlation) else f"{correlation:.3f}"

    relative_plots = [path.relative_to(report_path.parent) for path in plot_paths]
    lines = [
        f"# {repo} data analysis",
        "",
        "This report summarizes the intermediate data produced by `contrib-intel`.",
        "Candidate scores are heuristic ranking signals, not probabilities.",
        "",
        "## Dataset",
        "",
        f"- open issues: **{len(issues):,}**",
        f"- ranked candidates: **{len(candidates):,}**",
        f"- files with churn data: **{len(churn):,}**",
        "",
        "## Subsystem counts",
        "",
        markdown_table(subsystem_counts),
        "",
        f"![Subsystem counts]({relative_plots[0].as_posix()})",
        "",
        "## Issue age and candidate scores",
        "",
        markdown_table(score_summary),
        "",
        f"![Issue and score distributions]({relative_plots[1].as_posix()})",
        "",
        "## Churn relationship",
        "",
        "Pearson correlation between total file churn and bug-fix-related churn: "
        f"**{correlation_text}**.",
        "",
        "This correlation is descriptive. Commit-subject matching is a proxy and does not "
        "establish that churn causes defects.",
        "",
        f"![Churn versus bug-fix churn]({relative_plots[2].as_posix()})",
        "",
        "## Top candidates",
        "",
        markdown_table(top_candidates),
        "",
    ]
    report_path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Analyze contrib-intel intermediate data")
    parser.add_argument("config", help="Path to a repository YAML config")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = load_config(args.config)
    data_dir = Path(config["paths"]["data_dir"])
    opportunity_report = Path(config["paths"]["report_path"])
    report_path = opportunity_report.with_name(f"{config['repo']}-analysis.md")
    assets_dir = report_path.parent / "assets" / config["repo"]

    issues, candidates, churn = load_frames(data_dir)
    issues, candidates = add_analysis_columns(issues, candidates)
    plot_paths = save_plots(issues, candidates, churn, assets_dir)
    build_report(config["repo"], issues, candidates, churn, report_path, plot_paths)
    print(f"wrote analysis report to {report_path}")


if __name__ == "__main__":
    main()

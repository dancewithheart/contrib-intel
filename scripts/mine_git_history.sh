#!/usr/bin/env python3

from __future__ import annotations

import csv
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

import yaml


def load_config(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def run_git(repo_root: Path, args: list[str]) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=repo_root,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout


def parse_name_only_log(text: str) -> tuple[Counter[str], Counter[str]]:
    churn = Counter()
    bugfix_churn = Counter()

    current_is_bugfix = False

    for raw_line in text.splitlines():
        line = raw_line.strip()

        if line.startswith("SUBJECT:"):
            subject = line.removeprefix("SUBJECT:").strip().lower()
            current_is_bugfix = any(
                term in subject
                for term in ["fix", "bug", "regression", "warning", "error"]
            )
            continue

        if not line or line.startswith("COMMIT:"):
            continue

        churn[line] += 1
        if current_is_bugfix:
            bugfix_churn[line] += 1

    return churn, bugfix_churn


def write_counter_csv(path: Path, counter: Counter[str], column_name: str) -> None:
    rows = [{"file": file, column_name: count} for file, count in counter.most_common()]
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["file", column_name])
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    if len(sys.argv) != 2:
        print("usage: mine_git_history.py <config.yaml>")
        sys.exit(1)

    config = load_config(sys.argv[1])
    repo_root = Path(config["paths"]["local_repo"])
    data_dir = Path(config["paths"]["data_dir"])
    data_dir.mkdir(parents=True, exist_ok=True)

    log_text = run_git(
        repo_root,
        [
            "log",
            "--name-only",
            "--pretty=format:COMMIT:%H%nSUBJECT:%s",
            "--",
            ".",
        ],
    )

    churn, bugfix_churn = parse_name_only_log(log_text)

    write_counter_csv(data_dir / "file_churn.csv", churn, "churn")
    write_counter_csv(data_dir / "bugfix_churn.csv", bugfix_churn, "bugfix_churn")

    print(f"saved churn for {len(churn)} files")
    print(f"saved bugfix churn for {len(bugfix_churn)} files")


if __name__ == "__main__":
    main()

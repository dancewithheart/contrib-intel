#!/usr/bin/env python3

from __future__ import annotations

import subprocess
import sys
from collections import Counter
from pathlib import Path

from scripts.common import load_config, write_csv


BUGFIX_TERMS = ["fix", "bug", "regression", "warning", "error"]


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
            current_is_bugfix = any(term in subject for term in BUGFIX_TERMS)
            continue

        if not line or line.startswith("COMMIT:"):
            continue

        churn[line] += 1
        if current_is_bugfix:
            bugfix_churn[line] += 1

    return churn, bugfix_churn


def main() -> None:
    if len(sys.argv) != 2:
        print("usage: mine_git_history.py <config.yaml>")
        sys.exit(1)

    config = load_config(sys.argv[1])
    repo_root = Path(config["paths"]["local_repo"]).expanduser()
    data_dir = Path(config["paths"]["data_dir"])

    log_text = run_git(
        repo_root,
        ["log", "--name-only", "--pretty=format:COMMIT:%H%nSUBJECT:%s", "--", "."],
    )

    churn, bugfix_churn = parse_name_only_log(log_text)

    write_csv(
        data_dir / "file_churn.csv",
        [{"file": file, "churn": count} for file, count in churn.most_common()],
        ["file", "churn"],
    )
    write_csv(
        data_dir / "bugfix_churn.csv",
        [{"file": file, "bugfix_churn": count} for file, count in bugfix_churn.most_common()],
        ["file", "bugfix_churn"],
    )

    print(f"saved churn for {len(churn)} files")
    print(f"saved bugfix churn for {len(bugfix_churn)} files")


if __name__ == "__main__":
    main()

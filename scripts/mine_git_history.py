#!/usr/bin/env python3

from __future__ import annotations

import subprocess
import sys
from collections import Counter
from pathlib import Path

from scripts.common import load_config, write_csv

BUGFIX_TERMS = [
    "fix",
    "bug",
    "regression",
    "warning",
    "error",
    "panic",
    "impossible",
    "invariant",
    "unsolved",
    "confluence",
    "termination",
    "coverage",
]


def is_included(rel_path: str, config: dict) -> bool:
    filters = config.get("filters", {})
    include_paths = filters.get("include_paths", [])
    exclude_paths = filters.get("exclude_paths", [])
    exclude_file_names = set(filters.get("exclude_file_names", []))
    exclude_suffixes = filters.get("exclude_suffixes", [])

    file_name = Path(rel_path).name

    if include_paths and not any(rel_path.startswith(prefix) for prefix in include_paths):
        return False

    if any(rel_path.startswith(prefix) for prefix in exclude_paths):
        return False

    if file_name in exclude_file_names:
        return False

    if any(rel_path.endswith(suffix) for suffix in exclude_suffixes):
        return False

    return True


def run_git(repo_root: Path, args: list[str]) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=repo_root,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout


def parse_name_only_log(text: str, config: dict) -> tuple[Counter[str], Counter[str]]:
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

        if not is_included(line, config):
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

    churn, bugfix_churn = parse_name_only_log(log_text, config)

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
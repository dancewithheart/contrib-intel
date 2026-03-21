#!/usr/bin/env python3

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

import yaml


TEXT_FILE_EXTENSIONS = {
    ".scala",
    ".java",
    ".sbt",
    ".md",
    ".txt",
    ".yaml",
    ".yml",
    ".json",
}


def load_config(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def iter_text_files(root: Path):
    for path in root.rglob("*"):
        if path.is_file() and path.suffix in TEXT_FILE_EXTENSIONS:
            yield path


def find_pattern_hits(repo_root: Path, patterns: list[str]) -> list[dict]:
    hits: list[dict] = []

    for path in iter_text_files(repo_root):
        try:
            lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
        except Exception:
            continue

        for line_no, line in enumerate(lines, start=1):
            for pattern in patterns:
                if pattern.lower() in line.lower():
                    hits.append(
                        {
                            "file": str(path.relative_to(repo_root)),
                            "line": line_no,
                            "pattern": pattern,
                            "text": line.strip(),
                        }
                    )

    return hits


def count_subsystem_keywords(repo_root: Path, subsystems: dict[str, list[str]]) -> list[dict]:
    counts: dict[tuple[str, str], int] = {}

    for path in iter_text_files(repo_root):
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue

        rel = str(path.relative_to(repo_root))

        for subsystem, keywords in subsystems.items():
            total = sum(text.lower().count(keyword.lower()) for keyword in keywords)
            if total > 0:
                counts[(rel, subsystem)] = total

    return [
        {"file": file, "subsystem": subsystem, "count": count}
        for (file, subsystem), count in sorted(counts.items())
    ]


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    if len(sys.argv) != 2:
        print("usage: scan_repo_signals.py <config.yaml>")
        sys.exit(1)

    config = load_config(sys.argv[1])
    repo_root = Path(config["paths"]["local_repo"])
    data_dir = Path(config["paths"]["data_dir"])
    data_dir.mkdir(parents=True, exist_ok=True)

    grep_patterns = config["keywords"]["grep_patterns"]
    subsystems = config["keywords"]["subsystems"]

    todo_hits = find_pattern_hits(repo_root, grep_patterns)
    subsystem_hits = count_subsystem_keywords(repo_root, subsystems)

    write_csv(
        data_dir / "todo_hits.csv",
        todo_hits,
        ["file", "line", "pattern", "text"],
    )
    write_csv(
        data_dir / "subsystem_hits.csv",
        subsystem_hits,
        ["file", "subsystem", "count"],
    )

    summary = {
        "todo_hit_count": len(todo_hits),
        "subsystem_file_matches": len(subsystem_hits),
    }
    (data_dir / "scan_summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )

    print(f"saved {len(todo_hits)} todo/signal hits")
    print(f"saved {len(subsystem_hits)} subsystem file matches")


if __name__ == "__main__":
    main()

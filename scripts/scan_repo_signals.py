#!/usr/bin/env python3

from __future__ import annotations

import sys
from pathlib import Path

from scripts.common import load_config, write_csv, write_json


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

        rel = str(path.relative_to(repo_root))

        for line_no, line in enumerate(lines, start=1):
            lowered = line.lower()
            for pattern in patterns:
                if pattern.lower() in lowered:
                    hits.append(
                        {
                            "file": rel,
                            "line": line_no,
                            "pattern": pattern,
                            "text": line.strip(),
                        }
                    )

    return hits


def count_subsystem_keywords(repo_root: Path, subsystems: dict[str, list[str]]) -> list[dict]:
    rows: list[dict] = []

    for path in iter_text_files(repo_root):
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue

        rel = str(path.relative_to(repo_root))
        lowered = text.lower()

        for subsystem, keywords in subsystems.items():
            count = sum(lowered.count(keyword.lower()) for keyword in keywords)
            if count > 0:
                rows.append(
                    {
                        "file": rel,
                        "subsystem": subsystem,
                        "count": count,
                    }
                )

    return rows


def main() -> None:
    if len(sys.argv) != 2:
        print("usage: scan_repo_signals.py <config.yaml>")
        sys.exit(1)

    config = load_config(sys.argv[1])
    repo_root = Path(config["paths"]["local_repo"]).expanduser()
    data_dir = Path(config["paths"]["data_dir"])

    todo_hits = find_pattern_hits(repo_root, config["keywords"]["grep_patterns"])
    subsystem_hits = count_subsystem_keywords(repo_root, config["keywords"]["subsystems"])

    write_csv(data_dir / "todo_hits.csv", todo_hits, ["file", "line", "pattern", "text"])
    write_csv(data_dir / "subsystem_hits.csv", subsystem_hits, ["file", "subsystem", "count"])
    write_json(
        data_dir / "scan_summary.json",
        {
            "todo_hit_count": len(todo_hits),
            "subsystem_file_matches": len(subsystem_hits),
        },
        )

    print(f"saved {len(todo_hits)} repo signal hits")
    print(f"saved {len(subsystem_hits)} subsystem matches")


if __name__ == "__main__":
    main()
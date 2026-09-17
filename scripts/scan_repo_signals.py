#!/usr/bin/env python3

from __future__ import annotations

import sys
from pathlib import Path

from scripts.common import (
    git_tracked_files,
    load_config,
    write_csv,
    write_json,
)

DEFAULT_TEXT_FILE_EXTENSIONS = {
    ".hs",
    ".lhs",
    ".agda",
    ".lagda",
    ".lagda.md",
    ".el",
    ".scala",
    ".java",
    ".sbt",
    ".md",
    ".txt",
    ".yaml",
    ".yml",
    ".json",
}


def configured_text_file_extensions(config: dict) -> set[str]:
    filters = config.get("filters", {})
    configured = filters.get("text_file_extensions")

    if not configured:
        return set(DEFAULT_TEXT_FILE_EXTENSIONS)

    result: set[str] = set()
    for ext in configured:
        if not ext:
            continue
        ext = str(ext).strip()
        if not ext:
            continue
        if not ext.startswith("."):
            ext = f".{ext}"
        result.add(ext)

    return result or set(DEFAULT_TEXT_FILE_EXTENSIONS)


def matches_configured_extension(path: Path, allowed_extensions: set[str]) -> bool:
    suffixes = path.suffixes
    if not suffixes:
        return False

    # Support both normal suffixes like ".hs" and multi-suffix files like ".lagda.md".
    for i in range(len(suffixes)):
        combined = "".join(suffixes[i:])
        if combined in allowed_extensions:
            return True

    return False


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


def iter_tracked_text_files(repo_root: Path, config: dict):
    allowed_extensions = configured_text_file_extensions(config)

    for rel in git_tracked_files(repo_root):
        path = repo_root / rel
        if not matches_configured_extension(path, allowed_extensions):
            continue
        if not is_included(rel, config):
            continue
        yield rel, path


def find_pattern_hits(repo_root: Path, patterns: list[str], config: dict) -> list[dict]:
    hits: list[dict] = []

    for rel, path in iter_tracked_text_files(repo_root, config):
        try:
            lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
        except Exception:
            continue

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


def count_subsystem_keywords(repo_root: Path, subsystems: dict[str, list[str]], config: dict) -> list[dict]:
    rows: list[dict] = []

    for rel, path in iter_tracked_text_files(repo_root, config):
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue

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

    todo_hits = find_pattern_hits(repo_root, config["keywords"]["grep_patterns"], config)
    subsystem_hits = count_subsystem_keywords(repo_root, config["keywords"]["subsystems"], config)

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
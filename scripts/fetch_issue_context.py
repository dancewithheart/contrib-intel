#!/usr/bin/env python3

from __future__ import annotations

import json
import os
import sys
import time
import urllib.request
from pathlib import Path

from scripts.common import ensure_dir, load_config, read_json, write_json


def github_get(url: str, token: str | None, accept: str = "application/vnd.github+json") -> list[dict]:
    req = urllib.request.Request(url)
    req.add_header("Accept", accept)
    req.add_header("User-Agent", "contrib-intel")
    if token:
        req.add_header("Authorization", f"Bearer {token}")

    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_paginated(url: str, token: str | None, accept: str = "application/vnd.github+json") -> list[dict]:
    results: list[dict] = []
    page = 1

    while True:
        page_url = f"{url}{'&' if '?' in url else '?'}per_page=100&page={page}"
        items = github_get(page_url, token, accept=accept)
        if not items:
            break
        results.extend(items)
        if len(items) < 100:
            break
        page += 1
        time.sleep(0.2)

    return results


def main() -> None:
    if len(sys.argv) not in {2, 3}:
        print("usage: fetch_issue_context.py <config.yaml> [--refresh]")
        sys.exit(1)

    config = load_config(sys.argv[1])
    refresh = len(sys.argv) == 3 and sys.argv[2] == "--refresh"

    owner = config["owner"]
    name = config["name"]
    use_cache = config["github"].get("use_cache", True)
    max_issue_context = config["github"].get("max_issue_context", 100)

    data_dir = Path(config["paths"]["data_dir"])
    issues = read_json(data_dir / "issues.json", [])
    issues = issues[:max_issue_context]

    token = os.environ.get("GITHUB_TOKEN")

    context_dir = data_dir / "issue_context"
    ensure_dir(context_dir)

    summary: list[dict] = []

    for issue in issues:
        number = issue["number"]
        issue_dir = context_dir / str(number)
        ensure_dir(issue_dir)

        comments_path = issue_dir / "comments.json"
        timeline_path = issue_dir / "timeline.json"

        if use_cache and not refresh and comments_path.exists() and timeline_path.exists():
            comments = read_json(comments_path, [])
            timeline = read_json(timeline_path, [])
        else:
            comments_url = f"https://api.github.com/repos/{owner}/{name}/issues/{number}/comments"
            timeline_url = f"https://api.github.com/repos/{owner}/{name}/issues/{number}/timeline"

            comments = fetch_paginated(comments_url, token)
            timeline = fetch_paginated(
                timeline_url,
                token,
                accept="application/vnd.github.mockingbird-preview+json",
            )

            write_json(comments_path, comments)
            write_json(timeline_path, timeline)
            time.sleep(0.2)

        summary.append(
            {
                "number": number,
                "comments_path": str(comments_path),
                "timeline_path": str(timeline_path),
                "comment_count": len(comments),
                "timeline_event_count": len(timeline),
            }
        )

    write_json(data_dir / "issue_context_index.json", summary)
    print(f"saved context for {len(summary)} issues")


if __name__ == "__main__":
    main()
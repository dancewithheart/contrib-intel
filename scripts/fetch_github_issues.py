#!/usr/bin/env python3

from __future__ import annotations

import json
import os
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

from scripts.common import ensure_dir, load_config, read_json, write_json


def github_get(url: str, token: str | None) -> list[dict]:
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "contrib-intel")
    if token:
        req.add_header("Authorization", f"Bearer {token}")

    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_pages(base_url: str, token: str | None, max_items: int) -> list[dict]:
    results: list[dict] = []
    page = 1

    while len(results) < max_items:
        url = f"{base_url}&page={page}"
        items = github_get(url, token)
        if not items:
            break
        results.extend(items)
        if len(items) < 100:
            break
        page += 1
        time.sleep(0.2)

    return results[:max_items]


def main() -> None:
    if len(sys.argv) not in {2, 3}:
        print("usage: fetch_github_issues.py <config.yaml> [--refresh]")
        sys.exit(1)

    config = load_config(sys.argv[1])
    refresh = len(sys.argv) == 3 and sys.argv[2] == "--refresh"

    owner = config["owner"]
    name = config["name"]
    state = config["issue_queries"]["state"]
    per_page = config["github"]["per_page"]
    max_issues = config["github"]["max_issues"]
    max_prs = config["github"]["max_prs"]
    use_cache = config["github"].get("use_cache", True)

    data_dir = Path(config["paths"]["data_dir"])
    ensure_dir(data_dir)

    issues_path = data_dir / "issues.json"
    prs_path = data_dir / "prs.json"

    if use_cache and not refresh and issues_path.exists() and prs_path.exists():
        issues = read_json(issues_path, [])
        prs = read_json(prs_path, [])
        print(f"loaded {len(issues)} cached issues from {issues_path}")
        print(f"loaded {len(prs)} cached prs from {prs_path}")
        return

    token = os.environ.get("GITHUB_TOKEN")

    base = f"https://api.github.com/repos/{owner}/{name}/issues"
    common = f"?state={urllib.parse.quote(state)}&per_page={per_page}"

    all_items = fetch_pages(base + common, token, max(max_issues, max_prs))
    issues = [x for x in all_items if "pull_request" not in x][:max_issues]
    prs = [x for x in all_items if "pull_request" in x][:max_prs]

    write_json(issues_path, issues)
    write_json(prs_path, prs)

    print(f"saved {len(issues)} issues to {issues_path}")
    print(f"saved {len(prs)} prs to {prs_path}")


if __name__ == "__main__":
    main()

#!/usr/bin/env bash
set -euo pipefail

project="${1:-scala3}"
refresh="${2:-}"
config="configs/${project}.yaml"

if [[ ! -f "$config" ]]; then
  echo "Config not found: $config"
  echo "Available configs:"
  find configs -maxdepth 1 -name '*.yaml' -printf '  %f\n' | sort
  exit 1
fi

if [[ -n "$refresh" && "$refresh" != "--refresh" ]]; then
  echo "usage: ./go.sh [project] [--refresh]"
  exit 1
fi

refresh_args=()
if [[ "$refresh" == "--refresh" ]]; then
  refresh_args+=("--refresh")
fi

python3 -m scripts.fetch_github_issues "$config" "${refresh_args[@]}"
python3 -m scripts.fetch_issue_context "$config" "${refresh_args[@]}"
python3 -m scripts.rank_candidates "$config"
python3 -m scripts.build_report "$config"

report="reports/${project}-opportunities.md"

printf 'Generated %s\n' "$report"
printf '\nCandidate sample:\n'
sed -n '/Top concrete issue candidates:/,+9p' "$report"

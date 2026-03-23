#!/usr/bin/env bash
set -euo pipefail

export OS_PROJECT=io-sim
#export OS_PROJECT=scala3
export FILE=configs/${OS_PROJECT}.yaml

if [[ ! -f "$FILE" ]]; then
  echo "Config not found: $FILE"
  echo "Available configs:"
  ls configs/*.yaml
  exit 1
fi

python3 -m scripts.scan_repo_signals "$FILE"
python3 -m scripts.mine_git_history "$FILE"
python3 -m scripts.rank_candidates "$FILE"

python3 -m scripts.build_report "$FILE"
export REPORT=reports/${OS_PROJECT}-opportunities.md

if [[ -f "$REPORT" ]]; then
  cat "$REPORT"
else
  echo "Report not found: $REPORT"
  exit 1
fi

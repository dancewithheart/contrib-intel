

```sh
export FILE=configs/scala3.yaml
export FILE=configs/io-sim.yaml

python3 -m scripts.fetch_github_issues $FILE
python3 -m scripts.fetch_github_issues $FILE --refresh
python3 -m scripts.fetch_issue_context "$FILE"
python3 -m scripts.fetch_issue_context "$FILE" --refresh
python3 -m scripts.scan_repo_signals $FILE
python3 -m scripts.mine_git_history $FILE
python3 -m scripts.rank_candidates $FILE
python3 -m scripts.build_report $FILE
```

```sh
python3 -m pytest -vv
```
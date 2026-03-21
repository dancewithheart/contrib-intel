

```sh
python3 -m scripts.fetch_github_issues configs/scala3.yaml
python3 -m scripts.fetch_github_issues configs/scala3.yaml --refresh

python3 -m scripts.scan_repo_signals configs/scala3.yaml
python3 -m scripts.mine_git_history configs/scala3.yaml
python3 -m scripts.rank_candidates configs/scala3.yaml
python3 -m scripts.build_report configs/scala3.yaml
```

```sh
python3 -m pytest -vv
```
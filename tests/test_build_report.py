from scripts.build_report import make_summary

def test_summary_contains_issue_without_open_pr():
    candidates = [
        {
            "number": 123,
            "title": "Useful bug",
            "url": "https://github.com/example/repo/issues/123",
            "pr_status": "no_open_pr_found",
            "open_prs": [],
        },
        {
            "number": 124,
            "title": "Already being worked on",
            "url": "https://github.com/example/repo/issues/124",
            "pr_status": "open_pr",
            "open_prs": [
                {
                    "number": 200,
                    "url": "https://github.com/example/repo/pull/200",
                    "state": "open",
                    "draft": False,
                }
            ],
        },
    ]

    text = "\n".join(make_summary(candidates))

    assert "#123" in text
    assert "#124" not in text

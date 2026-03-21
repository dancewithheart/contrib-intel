from scripts.rank_candidates import analyze_issue_context


def test_analyze_issue_context_detects_signals():
    config = {
        "owner": "scala",
        "name": "scala3",
        "context_rules": {
            "maintainer_handles": ["odersky"],
            "maintainer_hint_phrases": ["we should", "would be nice"],
            "dormant_days_threshold": 30,
        },
    }

    issue = {
        "number": 1,
        "updated_at": "2025-01-01T00:00:00Z",
    }

    context = {
        "comments": [
            {
                "user": {"login": "odersky"},
                "body": "we should probably handle this in typer",
            }
        ],
        "timeline": [
            {
                "event": "cross-referenced",
                "source": {
                    "issue": {
                        "repository": {"full_name": "scala/scala3"},
                        "pull_request": {"url": "x"},
                    }
                },
            },
            {
                "event": "cross-referenced",
                "source": {
                    "issue": {
                        "repository": {"full_name": "zio/zio"},
                    }
                },
            },
        ],
    }

    result = analyze_issue_context(issue, context, config)

    assert result["same_repo_prs"] == 1
    assert result["external_refs"] == 1
    assert result["maintainer_hints"]
    assert isinstance(result["is_dormant"], bool)
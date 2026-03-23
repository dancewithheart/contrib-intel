from scripts.rank_candidates import issue_recommendation, score_issue_candidate


def test_issue_recommendation_prefers_maintainer_and_external_signal():
    analysis = {
        "same_repo_prs": 0,
        "external_refs": 2,
        "maintainer_hints": ["we should"],
        "dormant_days": 50,
        "is_dormant": False,
    }

    rec = issue_recommendation(analysis)
    assert "strong candidate" in rec


def test_issue_score_penalizes_same_repo_prs():
    config = {
        "context_scoring": {
            "same_repo_pr_penalty": 4.0,
            "external_reference_bonus": 3.0,
            "maintainer_hint_bonus": 4.0,
            "dormant_bonus": 2.0,
        }
    }

    analysis = {
        "same_repo_prs": 1,
        "external_refs": 0,
        "maintainer_hints": [],
        "dormant_days": 10,
        "is_dormant": False,
    }

    score = score_issue_candidate(analysis, subsystem_match_score=5, config=config)
    assert score == 1.0
from scripts.rank_candidates import issue_matches_keywords


def test_issue_matches_keywords():
    issue = {
        "title": "MatchTypeNoCases is no longer emitted",
        "body": "TypeComparer path looks dormant",
        "labels": [{"name": "bug"}],
    }

    assert issue_matches_keywords(issue, ["MatchTypeNoCases"])
    assert issue_matches_keywords(issue, ["TypeComparer"])
    assert not issue_matches_keywords(issue, ["explicit nulls"])

from scripts.build_report import make_summary


def test_make_summary_contains_top_candidates():
    issue_clusters = [
        {
            "title": "Match Types",
            "issues": [
                {
                    "number": 24753,
                    "title": "MatchTypeNoCases is no longer emitted",
                    "url": "https://github.com/scala/scala3/issues/24753",
                },
                {
                    "number": 23822,
                    "title": "Match type reduction does not fail even if selector matches none of the cases",
                    "url": "https://github.com/scala/scala3/issues/23822",
                },
            ],
            "files": ["compiler/src/dotty/tools/dotc/core/TypeComparer.scala"],
        },
        {
            "title": "Diagnostics",
            "issues": [
                {
                    "number": 100,
                    "title": "Some diagnostics issue",
                    "url": "https://github.com/scala/scala3/issues/100",
                }
            ],
            "files": ["compiler/src/dotty/tools/dotc/reporting/Reporter.scala"],
        },
    ]

    topic_map = [
        {
            "title": "Typer",
            "issues": [
                {
                    "number": 1,
                    "title": "Typer issue one",
                    "url": "https://github.com/scala/scala3/issues/1",
                },
                {
                    "number": 2,
                    "title": "Typer issue two",
                    "url": "https://github.com/scala/scala3/issues/2",
                },
            ],
            "files": ["compiler/src/dotty/tools/dotc/typer/Typer.scala"],
        }
    ]

    issue_candidates = [
        {
            "number": 24753,
            "title": "MatchTypeNoCases is no longer emitted",
            "subsystem": "match_types",
            "local_score": 9.0,
            "recommendation": "good candidate: maintainer hinted direction",
        }
    ]

    lines = make_summary(issue_clusters, topic_map, issue_candidates)
    text = "\n".join(lines)

    assert "Short summary" in text
    assert "Match Types" in text
    assert "#24753" in text
    assert "Top concrete issue candidates" in text
    assert "MatchTypeNoCases is no longer emitted" in text
from scripts.build_report import make_summary


def test_make_summary_contains_top_candidates():
    issue_clusters = [
        {
            "title": "Match Types",
            "issue_numbers": [24753, 23822],
            "files": ["compiler/src/dotty/tools/dotc/core/TypeComparer.scala"],
        },
        {
            "title": "Diagnostics",
            "issue_numbers": [100],
            "files": ["compiler/src/dotty/tools/dotc/reporting/Reporter.scala"],
        },
    ]

    topic_map = [
        {
            "title": "Typer",
            "issue_numbers": [1, 2],
            "files": ["compiler/src/dotty/tools/dotc/typer/Typer.scala"],
        }
    ]

    lines = make_summary(issue_clusters, topic_map)
    text = "\n".join(lines)

    assert "Short summary" in text
    assert "Match Types" in text
    assert "#24753" in text
    assert "Issue clusters" in text
    assert "Churn / test investment" in text
    assert "Topic map" in text
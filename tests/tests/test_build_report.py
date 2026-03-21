from scripts.build_report import make_summary


def test_make_summary_contains_top_candidates():
    candidates = [
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

    lines = make_summary(candidates)
    text = "\n".join(lines)

    assert "Short summary" in text
    assert "Match Types" in text
    assert "#24753" in text
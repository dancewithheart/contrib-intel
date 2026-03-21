from pathlib import Path

from scripts.scan_repo_signals import find_pattern_hits, count_subsystem_keywords


def test_finds_todo_and_todo_warn_hits_in_source_files(tmp_path: Path):
    repo = tmp_path / "repo"
    repo.mkdir()
    f = repo / "Test.scala"
    f.write_text(
        "// TODO warn ?\n"
        "object Test\n",
        encoding="utf-8",
    )

    hits = find_pattern_hits(repo, ["TODO", "TODO warn"])
    assert len(hits) == 2
    assert hits[0]["file"] == "Test.scala"


def test_counts_configured_subsystem_keywords_per_file(tmp_path: Path):
    repo = tmp_path / "repo"
    repo.mkdir()
    f = repo / "TypeComparer.scala"
    f.write_text(
        'object X { val s = "MatchTypeNoCases TypeComparer" }\n',
        encoding="utf-8",
    )

    rows = count_subsystem_keywords(
        repo,
        {"match_types": ["MatchTypeNoCases", "TypeComparer"]},
    )

    assert len(rows) == 1
    assert rows[0]["file"] == "TypeComparer.scala"
    assert rows[0]["subsystem"] == "match_types"
    assert rows[0]["count"] == 2
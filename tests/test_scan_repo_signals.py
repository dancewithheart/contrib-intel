from pathlib import Path

from scripts.scan_repo_signals import find_pattern_hits, count_subsystem_keywords


def test_find_pattern_hits(tmp_path: Path):
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


def test_count_subsystem_keywords(tmp_path: Path):
    repo = tmp_path / "repo"
    repo.mkdir()
    f = repo / "TypeComparer.scala"
    f.write_text(
        "object X { val s = \"MatchTypeNoCases TypeComparer\" }\n",
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

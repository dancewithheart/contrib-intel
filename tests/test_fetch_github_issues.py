from pathlib import Path

from scripts.common import write_json, read_json


def test_cached_issue_files_are_read(tmp_path: Path):
    data_dir = tmp_path / "data" / "scala3"
    issues_path = data_dir / "issues.json"
    prs_path = data_dir / "prs.json"

    write_json(issues_path, [{"number": 1, "title": "a"}])
    write_json(prs_path, [{"number": 2, "title": "b"}])

    assert read_json(issues_path, []) == [{"number": 1, "title": "a"}]
    assert read_json(prs_path, []) == [{"number": 2, "title": "b"}]

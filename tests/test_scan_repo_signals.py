from scripts.scan_repo_signals import is_included


def test_is_included_filters_output_file():
    config = {
        "filters": {
            "include_paths": ["compiler/src/dotty/tools/dotc/", "tests/"],
            "exclude_paths": ["out/"],
            "exclude_file_names": ["output_full.txt"],
            "exclude_suffixes": [".log"],
        }
    }

    assert is_included("compiler/src/dotty/tools/dotc/core/TypeComparer.scala", config)
    assert not is_included("output_full.txt", config)
    assert not is_included("out/tmp.scala", config)
    assert not is_included("docs/file.md", config)
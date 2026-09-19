from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

def load_config(path: str) -> dict[str, Any]:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)

def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)

def read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))

def write_json(path: Path, value: Any) -> None:
    ensure_dir(path.parent)
    path.write_text(json.dumps(value, indent=2), encoding="utf-8")

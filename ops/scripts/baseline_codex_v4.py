#!/usr/bin/env python3
"""Generate baseline for platform_v_4_0/main.

Derived from instructions in platform_v_4_0/main/prompt_codex_baseline_v_4_check.md
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any, Dict, List

import yaml


def parse_file_metadata(file_path: Path) -> Dict[str, Any]:
    """Return metadata about a file.

    Parameters
    ----------
    file_path: Path
        File to inspect for YAML front matter.

    Returns
    -------
    dict with keys: name, version, has_yaml
    """
    info: Dict[str, Any] = {"name": file_path.name, "version": None, "has_yaml": False}
    try:
        with file_path.open("r", encoding="utf-8") as fh:
            first_line = fh.readline().strip()
            if first_line == "---":
                yaml_lines: List[str] = []
                for line in fh:
                    if line.strip() == "---":
                        break
                    yaml_lines.append(line)
                meta = yaml.safe_load("".join(yaml_lines)) or {}
                info["has_yaml"] = True
                info["version"] = meta.get("VERSION")
    except Exception:
        # Ignore unreadable files
        pass
    return info


def collect_baseline(root: Path) -> List[Dict[str, Any]]:
    """Traverse platform_v_4_0/main and collect metadata."""
    base_path = root / "platform_v_4_0" / "main"
    results: List[Dict[str, Any]] = []
    for folder, _dirs, files in os.walk(base_path):
        folder_path = Path(folder)
        rel_folder = folder_path.relative_to(base_path)
        file_infos = [parse_file_metadata(folder_path / f) for f in sorted(files)]
        results.append({"folder": str(rel_folder), "files": file_infos})
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description="Baseline Codex V4")
    parser.add_argument(
        "--root",
        default=str(Path(__file__).resolve().parents[2]),
        help="Repository root path",
    )
    parser.add_argument(
        "--format",
        choices=["json", "yaml"],
        default="json",
        help="Output serialization format",
    )
    parser.add_argument(
        "--log",
        default="ops/log/baseline_codex_v4.log",
        help="Path to log file",
    )
    args = parser.parse_args()

    root_path = Path(args.root)
    data = collect_baseline(root_path)

    if args.format == "yaml":
        output = yaml.safe_dump(data, sort_keys=False, allow_unicode=True)
    else:
        output = json.dumps(data, indent=2, ensure_ascii=False)

    print(output)

    log_path = root_path / args.log
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text(output, encoding="utf-8")


if __name__ == "__main__":
    main()

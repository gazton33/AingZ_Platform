#!/usr/bin/env python3
"""Validate README metadata.

Checks that each provided README file contains a YAML front matter block with
required fields and ends with an OutputTemplate block.
"""

import sys
import re
from pathlib import Path

try:
    import yaml
except ImportError:
    print("pyyaml is required. install with 'pip install pyyaml'")
    sys.exit(1)

REQUIRED_FIELDS = ["CODE", "ID", "VERSION", "ROUTE", "CROSSREF", "AUTHOR", "DATE"]


def extract_front_matter(text: str):
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    fm_text = text[3:end]
    try:
        data = yaml.safe_load(fm_text)
    except Exception:
        return None
    return data


def has_output_template(text: str) -> bool:
    # Look for the heading 'OutputTemplate' near the end of file
    lines = text.strip().splitlines()
    return any(line.strip().startswith("## OutputTemplate") for line in lines[-10:])


def validate_file(path: Path) -> str:
    content = path.read_text(encoding="utf-8")
    data = extract_front_matter(content)
    if data is None:
        return f"{path}: missing or malformed YAML front matter"
    missing = [f for f in REQUIRED_FIELDS if f not in data]
    if missing:
        return f"{path}: missing fields {missing}"
    if not has_output_template(content):
        return f"{path}: missing OutputTemplate block"
    return f"{path}: OK"


def main():
    if len(sys.argv) < 2:
        print("Usage: python ops/validate_metadata.py <README paths>")
        sys.exit(1)
    for arg in sys.argv[1:]:
        path = Path(arg)
        if path.exists():
            print(validate_file(path))
        else:
            print(f"{arg}: file not found")


if __name__ == "__main__":
    main()

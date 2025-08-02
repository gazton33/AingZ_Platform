import os
import re
import sys
from pathlib import Path

PIPELINE_STAGES = {"LEGACY", "TMP", "MIG", "CORE", "BACKUP"}
ALLOWED_FILES = {"README.md", "LICENSE", ".gitignore", ".gitattributes", ".editorconfig"}
SNAKE_RE = re.compile(r"^[a-z0-9_]+(?:\.[a-z0-9_]+)?$")
EXCLUDE_DIRS = {".git", "legacy_old"}

def main() -> None:
    root = Path(__file__).resolve().parent.parent
    errors: list[str] = []
    for dirpath, dirnames, filenames in os.walk(root):
        rel_dir = Path(dirpath).relative_to(root)
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS and not d.startswith('.')]
        for d in dirnames:
            if d in PIPELINE_STAGES:
                continue
            if not SNAKE_RE.match(d):
                path = rel_dir / d if rel_dir != Path('.') else Path(d)
                errors.append(str(path))
        for f in filenames:
            if f in ALLOWED_FILES or f.startswith('README'):
                continue
            if not SNAKE_RE.match(f):
                path = rel_dir / f if rel_dir != Path('.') else Path(f)
                errors.append(str(path))
    if errors:
        print("Non-compliant names found:")
        for e in errors:
            print(f"- {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

import argparse
from pathlib import Path
import re

# Adapted from legacy_old/audit/originals/Lote_scripts/class_scan.py
#
"""Scan legacy files by class code.

Expected repository layout::

    legacy_old/
      lote_1/
        originals/  # default scanned by this script
"""

LEGACY_DIR = Path('legacy_old/lote_1/originals')


def find_class_files(directory: Path, class_code: str):
    """Return files under *directory* matching *class_code* pattern."""
    pattern = re.compile(class_code, re.IGNORECASE)
    return [
        p
        for p in directory.rglob('*')
        if p.is_file() and pattern.search(p.as_posix())
    ]


def group_by_name(paths):
    """Group paths by their file name."""
    groups = {}
    for p in paths:
        groups.setdefault(p.name, []).append(p)
    return groups


def parse_args(args=None):
    parser = argparse.ArgumentParser(
        description='Scan legacy files by class code'
    )
    parser.add_argument('class_code', help='Class code to match e.g. MTR, DOC')
    parser.add_argument(
        '-d', '--directory',
        default=str(LEGACY_DIR),
        help="Base directory to scan (default 'legacy_old/lote_1/originals/')"
    )
    parser.add_argument(
        '--duplicates',
        action='store_true',
        help='Show only duplicate file names'
    )
    return parser.parse_args(args)


def main():
    args = parse_args()
    directory = Path(args.directory)
    files = find_class_files(directory, args.class_code)
    groups = group_by_name(files)
    if args.duplicates:
        groups = {
            name: paths
            for name, paths in groups.items()
            if len(paths) > 1
        }
    for name, paths in sorted(groups.items()):
        print(name)
        for p in paths:
            print('  -', p.as_posix())


if __name__ == '__main__':
    main()

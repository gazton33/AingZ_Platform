#!/usr/bin/env python3
import pathlib
import sys

BASE = pathlib.Path(__file__).resolve().parents[1]

def main():
    mismatched = []
    for md in BASE.rglob('*.md'):
        if 'v_4_0' not in md.name:
            mismatched.append(str(md.relative_to(BASE)))
    if mismatched:
        print('Files without v_4_0 naming:')
        for m in mismatched:
            print('-', m)
        sys.exit(1)
    print('All ops markdown files follow v_4_0 naming convention.')

if __name__ == '__main__':
    main()

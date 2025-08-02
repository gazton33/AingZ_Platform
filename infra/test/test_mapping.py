from pathlib import Path
import datetime

import pytest

from scripts import mapping


def test_scan_legacy(tmp_path):
    (tmp_path / 'a.txt').write_text('')
    sub = tmp_path / 'sub'
    sub.mkdir()
    (sub / 'b.txt').write_text('')
    excl = tmp_path / 'exclude'
    excl.mkdir()
    (excl / 'c.txt').write_text('')
    result = mapping.scan_legacy(tmp_path, exclude=['exclude'])
    assert str(tmp_path / 'a.txt') in result
    assert str(sub / 'b.txt') in result
    assert all('exclude' not in p for p in result)


def test_append_mapping(tmp_path):
    registry = tmp_path / 'registry.md'
    files = ['f1.txt', 'f2.txt']
    mapping.append_mapping(files, registry, destination='DEST')
    content = registry.read_text()
    date_str = datetime.date.today().isoformat()
    assert f"## Mapeo automático ({date_str})" in content
    for f in files:
        assert f"| {f} | DEST |" in content

    # Re-run with same files should not duplicate
    mapping.append_mapping(files, registry, destination='DEST')
    content2 = registry.read_text().splitlines()
    assert content2 == content.splitlines()

import os
from pathlib import Path
import builtins

import pytest

from scripts import class_scan


def test_find_class_files(tmp_path):
    (tmp_path / 'MTR_file1.txt').write_text('a')
    (tmp_path / 'DOC_file.txt').write_text('b')
    sub = tmp_path / 'sub'
    sub.mkdir()
    (sub / 'MTR_file2.txt').write_text('c')
    result = class_scan.find_class_files(tmp_path, 'MTR')
    assert sorted(p.name for p in result) == ['MTR_file1.txt', 'MTR_file2.txt']


def test_group_by_name(tmp_path):
    file1 = tmp_path / 'a.txt'
    file1.write_text('')
    file2 = tmp_path / 'b.txt'
    file2.write_text('')
    dup = tmp_path / 'dup.txt'
    dup.write_text('')
    dup2 = tmp_path / 'sub/dup.txt'
    dup2.parent.mkdir()
    dup2.write_text('')
    result = class_scan.group_by_name([file1, file2, dup, dup2])
    assert result['dup.txt'] == [dup, dup2]
    assert result['a.txt'] == [file1]

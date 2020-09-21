# -*- coding:utf-8 -*-

"""Test gendiff module."""

import sys

from gendiff.file_loader import open_file
from gendiff.scripts.gendiff import main


def test_main(capfd):
    """Test main function."""
    sys.argv = [
        'test1',
        'tests/fixtures/before.json',
        'tests/fixtures/after.json',
    ]
    main()
    out, err = capfd.readouterr()
    test_diff = set(out[1:-1].split('\n'))
    sample_diff = set(open_file('tests/fixtures/diff.txt').split('\n'))
    assert sample_diff == test_diff
    assert err == ''
    sys.argv = [
        'test2',
        'tests/fixtures/before.yml',
        'tests/fixtures/after.yml',
    ]
    main()
    out, err = capfd.readouterr()
    test_diff = set(out[1:-1].split('\n'))
    assert sample_diff == test_diff
    assert err == ''

# -*- coding:utf-8 -*-

"""Test generate_diff module."""

from gendiff.file_loader import open_file
from gendiff.generate_diff import generate_diff, generate_diff_by_key


def test_generate_diff_by_key():
    """Test generate_diff_by_key function."""
    key = '0'
    first_value = 0
    second_value = 1
    assert generate_diff_by_key(
        key,
        first_value,
        second_value,
    ) == '  - 0: 0\n  + 0: 1'
    key = '1'
    first_value = 0
    second_value = None
    assert generate_diff_by_key(key, first_value, second_value) == '  - 1: 0'
    key = '2'
    first_value = None
    second_value = 0
    assert generate_diff_by_key(key, first_value, second_value) == '  + 2: 0'
    key = '3'
    first_value = 0
    second_value = 0
    assert generate_diff_by_key(key, first_value, second_value) == '    3: 0'


def test_generate_diff():
    """Test generate_diff function."""
    test_diff = set(open_file('tests/fixtures/diff.txt').split('\n'))
    diff = set(
        generate_diff(
            'tests/fixtures/before.json',
            'tests/fixtures/after.json',
        ).split('\n'),
    )
    assert diff == test_diff
    diff = set(
        generate_diff(
            'tests/fixtures/before.yaml',
            'tests/fixtures/after.yaml',
        ).split('\n'),
    )
    assert diff == test_diff

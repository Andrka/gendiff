# -*- coding:utf-8 -*-

"""Test plain_format module."""

from gendiff.file_loader import open_file
from gendiff.formatters.plain_format import prepare_to_plain_format

diff = open_file('tests/fixtures/diff.json')
result_path = 'tests/fixtures/diff_plain.txt'


def test_prepare_to_plain_format():
    """Test prepare_to_plain_format function."""
    sample_diff = set(open_file(result_path).split('\n'))
    test_diff = set(prepare_to_plain_format(diff).split('\n'))
    assert sample_diff == test_diff

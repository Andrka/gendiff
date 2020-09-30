# -*- coding:utf-8 -*-

"""Test json_like_format module."""

from gendiff.file_loader import open_file
from gendiff.formatters.json_like_format import prepare_to_json_like_format

diff = open_file('tests/fixtures/diff.json')
result_path = 'tests/fixtures/diff_json_like.txt'


def test_prepare_to_json_like_format():
    """Test prepare_to_json_like_format function."""
    sample_diff = set(open_file(result_path).split('\n'))
    test_diff = set(prepare_to_json_like_format(diff).split('\n'))
    assert sample_diff == test_diff

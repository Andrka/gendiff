# -*- coding:utf-8 -*-

"""Test json_like_format module."""

from gendiff.file_loader import open_file
from gendiff.formatters.json_like_format import (
    convert_to_json_veiw,
    prepare_diff_to_json_like_format,
)

diff = open_file('tests/fixtures/diff.json')
result_path = 'tests/fixtures/diff.txt'


def test_prepare_diff_to_json_like_format():
    """Test prepare_diff_to_json_like_format function."""
    sample_diff = set(open_file(result_path).split('\n'))
    test_diff = set(prepare_diff_to_json_like_format(diff).split('\n'))
    assert sample_diff == test_diff


def test_convert_to_json_veiw():
    """Test convert_to_json_veiw function."""
    sample_value = True
    assert convert_to_json_veiw(sample_value) == 'true'
    sample_value = False
    assert convert_to_json_veiw(sample_value) == 'false'
    sample_value = None
    assert convert_to_json_veiw(sample_value) == 'null'
    sample_value = 'Something'
    assert convert_to_json_veiw(sample_value) == sample_value

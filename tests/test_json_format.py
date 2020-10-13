# -*- coding:utf-8 -*-

"""Test json_format module."""

from gendiff.formatters.json_format import prepare_to_json_format


def test_prepare_to_json_format(diff_json, diff_json_txt):
    """Test prepare_to_json_format function."""
    test_diff = prepare_to_json_format(diff_json)
    assert diff_json_txt == test_diff

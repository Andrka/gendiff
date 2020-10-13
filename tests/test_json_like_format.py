# -*- coding:utf-8 -*-

"""Test json_like_format module."""

from gendiff.formatters.json_like_format import prepare_to_json_like_format


def test_prepare_to_json_like_format(diff_json, diff_json_like_txt):
    """Test prepare_to_json_like_format function."""
    test_diff = prepare_to_json_like_format(diff_json)
    assert diff_json_like_txt == test_diff

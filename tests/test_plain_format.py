# -*- coding:utf-8 -*-

"""Test plain_format module."""

from gendiff.formatters.plain_format import prepare_to_plain_format


def test_prepare_to_plain_format(diff_json, diff_plain_txt):
    """Test prepare_to_plain_format function."""
    test_diff = prepare_to_plain_format(diff_json)
    assert diff_plain_txt == test_diff

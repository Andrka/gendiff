# -*- coding:utf-8 -*-

"""Test plain module."""

from gendiff.format.plain import plain


def test_plain(diff_json, diff_plain_txt):
    """Test plain function."""
    test_diff = plain(diff_json)
    assert diff_plain_txt == test_diff

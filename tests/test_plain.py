# -*- coding:utf-8 -*-

"""Test plain module."""

from gendiff.format.plain import plain


def test_plain(diff, diff_plain_txt):
    """Test plain function."""
    test_diff = plain(diff)
    assert set(diff_plain_txt) == set(test_diff)

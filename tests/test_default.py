# -*- coding:utf-8 -*-

"""Test default module."""

from gendiff.format.default import default


def test_default(diff, diff_default_txt):
    """Test default function."""
    test_diff = default(diff)
    assert set(diff_default_txt) == set(test_diff)

# -*- coding:utf-8 -*-

"""Test default module."""

from gendiff.format.default import default


def test_default(diff_json, diff_default_txt):
    """Test default function."""
    test_diff = default(diff_json)
    assert diff_default_txt == test_diff

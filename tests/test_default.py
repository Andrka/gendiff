# -*- coding:utf-8 -*-

"""Test default module."""

from gendiff.format.default import default


def test_default(diff, diff_default_txt):
    """Test default function."""
    assert default(diff) == diff_default_txt

# -*- coding:utf-8 -*-

"""Test json module."""

from gendiff.format.json import json


def test_json(diff, diff_json_txt):
    """Test json function."""
    test_diff = json(diff)
    assert diff_json_txt == test_diff

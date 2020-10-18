# -*- coding:utf-8 -*-

"""Test json module."""

from gendiff.format.json import json


def test_json(diff, diff_json_txt):
    """Test json function."""
    assert json(diff) == diff_json_txt

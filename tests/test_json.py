# -*- coding:utf-8 -*-

"""Test json module."""

import json

import pytest

from gendiff.format.json import json as json_str


@pytest.mark.parametrize(
    'diff, output',
    [
        ('simple_diff', 'simple_output_json'),
        ('nested_diff', 'nested_output_json'),
    ],
)
def test_json(request, diff, output):
    """Test json function."""
    diff = request.getfixturevalue(diff)
    output = request.getfixturevalue(output)
    assert json.loads(json_str(diff)) == output

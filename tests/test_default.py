# -*- coding:utf-8 -*-

"""Test default module."""

import pytest

from gendiff.format.default import default


@pytest.mark.parametrize(
    'diff, output',
    [
        ('simple_diff', 'simple_output_default'),
        ('nested_diff', 'nested_output_default'),
    ],
)
def test_default(request, diff, output):
    """Test default function."""
    diff = request.getfixturevalue(diff)
    output = request.getfixturevalue(output)
    assert default(diff) == output

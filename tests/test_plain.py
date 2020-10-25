# -*- coding:utf-8 -*-

"""Test plain module."""

import pytest

from gendiff.format.plain import plain


@pytest.mark.parametrize(
    'diff, output',
    [
        ('simple_diff', 'simple_output_plain'),
        ('nested_diff', 'nested_output_plain'),
    ],
)
def test_plain(request, diff, output):
    """Test plain function."""
    diff = request.getfixturevalue(diff)
    output = request.getfixturevalue(output)
    assert plain(diff) == output

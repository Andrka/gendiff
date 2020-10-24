# -*- coding:utf-8 -*-

"""Test values module."""

import pytest

from gendiff.values import convert_to_json_value


@pytest.mark.parametrize(
    'sample_value, expected_result',
    [
        (True, 'true'),
        (False, 'false'),
        (None, 'null'),
        ('Something', 'Something'),
    ],
)
def test_convert_to_json_value(sample_value, expected_result):
    """Test convert_to_json_value function."""
    assert convert_to_json_value(sample_value) == expected_result

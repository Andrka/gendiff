# -*- coding:utf-8 -*-

"""Test converter module."""

import pytest

from gendiff.converter import convert_to_json_veiw


@pytest.mark.parametrize(
    'sample_value, expected_result',
    [
        (True, 'true'),
        (False, 'false'),
        (None, 'null'),
        ('Something', 'Something'),
    ],
)
def test_convert_to_json_veiw(sample_value, expected_result):
    """Test convert_to_json_veiw function."""
    assert convert_to_json_veiw(sample_value) == expected_result

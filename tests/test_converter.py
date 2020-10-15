# -*- coding:utf-8 -*-

"""Test converter module."""

from gendiff.format.converter import convert_to_json_veiw


def test_convert_to_json_veiw():
    """Test convert_to_json_veiw function."""
    sample_value = True
    assert convert_to_json_veiw(sample_value) == 'true'
    sample_value = False
    assert convert_to_json_veiw(sample_value) == 'false'
    sample_value = None
    assert convert_to_json_veiw(sample_value) == 'null'
    sample_value = 'Something'
    assert convert_to_json_veiw(sample_value) == sample_value

# -*- coding:utf-8 -*-

"""Test generate_diff module."""

from gendiff.file_loader import open_file
from gendiff.generate_diff import (
    convert_to_json_veiw,
    create_diff,
    generate_diff_for_print,
    prepare_diff_for_print,
)

diff = open_file('tests/fixtures/diff.json')
before_json_path = 'tests/fixtures/before.json'
after_json_path = 'tests/fixtures/after.json'
result_path = 'tests/fixtures/diff.txt'
before_yaml_path = 'tests/fixtures/before.yml'
after_yaml_path = 'tests/fixtures/after.yml'


def test_generate_diff_for_print():
    """Test generate_diff_for_print function."""
    sample_diff = set(open_file(result_path).split('\n'))
    test_diff = set(
        generate_diff_for_print(
            before_json_path,
            after_json_path,
        ).split('\n'),
    )
    assert sample_diff == test_diff
    test_diff = set(
        generate_diff_for_print(
            before_yaml_path,
            after_yaml_path,
        ).split('\n'),
    )
    assert sample_diff == test_diff


def test_create_diff():
    """Test create_diff function."""
    assert create_diff(
        open_file(before_json_path),
        open_file(after_json_path),
    ) == diff
    assert create_diff(
        open_file(before_yaml_path),
        open_file(after_yaml_path),
    ) == diff


def test_prepare_diff_for_print():
    """Test prepare_diff_for_print function."""
    sample_diff = set(open_file(result_path).split('\n'))
    test_diff = set(prepare_diff_for_print(diff).split('\n'))
    assert sample_diff == test_diff


def test_convert_to_json_veiw():
    """Test convert_to_json_veiw function."""
    sample_value = True
    assert convert_to_json_veiw(sample_value) == 'true'
    sample_value = False
    assert convert_to_json_veiw(sample_value) == 'false'
    sample_value = None
    assert convert_to_json_veiw(sample_value) == 'null'
    sample_value = 'Somthing'
    assert convert_to_json_veiw(sample_value) == sample_value

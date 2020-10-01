# -*- coding:utf-8 -*-

"""Test generate_diff module."""

from gendiff.file_loader import open_file
from gendiff.generate_diff import create_diff, generate_diff_for_print

diff = open_file('tests/fixtures/diff.json')
before_json_path = 'tests/fixtures/before.json'
after_json_path = 'tests/fixtures/after.json'
result_path_json_like = 'tests/fixtures/diff_json_like.txt'
result_path_plain = 'tests/fixtures/diff_plain.txt'
before_yaml_path = 'tests/fixtures/before.yml'
after_yaml_path = 'tests/fixtures/after.yml'


def test_generate_diff_for_print():
    """Test generate_diff_for_print function."""
    sample_diff = set(open_file(result_path_json_like).split('\n'))
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
    test_diff = set(
        generate_diff_for_print(
            before_json_path,
            after_json_path,
            'json_like',
        ).split('\n'),
    )
    assert sample_diff == test_diff
    test_diff = set(
        generate_diff_for_print(
            before_yaml_path,
            after_yaml_path,
            'json_like',
        ).split('\n'),
    )
    assert sample_diff == test_diff
    sample_diff = set(open_file(result_path_plain).split('\n'))
    test_diff = set(
        generate_diff_for_print(
            before_json_path,
            after_json_path,
            'plain',
        ).split('\n'),
    )
    assert sample_diff == test_diff
    test_diff = set(
        generate_diff_for_print(
            before_yaml_path,
            after_yaml_path,
            'plain',
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

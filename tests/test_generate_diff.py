# -*- coding:utf-8 -*-

"""Test generate_diff module."""

import pytest

from gendiff.generate_diff import create_diff, generate_diff_for_print

BEFORE_JSON_PATH = 'tests/fixtures/before.json'
AFTER_JSON_PATH = 'tests/fixtures/after.json'
BEFORE_YAML_PATH = 'tests/fixtures/before.yml'
AFTER_YAML_PATH = 'tests/fixtures/after.yml'


@pytest.mark.parametrize(
    'expected_result, before_path, after_path, output_format',
    [
        ('diff_json_like_txt', BEFORE_JSON_PATH, AFTER_JSON_PATH, None),
        ('diff_json_like_txt', BEFORE_YAML_PATH, AFTER_YAML_PATH, None),
        ('diff_json_like_txt', BEFORE_JSON_PATH, AFTER_JSON_PATH, 'json-like'),
        ('diff_json_like_txt', BEFORE_YAML_PATH, AFTER_YAML_PATH, 'json-like'),
        ('diff_plain_txt', BEFORE_JSON_PATH, AFTER_JSON_PATH, 'plain'),
        ('diff_plain_txt', BEFORE_YAML_PATH, AFTER_YAML_PATH, 'plain'),
        ('diff_json_txt', BEFORE_JSON_PATH, AFTER_JSON_PATH, 'json'),
        ('diff_json_txt', BEFORE_YAML_PATH, AFTER_YAML_PATH, 'json'),
    ],
)
def test_generate_diff_for_print(
    request,
    expected_result,
    before_path,
    after_path,
    output_format,
):
    """Test generate_diff_for_print function."""
    sample_diff = set(request.getfixturevalue(expected_result).split('\n'))
    test_diff = set(
        generate_diff_for_print(
            before_path,
            after_path,
            output_format,
        ).split('\n'),
    )
    assert sample_diff == test_diff


def test_create_diff(
    diff_json,
    before_json,
    after_json,
    before_yml,
    after_yml,
):
    """Test create_diff function."""
    assert create_diff(
        before_json,
        after_json,
    ) == diff_json
    assert create_diff(
        before_yml,
        after_yml,
    ) == diff_json

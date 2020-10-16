# -*- coding:utf-8 -*-

"""Test diff module."""

import pytest

from gendiff import format
from gendiff.diff import create_diff, generate_diff_for_print

BEFORE_JSON_PATH = 'tests/fixtures/before.json'
AFTER_JSON_PATH = 'tests/fixtures/after.json'
BEFORE_YAML_PATH = 'tests/fixtures/before.yml'
AFTER_YAML_PATH = 'tests/fixtures/after.yml'


@pytest.mark.parametrize(
    'expected_result, before_path, after_path, output_format',
    [
        ('diff_default_txt', BEFORE_JSON_PATH, AFTER_JSON_PATH, None),
        ('diff_default_txt', BEFORE_YAML_PATH, AFTER_YAML_PATH, None),
        ('diff_default_txt', BEFORE_JSON_PATH, AFTER_JSON_PATH, format.DEFAULT),
        ('diff_default_txt', BEFORE_YAML_PATH, AFTER_YAML_PATH, format.DEFAULT),
        ('diff_plain_txt', BEFORE_JSON_PATH, AFTER_JSON_PATH, format.PLAIN),
        ('diff_plain_txt', BEFORE_YAML_PATH, AFTER_YAML_PATH, format.PLAIN),
        ('diff_json_txt', BEFORE_JSON_PATH, AFTER_JSON_PATH, format.JSON),
        ('diff_json_txt', BEFORE_YAML_PATH, AFTER_YAML_PATH, format.JSON),
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


@pytest.mark.parametrize(
    'old, new',
    [
        ('before_json', 'after_json'),
        ('before_yml', 'after_yml'),
    ],
)
def test_create_diff(diff, request, old, new):
    """Test create_diff function."""
    assert create_diff(
        request.getfixturevalue(old),
        request.getfixturevalue(new),
    ) == diff

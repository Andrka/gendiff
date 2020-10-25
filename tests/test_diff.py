# -*- coding:utf-8 -*-

"""Test diff module."""

import json

import pytest

from gendiff import format
from gendiff.diff import compare, printable

SIMPLE_OLD_JSON = 'tests/fixtures/simple_input_old.json'
SIMPLE_NEW_JSON = 'tests/fixtures/simple_input_new.json'
SIMPLE_OLD_YAML = 'tests/fixtures/simple_input_old.yml'
SIMPLE_NEW_YAML = 'tests/fixtures/simple_input_new.yml'
NESTED_OLD_JSON = 'tests/fixtures/nested_input_old.json'
NESTED_NEW_JSON = 'tests/fixtures/nested_input_new.json'
NESTED_OLD_YAML = 'tests/fixtures/nested_input_old.yml'
NESTED_NEW_YAML = 'tests/fixtures/nested_input_new.yml'


@pytest.mark.parametrize(
    'expected_result, old_file, new_file, output_format',
    [
        ('simple_output_default', SIMPLE_OLD_JSON, SIMPLE_NEW_JSON, format.DEFAULT),
        ('simple_output_default', SIMPLE_OLD_YAML, SIMPLE_NEW_YAML, format.DEFAULT),
        ('simple_output_plain', SIMPLE_OLD_JSON, SIMPLE_NEW_JSON, format.PLAIN),
        ('simple_output_plain', SIMPLE_OLD_YAML, SIMPLE_NEW_YAML, format.PLAIN),
        ('simple_output_json', SIMPLE_OLD_JSON, SIMPLE_NEW_JSON, format.JSON),
        ('simple_output_json', SIMPLE_OLD_YAML, SIMPLE_NEW_YAML, format.JSON),
        ('nested_output_default', NESTED_OLD_JSON, NESTED_NEW_JSON, format.DEFAULT),
        ('nested_output_default', NESTED_OLD_YAML, NESTED_NEW_YAML, format.DEFAULT),
        ('nested_output_plain', NESTED_OLD_JSON, NESTED_NEW_JSON, format.PLAIN),
        ('nested_output_plain', NESTED_OLD_YAML, NESTED_NEW_YAML, format.PLAIN),
        ('nested_output_json', NESTED_OLD_JSON, NESTED_NEW_JSON, format.JSON),
        ('nested_output_json', NESTED_OLD_YAML, NESTED_NEW_YAML, format.JSON),
    ],
)
def test_printable_with_format(
    request,
    expected_result,
    old_file,
    new_file,
    output_format,
):
    """Test printable function with output format."""
    expected_diff = request.getfixturevalue(expected_result)
    test_diff = printable(
        old_file,
        new_file,
        output_format,
    )
    if output_format == format.JSON:
        test_diff = json.loads(test_diff)
    assert test_diff == expected_diff


@pytest.mark.parametrize(
    'expected_result, old_file, new_file',
    [
        ('simple_output_default', SIMPLE_OLD_JSON, SIMPLE_NEW_JSON),
        ('simple_output_default', SIMPLE_OLD_YAML, SIMPLE_NEW_YAML),
        ('nested_output_default', NESTED_OLD_JSON, NESTED_NEW_JSON),
        ('nested_output_default', NESTED_OLD_YAML, NESTED_NEW_YAML),
    ],
)
def test_printable_without_format(
    request,
    expected_result,
    old_file,
    new_file,
):
    """Test printable function without output format."""
    expected_diff = request.getfixturevalue(expected_result)
    test_diff = printable(
        old_file,
        new_file,
    )
    assert test_diff == expected_diff


@pytest.mark.parametrize(
    'expected_result, old_file, new_file',
    [
        ('simple_diff', 'simple_input_old_json', 'simple_input_new_json'),
        ('simple_diff', 'simple_input_old_yaml', 'simple_input_new_yml'),
        ('nested_diff', 'nested_input_old_json', 'nested_input_new_json'),
        ('nested_diff', 'nested_input_old_yaml', 'nested_input_new_yml'),
    ],
)
def test_compare(request, expected_result, old_file, new_file):
    """Test compare function."""
    assert compare(
        request.getfixturevalue(old_file),
        request.getfixturevalue(new_file),
    ) == request.getfixturevalue(expected_result)

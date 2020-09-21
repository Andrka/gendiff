# -*- coding:utf-8 -*-

"""Test file_loader module."""

from gendiff.file_loader import (
    open_file,
    open_json_file,
    open_txt_file,
    open_yaml_file,
)

before = {
    'common': {
        'setting1': 'Value 1',
        'setting2': 200,
        'setting3': True,
        'setting6': {
            'key': 'value',
        },
    },
    'group1': {
        'baz': 'bas',
        'foo': 'bar',
    },
    'group2': {
        'abc': 12345,
    },
}
after = {
    'common': {
        'setting1': 'Value 1',
        'setting3': True,
        'setting4': 'blah blah',
        'setting5': {
            'key5': 'value5',
        },
    },
    'group1': {
        'foo': 'bar',
        'baz': 'bars',
    },
    'group3': {
        'fee': 100500,
    },
}
diff_in_str = """{\n    common: {
        setting1: Value 1\n      - setting2: 200\n        setting3: true
      - setting6: {\n            key: value\n        }
      + setting4: blah blah\n      + setting5: {\n            key5: value5
        }\n    }\n    group1: {\n      + baz: bars\n      - baz: bas
        foo: bar\n    }\n  - group2: {\n        abc: 12345\n    }
  + group3: {\n        fee: 100500\n    }\n}"""
before_json_path = 'tests/fixtures/before.json'
after_json_path = 'tests/fixtures/after.json'
result_path = 'tests/fixtures/diff.txt'
before_yaml_path = 'tests/fixtures/before.yml'
after_yaml_path = 'tests/fixtures/after.yml'


def test_open_file():
    """Test open_file function."""
    assert open_file(before_json_path) == before
    assert open_file(after_json_path) == after
    assert open_file(result_path) == diff_in_str
    assert open_file(before_yaml_path) == before
    assert open_file(after_yaml_path) == after


def test_open_json_file():
    """Test open_json_file function."""
    assert open_json_file(before_json_path) == before
    assert open_json_file(after_json_path) == after


def test_open_txt_file():
    """Test open_txt_file function."""
    assert open_txt_file(result_path) == diff_in_str


def test_open_yaml_file():
    """Test open_yaml_file function."""
    assert open_yaml_file(before_yaml_path) == before
    assert open_yaml_file(after_yaml_path) == after

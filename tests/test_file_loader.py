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
            'doge': {
                'wow': 'too much',
            },
        },
    },
    'group1': {
        'baz': 'bas',
        'foo': 'bar',
        'nest': {
            'key': 'value',
        },
    },
    'group2': {
        'abc': 12345,
        'deep': {
            'id': 45,
        },
    },
}
after = {
    'common': {
        'follow': False,
        'setting1': 'Value 1',
        'setting3': {
            'key': 'value',
        },
        'setting4': 'blah blah',
        'setting5': {
            'key5': 'value5',
        },
        'setting6': {
            'key': 'value',
            'ops': 'vops',
            'doge': {
                'wow': 'so much',
            },
        },
    },
    'group1': {
        'foo': 'bar',
        'baz': 'bars',
        'nest': 'str',
    },
    'group3': {
        'fee': 100500,
        'deep': {
            'id': {
                'number': 45,
            },
        },
    },
}
diff_in_str = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: {
            key: value
        }
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: too much
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        fee: 100500
        deep: {
            id: {
                number: 45
            }
        }
    }
}"""
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

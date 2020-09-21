# -*- coding:utf-8 -*-

"""Test generate_diff module."""

from gendiff.file_loader import open_file
from gendiff.generate_diff import (
    ADD,
    CHANGED,
    CHILDREN,
    DEL,
    DIFF,
    NESTED,
    NO,
    OLD_VALUE,
    VALUE,
    create_diff,
    generate_diff,
    generate_diff_by_key,
    prepare_diff_for_print,
)

diff = {'common': {
    DIFF: NESTED,
    OLD_VALUE: None,
    VALUE: None,
    CHILDREN: {
        'setting1': {
            DIFF: NO,
            OLD_VALUE: None,
            VALUE: 'Value 1',
            CHILDREN: None,
        },
        'setting2': {
            DIFF: DEL,
            OLD_VALUE: 200,
            VALUE: None,
            CHILDREN: None,
        },
        'setting3': {
            DIFF: NO,
            OLD_VALUE: None,
            VALUE: True,
            CHILDREN: None,
        },
        'setting6': {
            DIFF: DEL,
            OLD_VALUE: {'key': 'value'},
            VALUE: None,
            CHILDREN: None,
        },
        'setting4': {
            DIFF: ADD,
            OLD_VALUE: None,
            VALUE: 'blah blah',
            CHILDREN: None,
        },
        'setting5': {
            DIFF: ADD,
            OLD_VALUE: None,
            VALUE: {'key5': 'value5'},
            CHILDREN: None,
        },
    },
}, 'group1': {
    DIFF: NESTED,
    OLD_VALUE: None,
    VALUE: None,
    CHILDREN: {
        'baz': {
            DIFF: CHANGED,
            OLD_VALUE: 'bas',
            VALUE: 'bars',
            CHILDREN: None,
        },
        'foo': {
            DIFF: NO,
            OLD_VALUE: None,
            VALUE: 'bar',
            CHILDREN: None,
        },
    },
}, 'group2': {
    DIFF: DEL,
    OLD_VALUE: {'abc': 12345},
    VALUE: None,
    CHILDREN: None,
}, 'group3': {
    DIFF: ADD,
    OLD_VALUE: None,
    VALUE: {'fee': 100500},
    CHILDREN: None,
},
}
before_json_path = 'tests/fixtures/before.json'
after_json_path = 'tests/fixtures/after.json'
result_path = 'tests/fixtures/diff.txt'
before_yaml_path = 'tests/fixtures/before.yml'
after_yaml_path = 'tests/fixtures/after.yml'


def test_generate_diff():
    """Test generate_diff function."""
    sample_diff = set(open_file(result_path).split('\n'))
    test_diff = set(
        generate_diff(
            before_json_path,
            after_json_path,
        ).split('\n'),
    )
    assert sample_diff == test_diff
    test_diff = set(
        generate_diff(
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


def test_generate_diff_by_key():
    """Test generate_diff_by_key function."""
    first_value = 0
    second_value = 1
    assert generate_diff_by_key(
        first_value,
        second_value,
    ) == {
        DIFF: CHANGED,
        OLD_VALUE: 0,
        VALUE: 1,
        CHILDREN: None,
    }
    first_value = 0
    second_value = None
    assert generate_diff_by_key(
        first_value,
        second_value,
    ) == {
        DIFF: DEL,
        OLD_VALUE: 0,
        VALUE: None,
        CHILDREN: None,
    }
    first_value = None
    second_value = 0
    assert generate_diff_by_key(
        first_value,
        second_value,
    ) == {
        DIFF: ADD,
        OLD_VALUE: None,
        VALUE: 0,
        CHILDREN: None,
    }
    first_value = 0
    second_value = 0
    assert generate_diff_by_key(
        first_value,
        second_value,
    ) == {
        DIFF: NO,
        OLD_VALUE: None,
        VALUE: 0,
        CHILDREN: None,
    }


def test_prepare_diff_for_print():
    """Test prepare_diff_for_print function."""
    sample_diff = set(open_file(result_path).split('\n'))
    test_diff = set(prepare_diff_for_print(diff).split('\n'))
    print('sample', open_file(result_path))
    print('test', prepare_diff_for_print(diff))
    assert sample_diff == test_diff

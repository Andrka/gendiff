# -*- coding:utf-8 -*-

"""Test file_loader module."""

from gendiff.file_loader import (
    open_file,
    open_json_file,
    open_txt_file,
    open_yaml_file,
)


def test_open_file():
    """Test open_file function."""
    assert open_file('tests/fixtures/before.json') == {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
    }
    assert open_file('tests/fixtures/after.json') == {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io",
    }
    assert open_file('tests/fixtures/diff.txt') == '''{\n  - timeout: 50
  + timeout: 20\n  - proxy: 123.234.53.22\n    host: hexlet.io
  + verbose: True\n}'''
    assert open_file('tests/fixtures/before.yaml') == {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
    }
    assert open_file('tests/fixtures/after.yaml') == {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io",
    }


def test_open_json_file():
    """Test open_json_file function."""
    assert open_json_file('tests/fixtures/before.json') == {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
    }
    assert open_json_file('tests/fixtures/after.json') == {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io",
    }


def test_open_txt_file():
    """Test open_txt_file function."""
    assert open_txt_file('tests/fixtures/diff.txt') == '''{
  - timeout: 50\n  + timeout: 20\n  - proxy: 123.234.53.22
    host: hexlet.io\n  + verbose: True\n}'''


def test_open_yaml_file():
    """Test open_yaml_file function."""
    assert open_yaml_file('tests/fixtures/before.yaml') == {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
    }
    assert open_yaml_file('tests/fixtures/after.yaml') == {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io",
    }

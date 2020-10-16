# -*- coding:utf-8 -*-

"""Define fixtures to use in tests."""

import ast
import json

import pytest
import yaml


@pytest.fixture(name='after_json')
def load_after_json() -> dict:
    """Load after.json file for tests."""
    with open('tests/fixtures/after.json', 'r') as json_file:
        json_data = json.load(json_file)
    return json_data


@pytest.fixture(name='after_yml')
def load_after_yaml() -> dict:
    """Load after.yml file for tests."""
    with open('tests/fixtures/after.yml', 'r') as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)
    return yaml_data


@pytest.fixture(name='before_json')
def load_before_json() -> dict:
    """Load before.json file for tests."""
    with open('tests/fixtures/before.json', 'r') as json_file:
        json_data = json.load(json_file)
    return json_data


@pytest.fixture(name='before_yml')
def load_before_yaml() -> dict:
    """Load before.yml file for tests."""
    with open('tests/fixtures/before.yml', 'r') as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)
    return yaml_data


@pytest.fixture(name='diff_default_txt')
def load_diff_default_txt() -> str:
    """Load diff_default.txt file for tests."""
    with open('tests/fixtures/diff_default.txt', 'r') as txt_file:
        txt_data = txt_file.read()
    return txt_data


@pytest.fixture(name='diff_json_txt')
def load_diff_json_txt() -> str:
    """Load diff_json.txt file for tests."""
    with open('tests/fixtures/diff_json.txt', 'r') as txt_file:
        txt_data = txt_file.read()
    return txt_data


@pytest.fixture(name='diff_plain_txt')
def load_diff_plain_txt() -> str:
    """Load diff_plain.txt file for tests."""
    with open('tests/fixtures/diff_plain.txt', 'r') as txt_file:
        txt_data = txt_file.read()
    return txt_data


@pytest.fixture(name='diff')
def load_diff() -> dict:
    """Load diff.txt file for tests."""
    with open('tests/fixtures/diff.txt', 'r') as txt_file:
        txt_data = txt_file.read()
    return ast.literal_eval(txt_data)

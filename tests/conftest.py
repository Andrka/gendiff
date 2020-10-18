# -*- coding:utf-8 -*-

"""Define fixtures to use in tests."""

import ast
import json

import pytest
import yaml


@pytest.fixture(name='new_json')
def load_new_json() -> dict:
    """Load new.json file for tests."""
    with open('tests/fixtures/new.json', 'r') as json_file:
        json_data = json.load(json_file)
    return json_data


@pytest.fixture(name='new_yml')
def load_new_yaml() -> dict:
    """Load new.yml file for tests."""
    with open('tests/fixtures/new.yml', 'r') as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)
    return yaml_data


@pytest.fixture(name='old_json')
def load_old_json() -> dict:
    """Load old.json file for tests."""
    with open('tests/fixtures/old.json', 'r') as json_file:
        json_data = json.load(json_file)
    return json_data


@pytest.fixture(name='old_yml')
def load_old_yaml() -> dict:
    """Load old.yml file for tests."""
    with open('tests/fixtures/old.yml', 'r') as yaml_file:
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

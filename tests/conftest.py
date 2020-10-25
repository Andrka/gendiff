# -*- coding:utf-8 -*-

"""Define fixtures to use in tests."""

import ast
import json

import pytest
import yaml


@pytest.fixture(name='simple_input_new_json')
def load_simple_input_new_json() -> dict:
    """Load simple_input_new.json file for tests."""
    with open('tests/fixtures/simple_input_new.json', 'r') as json_file:
        json_data = json.load(json_file)
    return json_data


@pytest.fixture(name='nested_input_new_json')
def load_nested_input_new_json() -> dict:
    """Load nested_input_new.json file for tests."""
    with open('tests/fixtures/nested_input_new.json', 'r') as json_file:
        json_data = json.load(json_file)
    return json_data


@pytest.fixture(name='simple_input_new_yml')
def load_simple_input_new_yml() -> dict:
    """Load simple_input_new.yml file for tests."""
    with open('tests/fixtures/simple_input_new.yml', 'r') as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)
    return yaml_data


@pytest.fixture(name='nested_input_new_yml')
def load_nested_input_new_yml() -> dict:
    """Load nested_input_new.yml file for tests."""
    with open('tests/fixtures/nested_input_new.yml', 'r') as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)
    return yaml_data


@pytest.fixture(name='simple_input_old_json')
def load_simple_input_old_json() -> dict:
    """Load simple_input_old.json file for tests."""
    with open('tests/fixtures/simple_input_old.json', 'r') as json_file:
        json_data = json.load(json_file)
    return json_data


@pytest.fixture(name='nested_input_old_json')
def load_nested_input_old_json() -> dict:
    """Load nested_input_old.json file for tests."""
    with open('tests/fixtures/nested_input_old.json', 'r') as json_file:
        json_data = json.load(json_file)
    return json_data


@pytest.fixture(name='simple_input_old_yaml')
def load_simple_input_old_yaml() -> dict:
    """Load simple_input_old.yml file for tests."""
    with open('tests/fixtures/simple_input_old.yml', 'r') as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)
    return yaml_data


@pytest.fixture(name='nested_input_old_yaml')
def load_nested_input_old_yaml() -> dict:
    """Load nested_input_old.yml file for tests."""
    with open('tests/fixtures/nested_input_old.yml', 'r') as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)
    return yaml_data


@pytest.fixture(name='simple_output_default')
def load_simple_output_default() -> str:
    """Load simple_output_default.txt file for tests."""
    with open('tests/fixtures/simple_output_default.txt', 'r') as txt_file:
        txt_data = txt_file.read()
    return txt_data


@pytest.fixture(name='nested_output_default')
def load_nested_output_default() -> str:
    """Load nested_output_default.txt file for tests."""
    with open('tests/fixtures/nested_output_default.txt', 'r') as txt_file:
        txt_data = txt_file.read()
    return txt_data


@pytest.fixture(name='simple_output_json')
def load_simple_output_json() -> dict:
    """Load simple_output_json.json file for tests."""
    with open('tests/fixtures/simple_output_json.json', 'r') as json_file:
        json_data = json.load(json_file)
    return json_data


@pytest.fixture(name='nested_output_json')
def load_nested_output_json() -> dict:
    """Load nested_output_json.json file for tests."""
    with open('tests/fixtures/nested_output_json.json', 'r') as json_file:
        json_data = json.load(json_file)
    return json_data


@pytest.fixture(name='simple_output_plain')
def load_simple_output_plain() -> str:
    """Load simple_output_plain.txt file for tests."""
    with open('tests/fixtures/simple_output_plain.txt', 'r') as txt_file:
        txt_data = txt_file.read()
    return txt_data


@pytest.fixture(name='nested_output_plain')
def load_nested_output_plain() -> str:
    """Load nested_output_plain.txt file for tests."""
    with open('tests/fixtures/nested_output_plain.txt', 'r') as txt_file:
        txt_data = txt_file.read()
    return txt_data


@pytest.fixture(name='simple_diff')
def load_simple_diff() -> dict:
    """Load simple_diff.txt file for tests."""
    with open('tests/fixtures/simple_diff.txt', 'r') as txt_file:
        txt_data = txt_file.read()
    return ast.literal_eval(txt_data)


@pytest.fixture(name='nested_diff')
def load_nested_diff() -> dict:
    """Load nested_diff.txt file for tests."""
    with open('tests/fixtures/nested_diff.txt', 'r') as txt_file:
        txt_data = txt_file.read()
    return ast.literal_eval(txt_data)

# -*- coding:utf-8 -*-

"""Open data files."""

import json

import yaml


def open_file(path_to_file: str):
    """Check extension and open file."""
    file_types = {
        'json': open_json_file,
        'txt': open_txt_file,
        'yml': open_yaml_file,
    }
    file_extension = path_to_file.split('.')[-1]
    return file_types[file_extension](path_to_file)


def open_json_file(path_to_file: str) -> dict:
    """Open json file."""
    with open('{0}'.format(path_to_file), 'r') as json_file:
        data_from_json_file = json.load(json_file)
    return data_from_json_file


def open_txt_file(path_to_file: str) -> str:
    """Open txt file."""
    with open('{0}'.format(path_to_file), 'r') as txt_file:
        data_from_txt_file = txt_file.read()
    return data_from_txt_file


def open_yaml_file(path_to_file: str) -> dict:
    """Open yaml file."""
    with open('{0}'.format(path_to_file), 'r') as yaml_file:
        data_from_yaml_file = yaml.safe_load(yaml_file)
    return data_from_yaml_file

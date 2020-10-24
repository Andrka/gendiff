# -*- coding:utf-8 -*-

"""Load data files."""

import json
import os

import yaml

YAML = ('.yml', '.yaml')
JSON = '.json'


def load(path_to_file: str) -> dict:
    """Check extension and load file.

    Raises:
        ValueError: unsupported file type.

    """
    _, file_extension = os.path.splitext(path_to_file)
    extension = file_extension.lower()
    with open(path_to_file, 'r') as data_file:
        if extension in YAML:
            load_data = yaml.safe_load(data_file)
        elif extension == JSON:
            load_data = json.load(data_file)
        else:
            raise ValueError('Unsupported file type!')
    return load_data

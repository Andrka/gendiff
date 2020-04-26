# -*- coding:utf-8 -*-

"""Realize command line interface."""

import json


def print_result(diff_result: str):
    """Print taken result."""
    print('\n', diff_result, sep='')


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

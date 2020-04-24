# -*- coding:utf-8 -*-

"""Realize command line interface."""

import json


def print_result(diff_result: str):
    """Print taken result."""
    print('\n', diff_result, sep='')  # noqa: WPS421


def open_json(path_to_file: str) -> dict:
    """Open json file."""
    return json.load(open(path_to_file))  # noqa: WPS515

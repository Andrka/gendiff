# -*- coding:utf-8 -*-

"""Generate json text diff between two files."""

import json as json_load


def json(diff_dict: dict) -> str:
    """Convert givven diff to json text format."""
    return json_load.dumps(diff_dict, sort_keys=True, indent=4)

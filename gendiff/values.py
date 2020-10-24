# -*- coding:utf-8 -*-

"""Convert given python value to json value."""


def convert_to_json_value(value) -> str:
    """Convert given python value to json value."""
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    return value

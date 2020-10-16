# -*- coding:utf-8 -*-

"""Convert given python value to json veiw."""


def convert_to_json_veiw(value) -> str:  # noqa: WPS110
    """Convert given python value to json veiw."""
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    return value

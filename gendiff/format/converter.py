# -*- coding:utf-8 -*-

"""Convert given python value to json veiw."""


def convert_to_json_veiw(key_value) -> str:
    """Convert given python value to json veiw."""
    transformations = {
        True: 'true',
        False: 'false',
        None: 'null',
    }
    transformation = transformations.get(key_value)
    if (transformation):
        return transformation
    return key_value

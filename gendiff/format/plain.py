# -*- coding:utf-8 -*-

"""Generate plain text diff between two files."""

from gendiff import diff
from gendiff.converter import convert_to_json_veiw

STATUS = {  # noqa: WPS407
    diff.ADDED: 'added',
    diff.DELETED: 'removed',
    diff.CHANGED: 'updated',
}


def plain(diff_dict: dict, path_to_root: str = ''):  # noqa: WPS210, WPS231
    """Convert given diff to plain text format."""
    result = []
    for key, (status, value) in sorted(diff_dict.items()):  # noqa: WPS405, WPS414, E501
        if status == diff.NESTED:
            result.append(
                plain(value, '{0}{1}.'.format(path_to_root, key)),
            )
        elif status in STATUS:
            result.append(
                "Property '{0}{1}' was {2}".format(
                    path_to_root,
                    key,
                    STATUS[status],  # noqa: WPS529
                ),
            )
            if status == diff.CHANGED:
                old_value, new_value = value
                result[-1] = '{0}. From {1} to {2}'.format(
                    result[-1],
                    convert_to_string_veiw(old_value),
                    convert_to_string_veiw(new_value),
                )
            elif status == diff.ADDED:
                result[-1] = '{0} with value: {1}'.format(
                    result[-1],
                    convert_to_string_veiw(value),
                )
    return '\n'.join(result)


def convert_to_string_veiw(value) -> str:
    """Convert given value to string view."""
    if isinstance(value, dict):
        return '[complex value]'
    elif not isinstance(value, bool):
        return "'{0}'".format(convert_to_json_veiw(value))
    return convert_to_json_veiw(value)

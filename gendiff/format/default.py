# -*- coding:utf-8 -*-

"""Generate json-like text diff between two files."""

from gendiff import diff, format
from gendiff.converter import convert_to_json_veiw


def default(  # noqa: WPS231
    diff_dict: dict,
    level_of_indent: int = 0,
) -> str:
    """Convert given diff to json-like text format."""
    diff_in_str = '{0}\n'.format('{')
    for key, key_parameter in diff_dict.items():
        if isinstance(key_parameter, tuple):
            if key_parameter[0] == diff.DELETED:
                diff_in_str = '{0}{1}  - {2}: {3}\n'.format(
                    diff_in_str,
                    format.INDENT * level_of_indent,  # noqa: WPS204
                    key,
                    default(  # noqa: WPS204
                        key_parameter[1],
                        level_of_indent + 1,  # noqa: WPS204
                    ) if isinstance(
                        key_parameter[1],  # noqa: WPS204
                        dict,
                    ) else convert_to_json_veiw(key_parameter[1]),
                )
                continue
            if key_parameter[0] == diff.ADDED:
                diff_in_str = '{0}{1}  + {2}: {3}\n'.format(
                    diff_in_str,
                    format.INDENT * level_of_indent,
                    key,
                    default(
                        key_parameter[1],
                        level_of_indent + 1,
                    ) if isinstance(
                        key_parameter[1],
                        dict,
                    ) else convert_to_json_veiw(key_parameter[1]),
                )
                continue
            if key_parameter[0] == diff.SAME:
                diff_in_str = '{0}{1}    {2}: {3}\n'.format(
                    diff_in_str,
                    format.INDENT * level_of_indent,
                    key,
                    default(
                        key_parameter[1],
                        level_of_indent + 1,
                    ) if isinstance(
                        key_parameter[1],
                        dict,
                    ) else convert_to_json_veiw(key_parameter[1]),
                )
                continue
            if key_parameter[0] == diff.CHANGED:
                diff_in_str = '{0}{1}  - {2}: {3}\n{4}  + {5}: {6}\n'.format(
                    diff_in_str,
                    format.INDENT * level_of_indent,
                    key,
                    default(
                        key_parameter[1][0],
                        level_of_indent + 1,
                    ) if isinstance(
                        key_parameter[1][0],
                        dict,
                    ) else convert_to_json_veiw(key_parameter[1][0]),
                    format.INDENT * level_of_indent,
                    key,
                    default(
                        key_parameter[1][1],
                        level_of_indent + 1,
                    ) if isinstance(
                        key_parameter[1][1],
                        dict,
                    ) else convert_to_json_veiw(key_parameter[1][1]),
                )
                continue
            diff_in_str = '{0}{1}    {2}: {3}\n'.format(
                diff_in_str,
                format.INDENT * level_of_indent,
                key,
                default(
                    key_parameter[1],
                    level_of_indent + 1,
                ),
            )
        else:
            diff_in_str = '{0}{1}    {2}: {3}\n'.format(
                diff_in_str,
                format.INDENT * level_of_indent,
                key,
                default(
                    key_parameter,
                    level_of_indent + 1,
                ) if isinstance(
                    key_parameter,
                    dict,
                ) else convert_to_json_veiw(key_parameter),
            )
    return '{0}{1}{2}'.format(
        diff_in_str,
        format.INDENT * level_of_indent,
        '}',
    )

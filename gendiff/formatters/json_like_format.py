# -*- coding:utf-8 -*-

"""Generate json-like text diff between two files."""

from gendiff.constants import ADDED, CHANGED, DELETED, INDENT, SAME
from gendiff.formatters.converter import convert_to_json_veiw


def prepare_to_json_like_format(  # noqa: WPS231
    diff: dict,
    level_of_indent: int = 0,
) -> str:
    """Convert given diff to json-like text format."""
    diff_in_str = '{0}\n'.format('{')
    for key, key_parameter in diff.items():
        if isinstance(key_parameter, list):
            if key_parameter[0] == DELETED:
                diff_in_str = '{0}{1}  - {2}: {3}\n'.format(
                    diff_in_str,
                    INDENT * level_of_indent,  # noqa: WPS204
                    key,
                    prepare_to_json_like_format(  # noqa: WPS204
                        key_parameter[1],
                        level_of_indent + 1,  # noqa: WPS204
                    ) if isinstance(
                        key_parameter[1],  # noqa: WPS204
                        dict,
                    ) else convert_to_json_veiw(key_parameter[1]),
                )
                continue
            if key_parameter[0] == ADDED:
                diff_in_str = '{0}{1}  + {2}: {3}\n'.format(
                    diff_in_str,
                    INDENT * level_of_indent,
                    key,
                    prepare_to_json_like_format(
                        key_parameter[1],
                        level_of_indent + 1,
                    ) if isinstance(
                        key_parameter[1],
                        dict,
                    ) else convert_to_json_veiw(key_parameter[1]),
                )
                continue
            if key_parameter[0] == SAME:
                diff_in_str = '{0}{1}    {2}: {3}\n'.format(
                    diff_in_str,
                    INDENT * level_of_indent,
                    key,
                    prepare_to_json_like_format(
                        key_parameter[1],
                        level_of_indent + 1,
                    ) if isinstance(
                        key_parameter[1],
                        dict,
                    ) else convert_to_json_veiw(key_parameter[1]),
                )
                continue
            if key_parameter[0] == CHANGED:
                diff_in_str = '{0}{1}  - {2}: {3}\n{4}  + {5}: {6}\n'.format(
                    diff_in_str,
                    INDENT * level_of_indent,
                    key,
                    prepare_to_json_like_format(
                        key_parameter[1],
                        level_of_indent + 1,
                    ) if isinstance(
                        key_parameter[1],
                        dict,
                    ) else convert_to_json_veiw(key_parameter[1]),
                    INDENT * level_of_indent,
                    key,
                    prepare_to_json_like_format(
                        key_parameter[2],
                        level_of_indent + 1,
                    ) if isinstance(
                        key_parameter[2],
                        dict,
                    ) else convert_to_json_veiw(key_parameter[2]),
                )
                continue
            diff_in_str = '{0}{1}    {2}: {3}\n'.format(
                diff_in_str,
                INDENT * level_of_indent,
                key,
                prepare_to_json_like_format(
                    key_parameter[1],
                    level_of_indent + 1,
                ),
            )
        else:
            diff_in_str = '{0}{1}    {2}: {3}\n'.format(
                diff_in_str,
                INDENT * level_of_indent,
                key,
                prepare_to_json_like_format(
                    key_parameter,
                    level_of_indent + 1,
                ) if isinstance(
                    key_parameter,
                    dict,
                ) else convert_to_json_veiw(key_parameter),
            )
    return '{0}{1}{2}'.format(diff_in_str, INDENT * level_of_indent, '}')

# -*- coding:utf-8 -*-

"""Generate json text diff between two files."""

from gendiff.constants import ADDED, CHANGED, DELETED, INDENT, NESTED, SAME
from gendiff.formatters.converter import convert_to_json_veiw


def prepare_to_json_format(  # noqa: WPS231, WPS210
    diff: dict,
    level_of_indent: int = 0,
) -> str:
    """Convert givven diff to json text format."""
    diff_in_str = '{0}\n'.format('{')
    for key, key_parameter in diff.items():
        if isinstance(key_parameter, list):
            if key_parameter[0] in {DELETED, ADDED, SAME, NESTED}:
                current_value = key_parameter[1]
                if isinstance(current_value, str):
                    current_value = '"{0}"'.format(current_value)
                diff_in_str = (
                    '{0}{1}    "{2}": {3}\n{4}"type": '
                    '"{5}",\n{6}"value": {7},\n{8}{9},\n'  # noqa: WPS326
                ).format(
                    diff_in_str,
                    INDENT * level_of_indent,
                    key,
                    '{',
                    INDENT * (level_of_indent + 2),  # noqa: WPS204
                    key_parameter[0],
                    INDENT * (level_of_indent + 2),
                    prepare_to_json_format(
                        current_value,
                        level_of_indent + 2,
                    ) if isinstance(
                        current_value,  # noqa: WPS204
                        dict,
                    ) else convert_to_json_veiw(current_value),
                    INDENT * (level_of_indent + 1),
                    '}',
                )
                continue
            if key_parameter[0] == CHANGED:
                new_value = key_parameter[2]
                if isinstance(new_value, str):
                    new_value = '"{0}"'.format(new_value)
                old_value = key_parameter[1]
                if isinstance(old_value, str):
                    old_value = '"{0}"'.format(old_value)
                diff_in_str = (
                    '{0}{1}    "{2}": {3}\n{4}"type": "{5}",\n{6}'
                    '"value": {7}\n{8}"old": '  # noqa: WPS326
                    '{9},\n{10}"new": {11},\n{12}{13},\n{14}{15},\n'
                ).format(
                    diff_in_str,
                    INDENT * level_of_indent,
                    key,
                    '{',
                    INDENT * (level_of_indent + 2),
                    key_parameter[0],
                    INDENT * (level_of_indent + 2),
                    '{',
                    INDENT * (level_of_indent + 3),
                    prepare_to_json_format(
                        old_value,
                        level_of_indent + 3,
                    ) if isinstance(
                        old_value,
                        dict,
                    ) else convert_to_json_veiw(old_value),
                    INDENT * (level_of_indent + 3),
                    prepare_to_json_format(
                        new_value,
                        level_of_indent + 3,
                    ) if isinstance(
                        new_value,
                        dict,
                    ) else convert_to_json_veiw(new_value),
                    INDENT * (level_of_indent + 2),
                    '}',
                    INDENT * (level_of_indent + 1),
                    '}',
                )
                continue
        else:
            current_value = key_parameter
            if isinstance(current_value, str):
                current_value = '"{0}"'.format(current_value)
            diff_in_str = '{0}{1}    "{2}": {3},\n'.format(
                diff_in_str,
                INDENT * level_of_indent,
                key,
                prepare_to_json_format(
                    current_value,
                    level_of_indent + 1,
                ) if isinstance(
                    current_value,
                    dict,
                ) else convert_to_json_veiw(current_value),
            )
    return '{0}{1}{2}'.format(diff_in_str, INDENT * level_of_indent, '}')

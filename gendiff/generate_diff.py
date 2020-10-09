# -*- coding:utf-8 -*-

"""Find diff."""

from gendiff.constants import ADDED, CHANGED, DELETED, NESTED, SAME
from gendiff.file_loader import open_file
from gendiff.formatters.json_format import prepare_to_json_format
from gendiff.formatters.json_like_format import prepare_to_json_like_format
from gendiff.formatters.plain_format import prepare_to_plain_format


def generate_diff_for_print(
    path_to_first_file: str,
    path_to_second_file: str,
    print_format: str = 'json_like',
) -> str:
    """Generate and return diff between two files."""
    first_file = open_file(path_to_first_file)
    second_file = open_file(path_to_second_file)
    diff = create_diff(first_file, second_file)
    if print_format == 'plain':
        return prepare_to_plain_format(diff)
    if print_format == 'json':
        return prepare_to_json_format(diff)
    return prepare_to_json_like_format(diff)


def create_diff(first_file: dict, second_file: dict) -> dict:  # noqa: WPS210
    """Create dict with diff between two files."""
    diff = {}
    common_keys = first_file.keys() & second_file.keys()
    deleted_keys = first_file.keys() - second_file.keys()
    added_keys = second_file.keys() - first_file.keys()
    for common_key in common_keys:
        first_file_value = first_file.get(common_key)
        second_file_value = second_file.get(common_key)
        if first_file_value == second_file_value:
            diff[common_key] = [SAME, first_file_value]
        elif isinstance(  # noqa: WPS337
            first_file_value,
            dict,
        ) and isinstance(
            second_file_value,
            dict,
        ):
            diff[common_key] = [NESTED, create_diff(
                first_file_value,
                second_file_value,
            )]
        else:
            diff[common_key] = [
                CHANGED,
                first_file_value,
                second_file_value,
            ]
    for deleted_key in deleted_keys:
        diff[deleted_key] = [DELETED, first_file.get(deleted_key)]
    for added_key in added_keys:
        diff[added_key] = [ADDED, second_file.get(added_key)]
    return diff

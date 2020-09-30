# -*- coding:utf-8 -*-

"""Find diff."""

from gendiff.constants import ADDED, CHANGED, DELETED, NESTED, SAME
from gendiff.file_loader import open_file
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
    return prepare_to_json_like_format(diff)


def create_diff(first_file: dict, second_file: dict) -> dict:  # noqa: WPS231
    """Create dict with diff between two files."""
    diff = {}
    keys = set(first_file.keys()) | set(second_file.keys())
    for key in keys:
        first_file_value = first_file.get(key)
        second_file_value = second_file.get(key)
        if first_file_value == second_file_value:
            diff[key] = [SAME, first_file_value]  # noqa: WPS204
            continue
        if isinstance(first_file_value, dict):
            if isinstance(second_file_value, dict):
                diff[key] = [
                    NESTED,
                    create_diff(first_file_value, second_file_value),
                ]
                continue
        if first_file_value is None:
            diff[key] = [ADDED, second_file_value]
            continue
        if second_file_value is None:
            diff[key] = [DELETED, first_file_value]
            continue
        diff[key] = [CHANGED, first_file_value, second_file_value]
    return diff

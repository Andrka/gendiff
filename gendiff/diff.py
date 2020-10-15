# -*- coding:utf-8 -*-

"""Find diff."""

from gendiff import files, format

NESTED = 'nested'
ADDED = 'added'
DELETED = 'deleted'
CHANGED = 'changed'
SAME = 'same'


def generate_diff_for_print(
    old_file: str,
    new_file: str,
    output_format: str = 'default',
) -> str:
    """Generate and return diff between two files."""
    first_file = files.load(old_file)
    second_file = files.load(new_file)
    diff = create_diff(first_file, second_file)
    if output_format == format.PLAIN:
        return format.plain(diff)
    if output_format == format.JSON:
        return format.json(diff)
    return format.default(diff)


def create_diff(first_file: dict, second_file: dict) -> dict:  # noqa: WPS210
    """Create dict with diff between two files."""
    diff_result = {}
    common_keys = first_file.keys() & second_file.keys()
    deleted_keys = first_file.keys() - second_file.keys()
    added_keys = second_file.keys() - first_file.keys()
    for common_key in common_keys:
        first_file_value = first_file.get(common_key)
        second_file_value = second_file.get(common_key)
        if first_file_value == second_file_value:
            diff_result[common_key] = [SAME, first_file_value]
        elif isinstance(  # noqa: WPS337
            first_file_value,
            dict,
        ) and isinstance(
            second_file_value,
            dict,
        ):
            diff_result[common_key] = [NESTED, create_diff(
                first_file_value,
                second_file_value,
            )]
        else:
            diff_result[common_key] = [
                CHANGED,
                first_file_value,
                second_file_value,
            ]
    for deleted_key in deleted_keys:
        diff_result[deleted_key] = [DELETED, first_file.get(deleted_key)]
    for added_key in added_keys:
        diff_result[added_key] = [ADDED, second_file.get(added_key)]
    return diff_result

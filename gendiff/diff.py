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
    for key in common_keys:
        old_value = first_file[key]
        new_value = second_file[key]
        if old_value == new_value:
            diff_result[key] = (SAME, old_value)  # noqa: WPS204
        elif (  # noqa: WPS337
            isinstance(old_value, dict)
                and isinstance(new_value, dict)  # noqa: W503
            ):
            diff_result[key] = (NESTED, create_diff(
                old_value,
                new_value,
            ))
        else:
            diff_result[key] = (CHANGED, (old_value, new_value))
    deleted_keys = first_file.keys() - second_file.keys()
    for key in deleted_keys:  # noqa: WPS440
        diff_result[key] = (DELETED, first_file[key])  # noqa: WPS441
    added_keys = second_file.keys() - first_file.keys()
    for key in added_keys:  # noqa: WPS440
        diff_result[key] = (ADDED, second_file[key])  # noqa: WPS441
    return diff_result

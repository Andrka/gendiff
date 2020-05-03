# -*- coding:utf-8 -*-

"""Find diff."""

from gendiff import file_loader


def generate_diff(path_to_first_file: str, path_to_second_file: str) -> str:
    """Generate and return diff between two files."""
    first_file = file_loader.open_file(path_to_first_file)
    second_file = file_loader.open_file(path_to_second_file)
    keys = set(first_file.keys()) | set(second_file.keys())
    diff_result = ['{']
    for key in keys:
        diff_result.append(
            generate_diff_by_key(
                key,
                first_file.get(key),
                second_file.get(key),
            ),
        )
    diff_result.append('}')
    return '\n'.join(diff_result)


def generate_diff_by_key(key: str, first_value, second_value) -> str:
    """Generate and return diff by given key."""
    if (first_value is not None) and (second_value is None):
        return '  - {0}: {1}'.format(key, first_value)
    if (first_value is None) and (second_value is not None):
        return '  + {0}: {1}'.format(key, second_value)
    if first_value == second_value:
        return '    {0}: {1}'.format(key, first_value)
    return '  - {0}: {1}\n  + {2}: {3}'.format(
        key,
        first_value,
        key,
        second_value,
    )

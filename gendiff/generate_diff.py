# -*- coding:utf-8 -*-

"""Find diff."""

from gendiff import cli


def generate_diff(path_to_first_file: str, path_to_second_file: str) -> str:
    """Generate and return diff between two .json files."""
    first_file = cli.open_json_file(path_to_first_file)
    second_file = cli.open_json_file(path_to_second_file)
    keys = set(first_file.keys()) | set(second_file.keys())
    diff_result = ['{']
    for key in keys:
        diff_result.append(
            generate_diff_string(
                key,
                first_file.get(key),
                second_file.get(key),
            ),
        )
    diff_result.append('}')
    return '\n'.join(diff_result)


def generate_diff_string(key: str, first_value, second_value) -> str:
    """Generate and return diff string."""
    if first_value and not second_value:
        return '  - {0}: {1}'.format(key, first_value)
    if not first_value and second_value:
        return '  + {0}: {1}'.format(key, second_value)
    if first_value == second_value:
        return '    {0}: {1}'.format(key, first_value)
    return '  - {0}: {1}\n  + {2}: {3}'.format(
        key,
        first_value,
        key,
        second_value,
    )

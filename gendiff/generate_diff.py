# -*- coding:utf-8 -*-

"""Find diff."""

from gendiff import cli


def generate_diff(path_to_first_file: str, path_to_second_file: str) -> str:
    """Find diff between two json files."""
    first_file = cli.open_json(path_to_first_file)
    second_file = cli.open_json(path_to_second_file)
    keys = set(first_file.keys()) & set(second_file.keys())
    diff_result = ['{']
    for key in keys:
        first_file_value = first_file.get(key)
        second_file_value = second_file.get(key)
        if first_file_value and not second_file_value:
            diff_result.append(['  - {0}: {1}'.format(key, first_file_value)])
            continue
        if not first_file_value and second_file_value:
            diff_result.append(['  + {0}: {1}'.format(key, second_file_value)])
            continue
        if first_file_value == second_file_value:
            diff_result.append(['    {0}: {1}'.format(key, first_file_value)])
            continue
        diff_result.append(['  - {0}: {1}'.format(key, first_file_value)])
        diff_result.append(['  + {0}: {1}'.format(key, second_file_value)])
    diff_result.append('}')
    return '\n'.join(diff_result)

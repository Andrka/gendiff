# -*- coding:utf-8 -*-

"""Find diff."""

from gendiff.file_loader import open_file


def generate_diff_for_print(
    path_to_first_file: str,
    path_to_second_file: str,
) -> str:
    """Generate and return in str format diff between two files."""
    first_file = open_file(path_to_first_file)
    second_file = open_file(path_to_second_file)
    diff = create_diff(first_file, second_file)
    return prepare_diff_for_print(diff)


NESTED = 'nested'
ADDED = 'added'
DELETED = 'deleted'
CHANGED = 'changed'
SAME = 'same'


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


def convert_to_json_veiw(key_value) -> str:
    """Convert given python value to json veiw."""
    transformations = {
        True: 'true',
        False: 'false',
        None: 'null',
    }
    transformation = transformations.get(key_value)
    if (transformation):
        return transformation
    return key_value


INDENT = '    '


def prepare_diff_for_print(  # noqa: WPS231
    diff: dict,
    level_of_indent: int = 0,
) -> str:
    """Convert given diff to str for printing."""
    diff_in_str = '{0}\n'.format('{')
    for key, key_parameter in diff.items():
        if isinstance(key_parameter, list):
            if key_parameter[0] == DELETED:
                diff_in_str = '{0}{1}  - {2}: {3}\n'.format(
                    diff_in_str,
                    INDENT * level_of_indent,  # noqa: WPS204
                    key,
                    prepare_diff_for_print(  # noqa: WPS204
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
                    prepare_diff_for_print(
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
                    prepare_diff_for_print(
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
                    prepare_diff_for_print(
                        key_parameter[1],
                        level_of_indent + 1,
                    ) if isinstance(
                        key_parameter[1],
                        dict,
                    ) else convert_to_json_veiw(key_parameter[1]),
                    INDENT * level_of_indent,
                    key,
                    prepare_diff_for_print(
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
                prepare_diff_for_print(key_parameter[1], level_of_indent + 1),
            )
        else:
            diff_in_str = '{0}{1}    {2}: {3}\n'.format(
                diff_in_str,
                INDENT * level_of_indent,
                key,
                prepare_diff_for_print(
                    key_parameter,
                    level_of_indent + 1,
                ) if isinstance(
                    key_parameter,
                    dict,
                ) else convert_to_json_veiw(key_parameter),
            )
    return '{0}{1}{2}'.format(diff_in_str, INDENT * level_of_indent, '}')

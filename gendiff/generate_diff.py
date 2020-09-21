# -*- coding:utf-8 -*-

"""Find diff."""

from gendiff.file_loader import open_file


def generate_diff(path_to_first_file: str, path_to_second_file: str) -> str:
    """Generate and return in str format diff between two files."""
    first_file = open_file(path_to_first_file)
    second_file = open_file(path_to_second_file)
    diff = create_diff(first_file, second_file)
    return prepare_diff_for_print(diff)


NESTED = 'Nested'
DIFF = 'Diff'
NO = 'No'
ADD = 'Add'
DEL = 'Del'
CHANGED = 'Changed'
OLD_VALUE = 'Old value'
VALUE = 'Value'
CHILDREN = 'Children'


def create_diff(first_file: dict, second_file: dict) -> dict:
    """Create dict with diff between two files."""
    diff = {}
    keys = set(first_file.keys()) | set(second_file.keys())
    for key in keys:
        if isinstance(first_file.get(key), dict):
            if isinstance(second_file.get(key), dict):
                diff[key] = {
                    DIFF: NESTED,
                    OLD_VALUE: None,
                    VALUE: None,
                    CHILDREN: create_diff(
                        first_file.get(key),
                        second_file.get(key),
                    ),
                }
                continue
        diff[key] = generate_diff_by_key(
            first_file.get(key),
            second_file.get(key),
        )
    return diff


def generate_diff_by_key(first_value, second_value) -> dict:
    """Generate and return diff by single key."""
    if (first_value is not None) and (second_value is None):
        return {
            DIFF: DEL,
            OLD_VALUE: first_value,
            VALUE: None,
            CHILDREN: None,
        }
    if (first_value is None) and (second_value is not None):
        return {
            DIFF: ADD,
            OLD_VALUE: None,
            VALUE: second_value,
            CHILDREN: None,
        }
    if first_value == second_value:
        return {
            DIFF: NO,
            OLD_VALUE: None,
            VALUE: first_value,
            CHILDREN: None,
        }
    return {
        DIFF: CHANGED,
        OLD_VALUE: first_value,
        VALUE: second_value,
        CHILDREN: None,
    }


def prepare_diff_for_print(diff: dict) -> str:
    """Convert given diff to str for printing."""
    pass


'''
changes = {NO: ' ', ADD: '+', DEL: '-', }


def prepare_diff_for_print3(diff: dict) -> str:
    """Convert given diff to str for printing."""
    diff_in_str = '{\n'
    for key, key_parameters in diff.items():
        if isinstance(key_parameters, dict):
            if key_parameters.get(CHILDREN):
                diff_in_str = '{0}    {1}: {2}\n'.format(
                    diff_in_str,
                    key,
                    prepare_diff_for_print(key_parameters[CHILDREN]),
                )
            else:
                for key_changes, key_value in key_parameters.get(VALUE).items():
                    if isinstance(key_value, dict):
                        diff_in_str = '{0}  {1} {2}: {3}\n'.format(
                            diff_in_str,
                            changes[key_changes],
                            key,
                            prepare_diff_for_print(key_value),
                        )
                    else:
                        diff_in_str = '{0}  {1} {2}: {3}\n'.format(
                            diff_in_str,
                            changes[key_changes],
                            key,
                            key_value,
                        )
        else:
            diff_in_str = '{0}        {1}: {2}\n'.format(
                diff_in_str,
                key,
                key_parameters,
            )
    return '{0}{1}'.format(diff_in_str, '    }')


def prepare_diff_for_print(diff, level_of_indent: int = 0) -> str:
    diff_in_str = '{0}\n{1}'.format('{', '    ' * level_of_indent)
    if isinstance(diff, dict):
        for key, key_parameter in diff.items():
            if isinstance(key_parameter, dict):
                if key_parameter.get(CHILDREN):
                    diff_in_str = '{0}  {1} {2}: {3}\n'.format(diff_in_str, changes[key_parameter.get(VALUE)], key, prepare_diff_for_print(key_parameter[CHILDREN], level_of_indent + 1))
                if isinstance(key_parameter.get(VALUE), dict):
                    for change, change_value in key_parameter.get(VALUE).items():
                        diff_in_str = '{0}  {1} {2}: {3}\n'.format(diff_in_str, changes[change], key, prepare_diff_for_print(key_parameter[VALUE], level_of_indent + 1))
            else:
                diff_in_str = '{0}{1}\n'.format(diff_in_str, key_parameter)
    else:
        diff_in_str = '{0}{1}'.format(diff_in_str, diff)
    return '{0}{1}{2}{3}'.format(diff_in_str, '\n', '    ' * level_of_indent, '}')


def prepare_diff_for_print2(diff: dict) -> str:
    """Convert given diff to str for printing."""
    diff_in_list = []
    if isinstance(diff, dict):
        for key, key_parameters in diff.items():
            if isinstance(key_parameters, dict):
                if key_parameters.get(CHILDREN):
                    diff_in_list.append(
                        prepare_diff_for_print(key_parameters[CHILDREN]),
                    )
                else:
                    for change, change_value in key_parameters.get(VALUE).items():
                        diff_in_list.append('  {0} {1}: {2}'.format(changes[change], key, change_value))
    return '\n'.join(map(str, diff_in_list))


def prepare_diff_for_print1(diff: dict) -> str:
    """Convert given diff to str for printing."""
    diff_list = []
    for key, key_parameters in diff.items():
        #diff_list.append(['{0}:'.format(key)])
        if isinstance(key_parameters, dict):
            if key_parameters.get(CHILDREN):
                diff_list.append(
                    prepare_diff_for_print(key_parameters[CHILDREN]),
                )
            else:
                if isinstance(key_parameters.get(VALUE), dict):
                    for change, change_value in key_parameters.get(VALUE).items():
                        diff_list.append('  {0} {1}: {2}'.format(changes[change], key, change_value))
    return '\n'.join(map(str, diff_list))
'''

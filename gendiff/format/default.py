# -*- coding:utf-8 -*-

"""Generate json-like text diff between two files."""

from gendiff import diff
from gendiff.converter import convert_to_json_veiw

SYMBOLS = {  # noqa: WPS407
    diff.ADDED: '+',
    diff.DELETED: '-',
    diff.SAME: ' ',
}
INDENT = '  '


def default(diff_dict: dict, indent_level: int = 1) -> str:
    """Convert given diff to json-like text format."""
    result = []
    for key, (status, value) in sorted(diff_dict.items()):  # noqa: WPS414, WPS405, E501

        def indent_append(state, append_value):  # noqa: WPS430
            """Append expected indent, key and value in result list."""
            result.append(
                '{0}{1} {2}: {3}'.format(
                    INDENT * indent_level,
                    SYMBOLS[state],
                    key,
                    append_value,
                ),
            )

        if status == diff.NESTED:
            indent_append(diff.SAME, '{')
            result.append(default(value, indent_level + 2))
            result.append('{0}}}'.format(INDENT * (indent_level + 1)))
        elif status == diff.CHANGED:
            indent_append(
                diff.DELETED,
                value_to_str(value[0], indent_level),
            )
            indent_append(
                diff.ADDED,
                value_to_str(value[1], indent_level),
            )
        else:
            indent_append(
                status,
                value_to_str(value, indent_level),
            )
    if indent_level == 1:
        result = ['{'] + result + ['}']
    return '\n'.join(result)


def value_to_str(  # noqa: WPS231
    value,
    indent_level: int,
    nested_level: int = 1,
) -> str:
    """Convert given value to string."""
    if isinstance(value, dict):
        result = []
        if nested_level == 1:
            result.append('{')
        for key, item in value.items():
            if isinstance(item, dict):
                result.append(
                    '{0}{1}: {{'.format(
                        INDENT * (indent_level + 3),
                        key,
                    ),
                )
                result.append(
                    value_to_str(
                        item,
                        indent_level + 2,
                        nested_level + 1,
                    ),
                )
                if indent_level == 1:
                    result.append(
                        '{0}}}'.format(INDENT * (indent_level + 1)),
                    )
            else:
                result.append(
                    '{0}{1}: {2}'.format(
                        INDENT * (indent_level + 3),
                        key,
                        convert_to_json_veiw(item),
                    ),
                )
        if indent_level != 1:
            result.append(
                '{0}}}'.format(INDENT * (indent_level + 1)),
            )
        return '\n'.join(result)
    return convert_to_json_veiw(value)

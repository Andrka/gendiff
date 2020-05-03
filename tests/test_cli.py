# -*- coding:utf-8 -*-

"""Test cli module."""

import sys

from gendiff.cli import parse_arguments, print_result


def test_print_result(capfd):
    """Test print_result function."""
    print_result('test')
    out, err = capfd.readouterr()
    assert out == '\ntest\n'
    assert err == ''


def test_parse_arguments():
    """Test parse_arguments function."""
    sys.argv = [
        'test',
        'first',
        'second',
    ]
    args = parse_arguments()
    assert args.first_file == 'first'
    assert args.second_file == 'second'

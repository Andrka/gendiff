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
        'test1',
        'first',
        'second',
    ]
    args = parse_arguments()
    assert args.format is None
    assert args.first_file == 'first'
    assert args.second_file == 'second'
    sys.argv = [
        'test2',
        '-fjson_like',
        'first',
        'second',
    ]
    args = parse_arguments()
    assert args.format == 'json_like'
    assert args.first_file == 'first'
    assert args.second_file == 'second'
    sys.argv = [
        'test3',
        '-fplain',
        'first',
        'second',
    ]
    args = parse_arguments()
    assert args.format == 'plain'
    assert args.first_file == 'first'
    assert args.second_file == 'second'

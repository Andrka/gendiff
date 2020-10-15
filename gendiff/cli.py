# -*- coding:utf-8 -*-

"""Realize command line interface."""

import argparse

from gendiff import format


def parse_arguments():
    """Return parser of command line arguments."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument(
        '-f',
        '--format',
        default=format.DEFAULT,
        choices=[format.DEFAULT, format.PLAIN, format.JSON],
        help='set format of output',
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    return parser

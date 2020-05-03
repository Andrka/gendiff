# -*- coding:utf-8 -*-

"""Realize command line interface."""

import argparse


def print_result(diff_result: str):
    """Print taken result."""
    print('\n', diff_result, sep='')


def parse_arguments():
    """Take and return command line arguments."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    return parser.parse_args()

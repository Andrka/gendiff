#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Package is under development."""

import argparse

from gendiff.cli import print_result
from gendiff.generate_diff import generate_diff


def main():
    """Take command line arguments."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    print_result(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()

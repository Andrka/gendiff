#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Package is under development."""

from gendiff.cli import parse_arguments, print_result
from gendiff.generate_diff import generate_diff_for_print


def main():
    """Generate diff."""
    args = parse_arguments()
    print_result(generate_diff_for_print(args.first_file, args.second_file))


if __name__ == '__main__':
    main()

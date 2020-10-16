#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Package is under development."""

from gendiff.cli import parse_arguments
from gendiff.diff import generate_diff_for_print


def main():
    """Generate diff."""
    args = parse_arguments().parse_args()
    print()
    print(generate_diff_for_print(
        args.first_file,
        args.second_file,
        args.format,
    ))


if __name__ == '__main__':
    main()

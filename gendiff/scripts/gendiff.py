#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Generate differences script."""

from gendiff import cli, diff


def main():
    """Generate diff."""
    args = cli.parse_arguments().parse_args()
    print(diff.printable(
        args.first_file,
        args.second_file,
        args.format,
    ))


if __name__ == '__main__':
    main()

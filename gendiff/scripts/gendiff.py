# -*- coding:utf-8 -*-

""" Package is under development."""

import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()


if __name__ == '__main__':
    main()

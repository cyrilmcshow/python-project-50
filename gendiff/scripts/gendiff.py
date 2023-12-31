#!/usr/bin/env python3
import argparse
from gendiff.app import generate_diff


def add_arg():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')  # noqa E501
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        help='set format of output'
    )
    args = parser.parse_args()
    return args


def main():
    args = add_arg()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()

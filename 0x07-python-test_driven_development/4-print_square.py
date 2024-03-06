#!/usr/bin/python3
"""making square"""


def print_square(size):
    """error and making sq"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for _ in range(size):
        print("#"*size)

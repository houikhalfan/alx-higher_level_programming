#!/usr/bin/python3
"""file handling"""


def read_file(filename=""):
    """reading from a file using with to close automaticly"""
    with open(filename, 'r', encoding='utf-8') as a_file:
        print(a_file.read(), end="")

#!/usr/bin/python3
"""append file"""


def append_write(filename="", text=""):
    """append text to file"""
    with open(filename, 'a', encoding='utf-8') as a_file:
        return a_file.write(text)

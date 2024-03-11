#!/usr/bin/python3
"""file i/o"""


def write_file(filename="", text=""):
    """write"""
    with open(filename, 'w', encoding='utf-8') as a_file:
        return a_file.write(text)

#!/usr/bin/python3
"""function that writes
 an Object to a text file,
using a JSON representation"""


def class_to_json(obj):
    """class to json"""
    return obj.__dict__

#!/usr/bin/python3
"""
square class
"""


class Square:
    """ square claasss"""
    def __init__(self, size=0):
        """ int size
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

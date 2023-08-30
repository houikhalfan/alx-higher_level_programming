#!/usr/bin/python3
"""
square class
"""


class Square:
    """ square claasss"""
    def __init__(self, size=0):
        """ int size
        """
        self.__size = size

    @property
    def size(self):
        """retr size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ exceptions for size"""
        if type(value) is int and value >= 0:
            self.__size = value
        elif type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("{}".format('#'), end="")
                print()
        else:
            print()

#!/usr/bin/python3
"""
def a trg class
"""


class Rectangle:
    """Representation of a rectangle"""
    def __init__(self, width=0, height=0):
        """defining two parameter"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area calc"""
        return self.__height * self.__width

    def perimeter(self):
        """peri calc"""
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            return 2 * self.__width + 2 * self.__height

    def __str__(self):
        """fach command str() ayakghaw aliha direct had def atakhdm"""
        s = ""
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    s += "#"
                s += "\n"
        s = s[:-1]
        return s

    def __repr__(self):
        """anakhduu repr d def w t executa b eval"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

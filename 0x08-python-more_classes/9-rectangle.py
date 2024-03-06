#!/usr/bin/python3
"""
def a trg class
"""


class Rectangle:
    """Representation of a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    @classmethod
    def square(cls, size=0):
        return cls(width=size, height=size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 >= area_2:
            return rect_1
        elif area_1 < area_2:
            return rect_2

    def __init__(self, width=0, height=0):
        """defining two parameter"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        return self.__width * self.__height

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
                    s += "{}".format(self.print_symbol)
                s += "\n"
        s = s[:-1]
        return s

    def __repr__(self):
        """anakhduu repr d def w t executa b eval"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """del an object when we cal del"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

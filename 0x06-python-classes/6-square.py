#!/usr/bin/python3
"""square class ag
"""


class Square:
    """square class"""
    def __init__(self, size=0, position=(0, 0)):
        """initialization size: size
        initialization position: pos
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """retr value"""
        return self.__size

    @size.setter
    def size(self, value):
        """value excep"""
        if type(value) is int and value >= 0:
            self.__size = value
        elif type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """retr value"""
        return self.__position

    @position.setter
    def position(self, value):
        """value exceptions"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """square area"""
        return self.__size * self.__size

    def my_print(self):
        """print the # """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

#!/usr/bin/python3
"""rectangle class"""
from .base import Base


class Rectangle(Base):
    """Represents a rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle object with width,
        height, x-coordinate, y-coordinate, and an optional id."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle. Validates
        that the value is an integer and > 0."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.
        Validates that the value is an integer and > 0."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle.
        Validates that the value is an integer and >= 0."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the rectangle.
        Validates that the value is an integer and >= 0."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Display a visual representation of the
        rectangle using '#' characters."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """Return a string representation
        of the rectangle object."""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle.
        Can be called with positional arguments
        (id, width, height, x, y) or keyword arguments.
        """
        attrs = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation
        of the rectangle object."""
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }

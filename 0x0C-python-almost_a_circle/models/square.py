#!/usr/bin/python3
"""square class"""
from .rectangle import Rectangle


class Square(Rectangle):
    """representation of square"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square object with a
        given size, x-coordinate, y-coordinate,
        and an optional id.
        The size is used to set the width
        and height of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation
        of the Square object."""
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square. Validates that
        the value is an integer and > 0.
        The size is used to set the width and
        height of the square.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of the square.
        Can be called with positional
        arguments (id, size, x, y) or keyword arguments.
        """
        attrs = ['id', 'size', 'x', 'y']
        if args:
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation
        of the square object."""
        return {
            'id': self.id,
            'x': self.x,
            'size': self.width,
            'y': self.y
        }

    def area(self):
        """cal the area"""
        return self.width ** 2

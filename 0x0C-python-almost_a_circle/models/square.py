#!/usr/bin/python3
"""This module has a class, square
from the rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """This is the class, Square
    with a class constructor"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes the attributes"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """gets the square size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the squaresize"""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns the str rep of the instance"""
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.height)

    def update(self, *args, **kwargs):
        """assigns attributes to the arguments"""
        if args:
            sq_attrs = ["id", "size", "x", "y"]
            for x, ar in enumerate(args):
                setattr(self, sq_attrs[x], ar)
        elif kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)

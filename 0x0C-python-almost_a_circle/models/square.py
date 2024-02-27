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

    def __str__(self):
        """Returns the str rep of the instance"""
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.height)

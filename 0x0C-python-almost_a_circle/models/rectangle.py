#!/usr/bin/python3
"""
This module has a class, Rectangle
"""

from models.base import Base


class Rectangle(Base):
    """This is the class, Rectangle, that
    inherits from base. with private nstance
    attributes, each with their own getter and setters
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes the attributes of a rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # getters
    @property
    def width(self):
        """gives the width of the rect"""
        return self.__width

    @property
    def height(self):
        """gives the height of the rect"""
        return self.__height

    @property
    def x(self):
        """gives the x of the rect"""
        return self.__x

    @property
    def y(self):
        """gives the y of the rect"""
        return self.__y

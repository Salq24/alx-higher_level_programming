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
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

# getters
    @property
    def width(self):
        """gives the width"""
        return self.__width

    @property
    def height(self):
        """gives the height"""
        return self.__height

    @property
    def x(self):
        """gives the x"""
        return self.__x

    @property
    def y(self):
        """gives the y"""
        return self.__y

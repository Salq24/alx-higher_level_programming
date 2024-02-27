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
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """gets the rect width"""
            return self.__width

        @width.setter
        def width(self, value):
            """sets the rect width"""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            """gets the rect height"""
            return self.__height

        @height.setter
        def height(self, value):
            """sets the rect height"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            """gets the rect x"""
            return self.__x

        @x.setter
        def x(self, value):
            """sets the rect x"""
            if not isinstance(value, int):
                raise TypeError("x must be an integer")
            if value <= 0:
                raise ValueError("x must be > 0")
            self.__x = value

        @property
        def y(self):
            """gets the rect y"""
            return self.__y

        @y.setter
        def y(self, value):
            """sets the rect y"""
            if not isinstance(value, int):
                raise TypeError("y must be an integer")
            if value <= 0:
                raise ValueError("y must be > 0")
            self.__y = value

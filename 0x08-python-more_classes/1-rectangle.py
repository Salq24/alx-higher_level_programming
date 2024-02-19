#!/usr/bin/python3
"""
This module builds a class named rectangle,
with private instance attributes, width and
height"""


class Rectangle:
    """This is the class built.
    Attributes: width and height
    Raises:
    ValueError , if width or height are
    less than zero.
    TypeError, if width and height are not integers
    """
    def __init__(self, width=0, height=0):
        try:
            self.width = width
            self.height = height
        except (TypeError, ValueError) as e:
            print(f"{e}")

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            try:
                if not isinstance(value, int):
                    raise TypeError("width must be an integer")
                if value < 0:
                    raise ValueError("width must be >= 0")
                self.__width = value
            except (TypeError, ValueError) as e:
                print(f"{e}")

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            try:
                if not isinstance(value, int):
                    raise TypeError("height must be an integer")
                if value < 0:
                    raise ValueError("height must be >= 0")
                self.__height = value
            except (TypeError, ValueError) as e:
                print(f"{e}")

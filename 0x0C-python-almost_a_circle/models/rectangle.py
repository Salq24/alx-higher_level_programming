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

    @width.setter
    def width(self, value):
        """sets rect width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """sets rectangle height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """sets rectangle x value"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """sets rectangle y value"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the rectangle"""
        return (self.width * self.height)

    def display(self):
        """prints in stdout the rect instance,
        with the char, #
        """
        for i in range(self.y):
            print()
        for x in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            rect_attr = ["id", "width", "height", "x", "y"]
            for x, arg in enumerate(args):
                setattr(self, rect_attr[1], arg)
        elif kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def __str__(self):
        """returns the str rep of the rect instance"""
        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.x, self.y, self.width, self.height)

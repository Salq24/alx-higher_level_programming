#!/usr/bin/python3
"""A class that define a square and gets the area"""


class Square:
    """This is a class"""
    def __init__(self, size=0):
        """Initialization of size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Gets the area of the square"""
        return self.__size**2

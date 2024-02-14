#!/usr/bin/python3
"""A square is defined"""


class Square:
    """This is a class"""
    def __init__(self, size=0):
        """Square initilization by size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

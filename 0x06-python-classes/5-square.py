#!/usr/bin/python3
"""Creating a class, Square, that defines a square"""


class Square:
    """This is the class creation"""
    def __init__(self, size=0):
        """Initialization of size"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the area of the square"""
        return self.__size**2

    def my_print(self):
        """prints in stdout, the square, with '#'"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#' * self.__size)

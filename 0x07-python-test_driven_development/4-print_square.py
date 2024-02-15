#!/usr/bin/python3
""" This module has a function named print_square.
"""


def print_square(size):
    """ Prints a square with the character '#'.
        Args:
        size: size length of the square

        Returns:
        A square with thecharacter, '#'

        Raises:
        TypeError: if size is not an integer
        ValueError: if size < 0

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            print("#" * size)

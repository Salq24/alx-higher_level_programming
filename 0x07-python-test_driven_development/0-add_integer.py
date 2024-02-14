#!/usr/bin/python3
""" This has a function, add_integer, that adds up
two integers or floats, and returns the sum
"""


def add_integer(a, b=98):
    """In this function, b is a default value of 98,
    a and b have to be floats or integers.
    If floats, we convert to integers befors printing out
    the results
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        a + b
    return int(a + b)

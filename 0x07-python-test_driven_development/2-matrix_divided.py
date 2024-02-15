#!/usr/bin/python3
""" This module has a function named matrix_divided.
It takes in a list of lists, of integers or float type, divides
it with a number, div, and returns an new matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides through a list of lists, by a number, div

    Args:
    matrix: which is a list of lists
    div: can be an int or float.

    Returns: an new ;ist of lists.

    Raises:
    ZeroDivision error< if div is equal to 0
    TypeError: If there is another data type.
    """
    mess1 = ("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(matrix, list):
        raise TypeError(mess1)

    if not all(isinstance(i, list) for i in matrix):
        raise TypeError(mess1)
    if not all(len(i) == len(matrix[0]) for i in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(mess1)
            else:
                new_row.append(round(elem / div, 2))
        new_matrix.append(new_row)
    return new_matrix

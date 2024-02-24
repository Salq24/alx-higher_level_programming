#!/usr/bin/python3
"""
Thismodule has a function pascal_triangle
that returns a list of lists of integers
"""


def pascal_triangle(n):
    """
    This is the function, with
    arg, n
    """
    if n <= 0:
        return []

    pas = []
    for x in range(n):
        row = [1]
        if x > 0:
            row_p = pas[-1]
            for w in range(1, x):
                row.append(row_p[w - 1] + row_p[w])
            row.append(1)
        pas.append(row)

    return pas

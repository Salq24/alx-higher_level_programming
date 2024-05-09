#!/usr/bin/python3
""" finds a peak in a list of unsorted int"""


def find_peak(list_of_integers):
    d_lent = len(list_of_integers)
    d_mid = d_lent
    middle = d_lent // 2

    if not list_of_integers:
        return (None)

    while True:
        d_mid = d_mid // 2

        if middle < d_lent - 1 and
        list_of_integers[middle] < list_of_integers[middle + 1]:
            if d_mid // 2 == 0:
                d_mid = 2
                middle = middle + d_mid // 2
        elif d_mid > 0 and
        list_of_integers[middle] < list_of_integers[middle - 1]:
            if d_mid // 2 == 0:
                d_mid = 2
            middle = middle - d_mid // 2
        else:
            return (list_of_integers[middle])

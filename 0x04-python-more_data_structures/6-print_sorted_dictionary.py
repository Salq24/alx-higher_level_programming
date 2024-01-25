#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = dict(sorted(a_dictionary.items()))
    for i,v in new.items():
        max = print(("{}: {}").format(i, v))
    return max

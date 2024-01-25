#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for keyz in sorted(a_dictionary.keys()):
        print("{}: {}".format(keyz, a_dictionary[keyz]))

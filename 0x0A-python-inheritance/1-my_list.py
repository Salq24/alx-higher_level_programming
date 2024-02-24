#!/usr/bin/python3
"""
This module contains a class
MyList, that inherits from list
"""


class MyList(list):
    def print_sorted(self):
        sort_list = sorted(self)
        print(sort_list)

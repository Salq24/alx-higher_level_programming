#!/usr/bin/python3
"""
This module contains a function, write_file that
writes a string to a text file(UTF-8) and returns
the num of xters written
"""
def write_file(filename="", text=""):
    """This is the function, It should create
    the file if it does not exist, and should overwrite
    the content of the file if it already exists.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        num_xters = file.write(text)
    return num_xters

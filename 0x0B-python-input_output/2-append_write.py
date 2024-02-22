#!/usr/bin/python3
"""
This module has a function, append_write, which
appends a string at the end of a text file
(utf8) and returns the num of xters added
"""
def append_write(filename="", text=""):
    """
    This is the function. We did not manage file permission
    or errors here.
    If the file does not exist, it must be created.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        num_xters = file.write(text)
    return num_xters

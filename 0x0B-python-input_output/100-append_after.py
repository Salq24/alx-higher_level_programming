#!/usr/bin/python3
"""
This module has a function, append_after, that
inserts a line of text to a file, after each line
containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    This is the function, with args
    filename, search_string, new_string
    """
    if not filename or not search_string\
            or not new_string:
        return
    lns = ""
    with open(filename, 'r+') as file:

        for ln in file:
            lns += ln
            if search_string in ln:
                lns += new_string
    with open(filename, "w") as wrt:
        wrt.write(lns)

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

    with open(filename, 'r+') as file:
        lns = file.readlines()
        file.seek(0)

        for l in lns:
            file.write(l)
            if search_string in l:
                file.write(new_string + '\n')

        file.truncate()


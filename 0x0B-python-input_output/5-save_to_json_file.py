#!/usr/bin/python3
"""
This module makes a function, save_to_json_file,
which writes an object to a text file, using
a JSON rep.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    This is the function. Here, we are not
    handling errors.
    The arg @my_obj is the string to be
    converted"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)

#!/usr/bin/python3
"""
This module makes a function, load_from_json_file,
which creates an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    This is the function. Here, we are not
    handling errors.
    The arg @my_obj is the string to be
    converted"""
    with open(filename, 'r') as file:
        return json.load(file)

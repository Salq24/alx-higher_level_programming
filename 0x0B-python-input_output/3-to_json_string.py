#!/usr/bin/python3
"""
This module makes a function, to_json_string,
which returns the JSON rep of an object
or string
"""
import json


def to_json_string(my_obj):
    """
    This is the function. Here, we are not
    handling errors.
    The arg @my_obj is the string to be
    converted"""
    return json.dumps(my_obj)

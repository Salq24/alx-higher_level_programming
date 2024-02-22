#!/usr/bin/python3
"""
This module makes a function, from_json_string,
which returns an object rep by a JSON
string
"""
import json


def from_json_string(my_str):
    """
    This is the function. Here, we are not
    handling errors.
    The arg @my_str is the string to be
    converted"""
    return json.loads(my_str)

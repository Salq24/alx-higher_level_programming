#!/usr/bin/python3
""" This module has a function named say_my_name. It prints
My name is <first name> <last name>
"""
def say_my_name(first_name, last_name=""):
    """
    Prints 'My name is <first name> <last name>'
    Args:
    first_name: the first name
    last_name: the last name

    Returns:
    My name is <first name> <last name>

    Raises:
    TypeError: if datatype is not string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print(("My name is {} {}").format(first_name, last_name))

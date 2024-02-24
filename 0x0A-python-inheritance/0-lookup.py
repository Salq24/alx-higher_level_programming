#!/usr/bin/python3
"""
This module has a function, lookup,
that returns a list of available attributes
and methods of an object
"""

def lookup(obj):
    """This is the function"""
    return dir(obj)

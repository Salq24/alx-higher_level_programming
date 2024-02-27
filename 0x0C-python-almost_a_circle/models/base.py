#!/usr/bin/python3
"""
This module has a class, Base
"""


class Base:
    """This is the class,
    with private class attribute and
    class constructor
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

#!/usr/bin/python3
"""
This module has a class, Base
"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returnsthe JSON str rep of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON str rep of list_objs
        to a file"""
        filenm = cls.__name__ + ".json"
        with open(filenm, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                dict_list = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(dict_list))

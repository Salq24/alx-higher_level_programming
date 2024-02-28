#!/usr/bin/python3
"""
This module has a class, Base
"""


import json
import csv
import os


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

    @staticmethod
    def from_json_string(json_string):
        """that returns the list of the JSON str rep json_string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            second = cls(1, 1)
        elif cls.__name__ == 'Square':
            second = cls(1)
        else:
            return None
        second.update(**dictionary)
        return second

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filenm = cls.__name__ + ".json"
        try:
            with open(filenm, 'r') as file:
                json_str = file.read()
                dict_list = cls.from_json_string(json_str)
                return [cls.create(**dic) for dic in dict_list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in csv"""
        filenm = cls.__name__ + ".csv"
        with open(filenm, 'w', newline="") as file:
            if list_objs is not None or list_objs == []:
                file.write("[]")
            else:
                if cls.__name__ == 'Rectangle':
                    nms = ["id", "width", "height", "x", "y"]
                else:
                    nms = ["id", "size", "x", "y"]
                writter = csv.DictWriter(file, fieldnames=nms)
                for obj in list_objs:
                    writter.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in csv"""
        filenm = cls.__name__ + ".csv"
        try:
            with open(filenm, "r", newline="") as file:
                if cls.__name__ == "Rectangle":
                    nms = ["id", "width", "height", "x", "y"]
                else:
                    nms = ["id", "size", "x", "y"]
                dict_list = csv.DictReader(file, fieldnames=nms)
                dict_list = [dict([k, int(v)] for k, v in d.items())
                             for d in dict_list]
                return [cls.create(**d) for d in dict_list]
        except IOError:
            return []

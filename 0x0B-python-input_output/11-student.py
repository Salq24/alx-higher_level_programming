#!/usr/bin/python3
"""
This module has a class, Student, already
defined prev.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            dict = {}
            for at in attrs:
                if hasattr(self, at):
                    dict[attr] = getattr(self, at)
            return dict

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)

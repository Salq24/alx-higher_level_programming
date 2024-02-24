#!/usr/bin/python3
"""
Rhis module has a class, Student that defines
a student by public instance attributes,
first_name, last_name, age
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
                    dict[at] = getattr(self, at)
            return dict

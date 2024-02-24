#!/usr/bin/python3
"""
This module has a function, class_to_json,
that returns the dictionary description
with simple data structure for JSON serialization
of an object
"""


def class_to_json(obj):
    """
    This is the function. obj is an
    instance of a class.
    """
    if isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}
    elif isinstance(obj, (str, int, bool)):
        return obj
    elif isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif hasattr(obj, '__dict__'):
        return \
            {key: class_to_json(value) for key, value in obj.__dict__.items()}
    else:
        raise TypeError(f"Obj of type {type(obj)} is not JSON serializatable")

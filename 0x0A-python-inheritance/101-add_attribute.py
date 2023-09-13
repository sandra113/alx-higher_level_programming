#!/usr/bin/python3
"""Checks if an object can have a new attribute"""


def add_attribute(obj, attr_name, attr_value):
    """Checks if an object can have a new attribute"""
    if hasattr(obj, '__dict__') and not isinstance(obj, type):
        # If the object has a __dict__ attribute and is not a class (type)
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("Can't add new attribute")

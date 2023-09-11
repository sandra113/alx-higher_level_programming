#!/usr/bin/python3
"""Function to checkif an object is an instance of a specified class."""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a class.

    Args:
        obj: The object to be checked.
        a_clas: The class to compare against.

    Return:
        True if obj is an instance of a_class, else False.
    """
    if type(obj) == a_class:
        return True
    return False

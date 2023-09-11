#!/usr/bin/python3
"""Function to check if an object is an instance of a class."""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is exactly an instance of a class or,
    if the object is an instance of a class that inherited from, the class

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Return:
        True if obj is an instance of a_class, else False.
    """
    if isinstance(obj, a_class):
        return True
    return False

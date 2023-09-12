#!/usr/bin/python3
"""This module Check if the object is an instance of a class"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited 
    (directly or indirectly) from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a class inherited from a_class, otherwise False.
    """

    if type(obj) == a_class:
        return False
    for base_class in type(obj).__bases__:
        if inherits_from(base_class, a_class):
            return True
    return False

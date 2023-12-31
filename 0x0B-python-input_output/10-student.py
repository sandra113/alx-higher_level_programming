#!/usr/bin/python3
"""This module defines a student"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """initializes the public instancesfirst_name, last_name, age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of the Student instance."""
        if attrs is None:
            return self.__dict__
        else:
            attr_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    attr_dict[attr] = getattr(self, attr)
            return attr_dict

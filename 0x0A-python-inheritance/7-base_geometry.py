#!/usr/bin/python3
"""Defines an empty class BassGeometry"""


class BaseGeometry:
    """Defines the class"""

    def area(self):
        """defining public instance method area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))      
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

#!/usr/bin/python3
"""A module for a class Rectangle that  inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle that imports from BaseGeometry"""

    def __init__(self, width, height):
        """Initializes the instances width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

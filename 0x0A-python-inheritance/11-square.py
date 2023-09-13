#!/usr/bin/python3
"""A module for a class square that  inherits from rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class square that imports from Rectangle"""

    def __init__(self, size):
        """Initializes the instance size"""
        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """Calculates the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Returns a string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)

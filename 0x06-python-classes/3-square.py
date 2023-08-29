#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """This class represents a square."""

    def __init__(self, size=0):
        """
        Initializes a square instance.

        Args:
            size(int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Returns the current square area"""

        return self.__size * self.__size 

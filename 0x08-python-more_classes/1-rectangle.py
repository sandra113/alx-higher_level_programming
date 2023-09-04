#!/usr/bin/python3
"""This module defines a Square class."""


class Rectangle:
    """This class represents a square."""
    pass

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangule instance

        Args:
            width(int): The width of the rectangle
            height(int): The height of the rectangle
        """
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """
        Getter method for the height of the rectangle.

        Returns:
        int: The height fo the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height of the rectangular.

        Args:
            value (int): the height of the rectangle. Must be an integer >= 0

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is < 0.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """
        Getter method for the width of the rectangle.

        Returns:
        int: The width fo the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width of the rectangular.

        Args:
            value (int): the width of the rectangle. Must be an integer >= 0

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is < 0.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

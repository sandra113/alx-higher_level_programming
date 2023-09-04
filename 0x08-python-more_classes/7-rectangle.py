#!/usr/bin/python3
"""This module defines a Square class."""


class Rectangle:
    """This class represents a square."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangule instance

        Args:
            width(int): The width of the rectangle
            height(int): The height of the rectangle
        """
        self.__height = height
        self.__width = width
        self.__print_symbol = Rectangle.print_symbol
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width <= 0 or self.__height <= 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width <= 0 or self.__height <= 0:
            return ""
        rect_str = ""
        for i in range(self.__height):
            rect_str += str(self.print_symbol) * self.__width + "\n"
        return rect_str[:-1]

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

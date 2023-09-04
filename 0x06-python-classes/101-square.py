#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """This class represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square instance.

        Args:
            size(int): The size of the square.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter method to retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Getter method to retrieve the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method to set the position"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        a, b = value
        if not isinstance(a, int) or not isinstance(a, int) or a < 0 or b < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """Prints in stdout the square with character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.position[0], end='')
                print("#" * self.__size)

    def __str__(self):
        """
        Custom string representation for the Square object.
        """
        return self.matrix()

    def matrix(self):
        """Returns a matrix representation of the square."""
        if self.__size == 0:
            return ""
        else:
            matrix = []
            for _ in range(self.__position[1]):
                matrix.append([" " * self.__size])
            for _ in range(self.__size):
                matrix.append([" " * self.__position[0] + "#" * self.__size])
            return "\n".join("".join(row) for row in matrix)

#!/usr/bin/python3
"""Base class for models"""


class Base:
    """Base class for models"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class" constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def __str__(self):
        """Return a string representation of the object."""
        return "{}".format(self.id)

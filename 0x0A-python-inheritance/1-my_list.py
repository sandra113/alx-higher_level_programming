#!/usr/bin/python3
"""Defines class Mylist inherited from list"""


class MyList(list):
    """ Mylist class inherits from list """

    def print_sorted(self):
        """Prints sorted list"""
        if all(isinstance(x, int) for x in self):
            sorted_list = sorted(self)
            print(sorted_list)
        else:
            raise ValueError("Input list must contain only integers")

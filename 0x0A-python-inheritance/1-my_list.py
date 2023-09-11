#!/usr/bin/python3

class Mylist(list):
    """ Mylist class inherits from list """

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)

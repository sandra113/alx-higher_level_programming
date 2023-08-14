#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    length = len(my_list)

    new_list = my_list[length-1::-1]

    for i in range(length):

        print("{:d}".format(new_list[i]))

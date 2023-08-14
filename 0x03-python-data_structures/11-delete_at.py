#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list
    length = len(my_list) - 1
    for i in range(length):
        if i == idx:
            my_list.remove(my_list[i])
            return my_list

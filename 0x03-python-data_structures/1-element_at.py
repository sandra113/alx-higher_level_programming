#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0:
        return(None)
    length = len(my_list)
    for i in range(length):
        if i == idx:
            return(my_list[i])

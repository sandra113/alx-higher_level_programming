#!/usr/bin/python3

def remove_char_at(str, n):
    str_len = len(str)
    str_copy = ''

    for i in range(str_len):
        if i != n:
            str_copy += str[i]

    return str_copy

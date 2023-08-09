#!/usr/bin/python3

def print_last_digit(number):
    num = str(abs(number))
    num_len = len(num)
    last_digit = num[num_len - 1]
    return int(last_digit)

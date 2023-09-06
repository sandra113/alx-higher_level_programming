#!/usr/bin/python3

def add_integer(a, b=98):
    num1 = int(a)
    num2 = int(b)

    if not isinstance(num1, int) or isinstance(num1, float):
        raise TypeError("a must be an integer")

    if not isinstance(num2, int) or isinstance(num2, float):
        raise TypeError("b must be an integer")

    return num1 + num2

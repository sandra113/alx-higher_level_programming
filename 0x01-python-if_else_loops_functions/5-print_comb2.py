#!/usr/bin/python3

for i in range(0, 100):
    if i in range(0, 10):
        print("0{}, ".format(i), end='')
    elif i != 99:
        print("{}, ".format(i), end='')
    else:
        print(i)

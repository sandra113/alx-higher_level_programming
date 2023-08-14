#!/usr/bin/python3


"""
print a matrix integer
Parameters : matrix
"""


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in row:
            print("{:d}".format(num), end=" "if num != row[-1]else"")
        print()

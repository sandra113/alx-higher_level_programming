#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return list(map(lambda row: list(map(lambda i: i * i, row)), matrix))

#!/usr/bin/python3

def matrix_divided(matrix, div):
    for list_s in matrix:
        if not isinstance(list_s, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for i in list_s:
            if not isinstance(i , int) or isinstance(i, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    length = len(matrix[0])
    for row in matrix:
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) or isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round((i / div), 2) for i in list_s] for list_s in matrix]
            
    return new_matrix 

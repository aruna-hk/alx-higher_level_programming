#!/usr/bin/python3

""" module to divide elements of a matrix
    method(s):
        matrix_divided: prameters are matrix and divisor"""


def matrix_divided(matrix, div):
    if (type(matrix) is not list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    cpy = []
    for i in range(len(matrix)):
        if (type(matrix[i]) is not list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        row = []
        for j in range(len(matrix[i])):
            if ((type(matrix[i][j]) is not int) and (type(matrix[i][j]) is not float)):
                raise TypeError("Each row of the matrix must have the same size")
            if (div == 0):
                raise ZeroDivisionError("division by zero")
            j = 0
            row.append(round(matrix[i][j] / div, 2))
        cpy.append(row)
        j = 0
    return cpy

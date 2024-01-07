#!/bin/python3

""" this module contain a function to divide elemnts of  matrix """


def matrix_divided(matrix, div):
    """ divides elements of a matrix"""

    err = "matrix must be a matrix (list of lists) of integers/floats"
    for i in matrix:
        if (type(i) is not list):
            raise TypeError(err)
    _len = len(matrix[0])
    for j in matrix:
        if (len(j) != _len):
            raise TypeError("Each row of the matrix must have the same size")
    if (type(div) is not int and type(div) is not float):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    m_c = []
    for i in matrix:
        m_c.append(i[:])
    for r in range(len(m_c)):
        for c in range(len(m_c[r])):
            if (type(m_c[r][c]) is not int and type(m_c[r][c]) is not float):
                raise TypeError(err)
            m_c[r][c] /= div
            m_c[r][c] = round(m_c[r][c], 2)
    return m_c

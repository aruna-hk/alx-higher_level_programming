#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_m = []
    for i in range(len(matrix)):
        new_m.append([])
        for j in range(len(matrix[i])):
            new_m[i].append(matrix[i][j] ** 2)
    return new_m

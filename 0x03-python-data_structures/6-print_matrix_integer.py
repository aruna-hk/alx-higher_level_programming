#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if (matrix is None):
        return None
    for i in range(len(matrix)):
        j = 0
        for j in range(len(matrix[j])):
            print("{:d}".format(matrix[i][j]), end='')
            if (j != (len(matrix[j]) - 1)):
                print('', end=' ')
        print("")

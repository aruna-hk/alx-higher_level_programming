#!/usr/bin/python3
""" return list of numbers representing number n """


def pascal_triangle(n):
    """ pascal triangle """

    if (n <= 0):
        return []
    lis = []
    lis2 = []
    for i in range(1, n + 1):
        for j in range(i, i + 1):
            lis2.append(j)
        lis.append(lis2[:])
        lis2.clear

    return (lis)

#!/usr/bin/python3


""" print dimension of square with  #"""
def print_square(size):
    if (isinstance(size, int) is False):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must b >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        j = 0
        print('')

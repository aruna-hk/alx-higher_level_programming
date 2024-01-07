#!/usr/bin/python3

""" this module contains function to print square represatation
    using #
    """


def print_square(size):
    """ function prints square rep sing # """

    if (size < 0):
        raise ValueError("size must be >= 0")
    if (type(size) is not int):
        raise TypeError("size must be an integer")
    if (size == 0):
        print('')
        return
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print('')

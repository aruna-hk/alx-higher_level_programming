#!/usr/bin/python3


""" this module contain function to add two
    integers tgeher and return integer
"""

# function to perfome addition


def add_integer(a, b=98):

    """ add_integer function performs addition of whole integers
        and return int of a and b"""

    err_str = "{} must be an integer"
    if type(a) is chr or type(a) is str or a is None:
        raise TypeError(err_str.format("a"))
    if type(b) is chr or type(b) is str or b is None:
        raise TypeError(err_str.format("b"))
    return int(a) + int(b)

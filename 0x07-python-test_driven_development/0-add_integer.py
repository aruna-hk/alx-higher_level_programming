#!/usr/bin/python3

""" add two intergers and return sum

    methods:
        add_integer: takes two numbers and return sum
"""


def add_integer(a, b=98):

    """ adds two numbers
        a(int): integer argument
        b(int): integer argument  """

    if ((isinstance(a, int) is False) and (isinstance(a, float) is False)):
        raise (TypeError("a must be an integer"))
    if ((isinstance(b, int) is False) and (isinstance(b, float) is False)):
        raise (TypeError("b must be an integer"))
    return (int(a) + int(b))

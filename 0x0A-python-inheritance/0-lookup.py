#!/usr/bin/python3

"""  module to check attributes belonging to  class """


def lookup(obj):
    """ return list of class attributes"""

    return list(dir(obj))

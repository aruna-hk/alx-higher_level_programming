#!/usr/bin/python3

""" chech instance of object """


def is_same_class(obj, a_class):
    """ checks if obje is instance of class a_class """

    if isinstance(obj, a_class):
        return True
    else:
        return False

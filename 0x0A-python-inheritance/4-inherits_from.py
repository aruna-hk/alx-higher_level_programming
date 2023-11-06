#!/usr/bin/python3

""" check type of class or kindof  """


def inherits_from(obj, a_class):
    """ checks if object is instance of class a_class  + inherited"""

    if (issubclass(, a_class) is True):
        return True
    else:
        return False

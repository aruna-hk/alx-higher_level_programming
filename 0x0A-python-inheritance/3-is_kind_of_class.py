#!/usr/bin/python3

""" check type of class or kindof  """


def is_kind_of_class(obj, a_class):
    """ checks if object is instance of class a_class  + inherited"""

    if isinstance(obj, a_class):
        return True
    else:
        return False

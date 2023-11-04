#!/usr/bin/python3

"""exception handling"""


def safe_print_integer_err(value):
    """ safe print interger"""

    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False

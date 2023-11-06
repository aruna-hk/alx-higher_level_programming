#!/usr/bin/python3

""" BaseGeometry module """


class BaseGeometry:
    """ nothing in this class """

    def area(self):
        """ area method"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer validator method """

        if (type(value) is not int):
            raise TypeError(f"{name} must be an integer")
        if (value <= 0):
            raise ValueError(f"{name} must be greater than 0")

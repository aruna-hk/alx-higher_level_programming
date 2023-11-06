#!/usr/bin/python3
""" module rectangle inherites base geometry """


class Rectangle(__import__('7-base_geometry').BaseGeometry):
    """ class rectangle inherits from bas geometry """

    def __init__(self, width, height):
        self.integer_validator(self.__name__, width);
        self.integer_validator(self.__name__, height);
        self.__width = width
        self.__height

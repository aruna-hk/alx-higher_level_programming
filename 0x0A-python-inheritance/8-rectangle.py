#!/usr/bin/python3
""" module rectangle inherites base geometry """


class Rectangle(__import__('7-base_geometry').BaseGeometry):
    """ class rectangle inherits from bas geometry """

    def __init__(self, width, height):
        """ init method """

        __import__('7-base_geometry').BaseGeometry.__init__
        self.integer_validator(None, width)
        self.integer_validator(None, height)
        self.__width = width
        self.__height = height

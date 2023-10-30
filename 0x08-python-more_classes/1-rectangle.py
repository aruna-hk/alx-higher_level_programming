#!/usr/bin/python3

""" class module"""


class Rectangle:
    """ defin rectagle objct nd perform rectangle operations
        methods:
            width: setter and getter for the width
            height: setter and getter for the height
    """

    def __init__(self, width=0, height=0):
        """init method"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width getter"""
        return (self.__width)

    @property
    def height(self):
        """height getter"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """height setter"""
        if ((isinstance(value, int)) is False):
            raise (TypeError("height must be an integer"))
        if (value < 0):
            raise (ValueError("height must be >= 0"))
        self.__height = value

    @width.setter
    def width(self, value):
        """width setter"""
        if (isinstance(value, int) is False):
            raise (TypeError("width must be an integer"))
        if (value < 0):
            raise (ValueError("width must be >= 0"))
        self.__width = value

#!/usr/bin/python3

""" class module"""


class Rectangle:
    """ class rectangle define width and height"""

    def __init__(self, width=0, height=0):
        """init method"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""

        return (self.__width)

    @width.setter
    def width(self, value):
        """width setter"""

        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

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

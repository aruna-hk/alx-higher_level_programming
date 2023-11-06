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

    def area(self):
        """ return area of rectangle """

        return self.__width * self.__height

    def __str__(self):
        """ string reepresentation"""

        return f"[Rectangle] {self.__width}/{self.__height}"

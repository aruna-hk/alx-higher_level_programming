#!/usr/bin/python3

""" class module

    perform operation on retangle
    functions:
        width:getter and setter functions
        area: return area of the perimeter
        perimeter: return perimeter of the rectangle

"""


class Rectangle:

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

    def area(self):
        """ compute are of rectangle """
        return ((self.__width) * (self.__height))

    def perimeter(self):
        """ compute perimeter of rectngle"""
        return ((2 * self.__width) + (2 * self.__height))

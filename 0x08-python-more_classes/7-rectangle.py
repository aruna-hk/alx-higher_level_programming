#!/usr/bin/python3

""" class module"""


class Rectangle:
    """ class rectangle define and recangle functions"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """init method"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):

        """compute area of rectangle"""
        return (self.height * self.width)

    def perimeter(self):
        """compute perimeter of rectangle"""

        if ((self.width == 0) or (self.height == 0)):
            return 0
        return (2 * (self.width + self.height))

    def __str__(self):
        """String representation of the object"""

        lis = []
        if ((self.width == 0) or (self.height == 0)):
            st = ''.join(str(i) for i in lis)
            return st
        for i in range(self.__height):
            for j in range(self.__width):
                lis.append(self.print_symbol)
            if (i != (self.__height - 1)):
                lis.append('\n')
        return ''.join(str(i) for i in lis)

    def __repr__(self):
        """actual object representation """

        o = "{}".format(self.__class__.__name__)
        p = "({}, {})".format(self.__width, self.__height)
        return o + p

    def __del__(self):
        """delete object"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

#!/usr/bin/python3

""" square module """


class Square(__import__('9-rectangle').Rectangle):
    """class square """

    def __init__(self, size):
        """ init method"""

        self.integer_validator(None, size)
        self.__size = size
        __import__('9-rectangle').Rectangle.__init__(self, size, size)

    def area(self):
        """ perform area of square """

        return self.__size ** 2

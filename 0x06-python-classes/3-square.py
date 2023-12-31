#!/usr/bin/python3


"""
    class square creates an object with private attriute size
"""


class Square:
    """ square class does nothing

        Attrubutes:
            size (int): to instatiate private size attribute
    """
    def __init__(self, size=0):
        """ init function -instaiates orcts attributes

            args:
                size (int): instatiate private size attribute
        """
        if (type(size) is not int):
            raise (TypeError("size must be an integer"))
        if (size < 0):
            raise (ValueError("size must be >= 0"))
        self.__size = size

    def area(self):
        """ area - return square of private self """
        if (type(self.__size) is not int):
            raise (TypeError("size must be an integer"))
        if (self.__size < 0):
            raise (ValueError("size must be >= 0"))
        return self.__size ** 2

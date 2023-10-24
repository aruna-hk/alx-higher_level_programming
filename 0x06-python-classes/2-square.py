#!/usr/bin/python3


"""
    class square creates an object with private attriute size
"""


class Square:
    """ square class does nothing

        Attrubutes:
            size (int): to instatiate private size attribute
        args:
            size (int): instatiate private size attribute
    """
    def __init__(self, size=0):
        if (type(size) is not int):
            raise(TypeError("size must be an integer"))
        if (size < 0):
            raise(ValueError("size must be >= 0"))
        self.__size = size

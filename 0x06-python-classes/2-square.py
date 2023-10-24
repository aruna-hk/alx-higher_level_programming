#!/usr/bin/python3
"""
    class square creates an object with private attriute size
"""


class Square:
    """ square class does nothing

        Attrubutes:
            size (int): to instatiate private size attribute
        args:
            size: no type
    """
    def __init__(self, size=0):
        self.__size = size

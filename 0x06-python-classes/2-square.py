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
        if isinstance(size, int):
            if (size < 0):
                raise(ValueError("size must be >= 0"))
            else:
                self.__size = size
        else:
            raise(TypeError("size must be an integer"))

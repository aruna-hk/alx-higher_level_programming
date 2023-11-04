#!/usr/bin/python3


"""
    class square creates an object with private attriute size
"""


class Square:
    """ square class does nothing

        Attrubutes:
            size (int): to instatiate private size attribute
    """
    def __init__(self, size=0, position=(0, 0)):
        """ init function -instaiates orcts attributes

            args:
                size (int): instatiate private size attribute
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
        if (type(position) is not tuple or len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(position[0]) is not int or type(position[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """ area - return square of private self """
        return (self.__size ** 2)

    @property
    def size(self):
        """ getter """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ size - setter
            args:
                value: value to set size to
        """
        if (type(value) is not int):
            raise TypeError("size must be integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """ print square """
        if (self.__size == 0):
            print("")
        print("")
        for i in range(self.__size):
            for i in range(self.__size):
                print("#", end='')
            print("")
        print("")

    @property
    def position(self):
        """ position getter """
        return (self.__position)

    @position.setter
    def position(self, value):
        if (isinstance(value, tuple) is not True):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

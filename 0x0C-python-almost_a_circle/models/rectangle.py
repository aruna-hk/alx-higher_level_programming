#!/usr/bin/python3
""" rectangle class model rectangle  object"""


class Rectangle(__import__("base").Base):
    """ class rectagle inherits class BASE"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class contructor"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """return width"""

        return self.__width

    @width.setter
    def width(self, width):
        """ change/set the value of width"""

        if (type(width) is not int):
            raise TypeError("width must be an integer")
        if (width <= 0):
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """return height"""

        return self.__height

    @height.setter
    def height(self, height):
        """ change/set the value of height"""

        if (type(height) is not int):
            raise TypeError("height must be an integer")
        if (height <= 0):
            raise ValueError("height must be > 0")

        self.__height = height

    @property
    def x(self):
        """return x cordiate"""

        return self.__x

    @x.setter
    def x(self, x):
        """ change/set the value of x coordinate"""

        if (type(x) is not int):
            raise TypeError("x must be an integer")
        if (x < 0):
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """return y coordinate"""

        return self.__y

    @y.setter
    def y(self, y):
        """ change/set the value of y coordinate"""

        if (type(y) is not int):
            raise TypeError("y must be an integer")
        if (y < 0):
            raise ValueError("y must be >= 0")

        self.__y = y

    def area(self):
        """ compute area of rectangle """

        return self.width * self.height

    def display(self):
        """ print rectangle representation """

        for i in range(self.y):
            print("")
        for i in range(self.height):
            print(" " * self.x, end='')
            for j in range(self.width):
                print("{}".format("#"), end='')
            print("")

    def __str__(self):
        """string representation of rectangle """

        st = "[{}] ({}) ".format(self.__class__name, self.id)
        st2 = "{}/{} - {}/{}".format(self.x, self.y, self.width, self.height)
        return st + st2

    def update(self, *args, **kwargs):
        """update instance attributes with variable args"""

        lis = list(args)
        if (args is not None and len(lis) > 0):
            try:
                self.id = lis[0]
                self.width = lis[1]
                self.height = lis[2]
                self.x = lis[3]
                self.y = lis[4]
            except Exception as e:
                pass
        elif kwargs is not None:
            for k, v in kwargs.items():
                if (k == "height"):
                    self.height = v
                if (k == "width"):
                    self.width = v
                if (k == "x"):
                    self.x = v
                if (k == "y"):
                    self.y = v
                if (k == "id"):
                    self.id = v
        else:
            pass

    def to_dictionary(self):
        """ return object attributes in dictionary """

        dic = {}
        dic["id"] = self.id
        dic["width"] = self.width
        dic["height"] = self.height
        dic["x"] = self.x
        dic["y"] = self.y

        return dic

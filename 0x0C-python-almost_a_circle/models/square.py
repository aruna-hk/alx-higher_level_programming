#!/usr/bin/python3
""" class rectangle inherit class rectangle whih inherits from class  Base """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class model square """

    def __init__(self, size, x=0, y=0, id=None):
        """initializer """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ string represntation """

        st = "[{}] ({}) ".format(self.__class__.__name__, self.id)
        st2 = "{}/{} - {}".format(self.x, self.y, self.height)
        return st + st2

    @property
    def size(self):
        """ return size of square"""

        return self.width

    @size.setter
    def size(self, size):
        """ set size of square """

        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """update square model """

        lis = list(args)
        if (args is not None and len(lis) > 0):
            try:
                self.id = lis[0]
                self.width = lis[1]
                self.height = lis[1]
                self.x = lis[2]
                self.y = lis[3]
            except Exception as e:
                pass
        elif kwargs is not None:
            for k, v in kwargs.items():
                if (k == "size"):
                    self.height = v
                if (k == "size"):
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
        """ return dictionary of state of square model """

        dic = {}
        dic["id"] = self.id
        dic["size"] = self.width
        dic["x"] = self.x
        dic["y"] = self.y
        return dic

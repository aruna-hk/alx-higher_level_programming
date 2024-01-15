#!/usr/bin/python3
""" base class test module"""


import unittest
import json
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class Test_base(unittest.TestCase):
    """ test base class """

    def setUp(self):
        """ perform object initialization """

        self.base = Base()

    def test_object_instance(self):
        """test creation of base class instance"""

        self.assertTrue(isinstance(self.base, Base))

    def test_id(self):
        """ test id instance variable """

        self.assertEqual(self.base.id, 1)

    def test_passed_id(self):
        """ test id whe id is passed """

        base2 = Base(45)
        self.assertEqual(base2.id, 45)

    def test_recreateobj(self):
        """ recreate object """

        rectangle = Rectangle(1, 2, 3, 4, 5)
        dictionary = rectangle.to_dictionary()
        obj = Rectangle.create(**dictionary)
        self.assertFalse(obj == rectangle)
        self.assertFalse(obj is rectangle)

    def test_recreateobj_square(self):
        """ recreate object """

        sq = Square(4, 3, 6, 1)
        dictionary = sq.to_dictionary()
        obj = Square.create(**dictionary)
        self.assertFalse(obj == sq)
        self.assertFalse(obj is sq)


if __name__ == "__main__":
    unittest.main()

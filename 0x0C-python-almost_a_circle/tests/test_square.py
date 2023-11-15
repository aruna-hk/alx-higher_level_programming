#!/usr/bin/python3
""" class sqangle test case """
import unittest
from models.base import Base
from models.square import Square


class Test_base(unittest.TestCase):
    """ test base class """

    def setUp(self):
        """instatiate sqangle object"""

        self.sq = Square(3)

    def test_init_value(self):
        """test instatiation """

        self.sq.id = 1
        self.assertEqual(self.sq.id, 1)
        self.assertEqual(self.sq.size, 3)
        self.assertEqual(self.sq.x, 0)
        self.assertEqual(self.sq.y, 0)

    def test_validate_init(self):
        """test instatiation """

        with self.assertRaises(TypeError):
            self.sq.size = "xyz"
        with self.assertRaises(ValueError):
            self.sq.x = -1
        with self.assertRaises(ValueError):
            self.sq.y = -1
        with self.assertRaises(ValueError):
            self.sq.width = 0
        with self.assertRaises(ValueError):
            self.sq.height = 0

    def test_area(self):
        """test computation of area of sqangle"""

        self.sq.size = 10
        area = self.sq.area()
        self.assertEqual(area, 100)

    def test_str_(self):
        """ test print of object """

        self.sq.id = 1
        self.sq.size = 10
        self.sq.x = 0
        self.sq.y = 0

        x = self.sq.__str__()
        self.assertEqual(x, "[Square] (1) 0/0 - 10")

    def test_args(self):
        """ test updating with variable args"""

        self.sq.update(89)
        self.assertEqual(self.sq.id, 89)
        self.sq.update(89, 12)
        self.assertEqual(self.sq.size, 12)
        self.sq.update(89, 12, 1)
        self.assertEqual(self.sq.x, 1)
        self.sq.update(89, 12, 1, 1)
        self.assertEqual(self.sq.y, 1)

    def test_kwargs(self):
        """ test for key worded update"""

        self.sq.update(x=1)
        self.assertEqual(self.sq.x, 1)
        self.sq.update(y=1)
        self.assertEqual(self.sq.y, 1)
        self.sq.update(size=9)
        self.assertEqual(self.sq.size, 9)

    def test_to_dictionary(self):
        """ store object attributes in dictionary"""

        self.sq.id = 1
        self.sq.size = 10
        self.sq.x = 2
        self.sq.y = 1

        res_dic = {'id': 1, 'size': 10, 'x': 2, 'y': 1}
        dic = self.sq.to_dictionary()
        self.assertEqual(dic, res_dic)
        self.assertIsInstance(dic, dict)


if __name__ == "__main__":
    unittest.main()

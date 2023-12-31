#!/usr/bin/python3
""" class sqangle test case """
import unittest
from models.base import Base
from models.square import Square


class Test_base(unittest.TestCase):
    """ test base class """

    def test_init_size(self):
        """test instatiation size only """

        """ size  only  """
        sq = Square(1)
        self.assertEqual(sq.size, 1)
        self.assertEqual(sq.x, 0)
        self.assertEqual(sq.y, 0)
        self.assertEqual(sq.id, 10)

    def test_init_size_x(self):
        """test instatiation size and x coordinate"""

        sq = Square(1, 2)
        self.assertEqual(sq.size, 1)
        self.assertEqual(sq.x, 2)
        self.assertEqual(sq.y, 0)
        self.assertEqual(sq.id, 11)

    def test_init_size_x_y(self):
        """test instatiation size, x,y coordinate"""

        sq = Square(1, 2, 4)
        self.assertEqual(sq.size, 1)
        self.assertEqual(sq.x, 2)
        self.assertEqual(sq.y, 4)
        self.assertEqual(sq.id, 12)

    def test_init_size_x_y_id(self):
        """test instatiation size, x, y and id"""

        sq = Square(1, 2, 4, 99)
        self.assertEqual(sq.size, 1)
        self.assertEqual(sq.x, 2)
        self.assertEqual(sq.y, 4)
        self.assertEqual(sq.id, 99)

    def test_validate_init(self):
        """test instatiation of invalid types -- setters test """

        with self.assertRaises(TypeError):
            sq = Square("1")
        with self.assertRaises(TypeError):
            sq = Square(1, "2")
        with self.assertRaises(TypeError):
            sq3 = Square(1, 2, "4")
        with self.assertRaises(ValueError):
            sq3 = Square(-1)
        with self.assertRaises(ValueError):
            sq3 = Square(2, -5)
        with self.assertRaises(ValueError):
            sq3 = Square(2, 4, -5)
        with self.assertRaises(ValueError):
            sq3 = Square(0)

    def test_str_(self):
        """ test print of object """

        sq = Square(3, 1, 3, 8)
        x = sq.__str__()
        self.assertEqual(x, "[Square] (8) 1/3 - 3")

    def test_to_dictionary(self):
        """ store object attributes in dictionary"""

        sq = Square(3, 1, 3, 89)
        sq_dic = {'id': 89, 'size': 3, 'x': 1, 'y': 3}
        dic = sq.to_dictionary()
        self.assertIsInstance(dic, dict)
        self.assertEqual(dic, sq_dic)

    def test_update_ags(self):
        """ test updating with variable args"""

        sq = Square(10, 9, 0, 1)
        sq.update(89)
        self.assertEqual(sq.id, 89)
        sq.update(89, 12)
        self.assertEqual(sq.size, 12)
        sq.update(89, 12, 10)
        self.assertEqual(sq.x, 10)
        sq.update(89, 12, 10, 9)
        self.assertEqual(sq.y, 9)

    def test_kwargs(self):
        """ test for key worded update"""

        sq = Square(5, 3, 2, 22)
        sq.update(**{'id': 99})
        self.assertEqual(sq.id, 99)
        sq.update(**{'id': 99, 'size': 1})
        self.assertEqual(sq.size, 1)
        sq.update(**{'id': 99, 'size': 1, 'x': 2})
        self.assertEqual(sq.x, 2)
        sq.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(sq.y, 3)


if __name__ == "__main__":
    unittest.main()

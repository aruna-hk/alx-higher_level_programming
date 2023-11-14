#!/usr/bin/python3
"""class square tests"""
from models.rectangle import Rectangle
from models.square import Square as square
import unittest


class Test_square(unittest.TestCase):
    """ test base class """

    def test_creat(self):
        """test creation os square object"""

        s1 = square(3, 2, 3, 1)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.width, 3)
        self.assertEqual(s1.height, 3)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)

    def test_setter(self):
        """test size setter"""

        s1 = square(2, 2, 3, 1)
        self.assertEqual(s1.width, 2)
        s1.size = 4
        self.assertEqual(s1.width, 4)

    def test_to_dict(self):
        """ convert to dictionary """

        s1 = square(3, 1, 2, 1)
        dct = {'id': 1, 'x': 1, 'size': 3, 'y': 2}
        self.assertEqual(s1.to_dictionary(), dct)


if __name__ == "__main__":
    unittest.main()

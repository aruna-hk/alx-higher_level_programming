#!/usr/bin/python3
""" class rectangle test case """
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_base(unittest.TestCase):
    """ test base class """

    def setUp(self):
        """instatiate rectangle object"""

        self.rect = Rectangle(3, 2)

    def test_init_value(self):
        """test instatiation """

        self.rect.id = 1
        self.assertEqual(self.rect.id, 1)
        self.assertEqual(self.rect.width, 3)
        self.assertEqual(self.rect.height, 2)
        self.assertEqual(self.rect.x, 0)
        self.assertEqual(self.rect.y, 0)

    def test_validate_init(self):
        """test instatiation """

        with self.assertRaises(TypeError):
            self.rect.width = "xyz"
        with self.assertRaises(TypeError):
            self.rect.height = "yxy"
        with self.assertRaises(ValueError):
            self.rect.x = -1
        with self.assertRaises(ValueError):
            self.rect.y = -1
        with self.assertRaises(ValueError):
            self.rect.width = 0
        with self.assertRaises(ValueError):
            self.rect.height = 0

    def test_area(self):
        """test computation of area of rectangle"""

        self.rect.width = 10
        self.rect.height = 9
        area = self.rect.area()
        self.assertEqual(area, 90)

    def test_str_(self):
        """ test print of object """

        self.rect.id = 1
        self.rect.width = 10
        self.rect.height = 9
        self.rect.x = 0
        self.rect.y = 0

        x = self.rect.__str__()
        self.assertEqual(x, "[Rectangle] (1) 0/0 - 10/9")

    def test_args(self):
        """ test updating with variable args"""

        self.rect.update(89)
        self.assertEqual(self.rect.id, 89)
        self.rect.update(89, 12)
        self.assertEqual(self.rect.width, 12)
        self.rect.update(89, 12, 10)
        self.assertEqual(self.rect.height, 10)

    def test_kwargs(self):
        """ test for key worded update"""

        self.rect.update(x=1)
        self.assertEqual(self.rect.x, 1)
        self.rect.update(y=1)
        self.assertEqual(self.rect.y, 1)
        self.rect.update(id=1)
        self.assertEqual(self.rect.id, 1)

    def test_to_dictionary(self):
        """ store object attributes in dictionary"""

        self.rect.id = 1
        self.rect.width = 10
        self.rect.height = 9
        self.rect.x = 0
        self.rect.y = 0

        res_dic = {'id': 1, 'width': 10, 'height': 9, 'x': 0, 'y': 0}
        dic = self.rect.to_dictionary()
        self.assertEqual(dic, res_dic)
        self.assertIsInstance(dic, dict)


if __name__ == "__main__":
    unittest.main()

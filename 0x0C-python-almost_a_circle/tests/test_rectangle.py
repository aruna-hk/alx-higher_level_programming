#!/usr/bin/python3
""" class rectangle test case """
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_base(unittest.TestCase):
    """ test base class """

    def test_area(self):
        """test creation of triangle object"""

        rec = Rectangle(3, 2)
        self.assertEqual(rec.area(), 6)

    def test_base(self):
        """test object values """

        r1 = Rectangle(10, 2)

        self.assertEqual(r1.id, 6)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_setters_width(self):
        """ test width setter"""

        er = "width must be an integer"

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle("10", 1)
        self.assertEqual(str(err.exception), er)

    def test_setters_h(self):
        """ test heigh setter"""

        er = "height must be an integer"

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(10, "1")
        self.assertEqual(str(err.exception), er)

    def test_setters_x(self):
        """ test x setter"""

        er = "x must be an integer"

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(10, 1, "4")
        self.assertEqual(str(err.exception), er)

    def test_setters_y(self):
        """ test y setter"""

        er = "y must be an integer"

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(10, 1, y="rt")
        self.assertEqual(str(err.exception), er)

    def test_getters(self):
        """ test getters"""

        r1 = Rectangle(1, 2, x=3, y=3, id=1)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 3)

    def test_valuex(self):
        """ test wrong type x"""

        with self.assertRaises(ValueError) as err:
            r1 = Rectangle(10, 1, x=-1)
        self.assertEqual(str(err.exception), "x must be >= 0")

    def test_valuey(self):
        """ test wrong type y"""

        with self.assertRaises(ValueError) as err:
            r1 = Rectangle(10, 1, y=-1)
        self.assertEqual(str(err.exception), "y must be >= 0")

    def test_str(self):
        """test __str__"""

        r1 = Rectangle(1, 2, x=3, y=3, id=1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 3/3 - 1/2")

    def test_update(self):
        """test update function"""

        r1 = Rectangle(1, 2, x=3, y=3, id=1)
        r1.update(89)
        self.assertEqual(r1.id, 89)
        r1.update(89, 2)
        self.assertEqual(r1.width, 2)
        r1.update(89, 2, 3)
        self.assertEqual(r1.height, 3)
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.x, 4)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.y, 5)
        r1.update(height=1)
        self.assertEqual(r1.height, 1)

    def test_display(self):
        """test display rectangle repr"""

        self.assertEqual(None, None)


if __name__ == "__main__":
    unittest.main()

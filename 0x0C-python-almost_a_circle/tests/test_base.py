#!/usr/bin/python3
""" base class test file"""
import unittest
import json
from models.rectangle import Rectangle
from models.base import Base


class Test_base(unittest.TestCase):
    """ test base class """

    def setUp(self):
        """set up for test instantiate object with cof base class"""

        self.base = Base()

    def test_base(self):
        """test creation of base class instance"""

        self.assertEqual(self.base.id, 1)


if __name__ == "__main__":
    unittest.main()

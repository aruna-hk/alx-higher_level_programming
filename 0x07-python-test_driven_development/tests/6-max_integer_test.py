#!/usr/bin/python3

"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class text_max_integer(unittest.TestCase):
    """ class test max_integer function"""

    def test_correctvalues(self):
        """ test when value provided are all integers """

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_float_int(self):
        """ mixture of ins and floats """

        self.assertEqual(max_integer([10, 10.5, 3, 4]), 10.5)

    def test_list_empty(self):
        """ test when list is empty """

        self.assertEqual(max_integer(), None)

    def test_all_equal(self):
        """all elements equal"""

        self.assertEqual(max_integer([2, 2, 2]), 2)

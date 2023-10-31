import unittest
""" max inerger test"""

class TestMax_integerMethod:
    """  unitest for max_integer function"""


    def test_zero(self):
        """ case list is empy:"""

        self.assertEqual(__import__('6-max_integer').max_integer(list=[]), None)
    def test_order(self):
        """ case ordered elements in the list"""

        self.assertEqual(__import__('6-max_integer').max_integer([1, 2, 3, 4]), 4)

    def test_unorder(self):
        """ case unordered in the list """

        self.assertEqual(__import__('6-max_integer').max_integer([1, 65, 3, 7]), 65)


if __name__ == "__main__":
    unittest.main()

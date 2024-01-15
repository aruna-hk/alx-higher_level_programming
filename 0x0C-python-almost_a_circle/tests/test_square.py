#!/usr/bin/python3
""" test module for class square """
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRect(unittest.TestCase):
    """ testrect cals test square class """

    def setUp(self):
        """ object creation """

        self.square = Square(3, x=0, y=0, id=None)

    def test_dimension(self):
        """ check square dimensions """

        self.assertEqual(self.square.size, 3)

    def test_pos(self):
        """ test square position """

        self.assertEqual(self.square.x, 0)
        self.assertEqual(self.square.y, 0)

    def test_invalid_type(self):
        """ test initialization with invalid types """

        with self.assertRaises(TypeError):
            self.square.x = "string"

        with self.assertRaises(TypeError):
            self.square.y = "string"

        with self.assertRaises(TypeError):
            self.square.width = "string"

        with self.assertRaises(TypeError):
            self.square.height = "string"

        with self.assertRaises(ValueError):
            self.square.x = -1

        with self.assertRaises(ValueError):
            self.square.y = -3

        with self.assertRaises(ValueError):
            self.square.width = 0

        with self.assertRaises(ValueError):
            self.square.height = -10

    def test_areamethod(self):
        """ test the area method in square """

        self.assertEqual(self.square.area(), 9)

    def test_update(self):
        """ test update method """

        self.square.update(89, 8, 2, 3)
        self.assertEqual(self.square.size, 8)
        self.assertEqual(self.square.id, 89)

    def test_updatekwags(self):
        """ update key worded arguments """

        self.square.update(y=3, size=5, x=4, id=90)
        self.assertEqual(self.square.size, 5)
        self.assertEqual(self.square.y, 3)
        self.assertEqual(self.square.id, 90)

    def test_to_dictionary(self):
        """ test to dictionary method """

        self.square.update(90, 5, 3, 4)
        dic = {'x': 3, 'y': 4, 'id': 90, 'size': 5}
        dic2 = self.square.to_dictionary()
        self.assertIsInstance(dic2, dict)
        self.assertEqual(dic2, dic)

    def test_to_json(self):
        """ test conversion from pyobj to json obj """

        json_str = "[{\"x\": 3, \"width\": 89, \
        \"id\": 1, \"height\": 2, \"y\": 4}]"
        obj_json = Base.to_json_string([self.square.to_dictionary()])

    def test_save_to_file_read_from_file(self):
        """save object to a file inform of json object """

        jstr = Base.to_json_string([self.square.to_dictionary()])
        with open(self.square.__class__.__name__ + ".json", "w") as file:
            json.dump(jstr, file)
        with open(self.square.__class__.__name__ + ".json", "r") as file2:
            jobj = json.load(file2)
        self.assertEqual(jobj, jstr)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
""" test module for class rectangle """
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle


class TestRect(unittest.TestCase):
    """ testrect cals test rectangle class """

    def setUp(self):
        """ object creation """

        self.rectangle = Rectangle(3, 4)

    def test_dimension(self):
        """ check rectangle dimensions """

        self.assertEqual(self.rectangle.width, 3)
        self.assertEqual(self.rectangle.height, 4)

    def test_pos(self):
        """ test rectangle position """

        self.assertEqual(self.rectangle.x, 0)
        self.assertEqual(self.rectangle.y, 0)

    def test_invalid_type(self):
        """ test initialization with invalid types """

        with self.assertRaises(TypeError):
            self.rectangle.x = "string"

        with self.assertRaises(TypeError):
            self.rectangle.y = "string"

        with self.assertRaises(TypeError):
            self.rectangle.width = "string"

        with self.assertRaises(TypeError):
            self.rectangle.height = "string"

        with self.assertRaises(ValueError):
            self.rectangle.x = -1

        with self.assertRaises(ValueError):
            self.rectangle.y = -3

        with self.assertRaises(ValueError):
            self.rectangle.width = 0

        with self.assertRaises(ValueError):
            self.rectangle.height = -10

    def test_areamethod(self):
        """ test the area method in rectangle """

        self.assertEqual(self.rectangle.area(), 12)

    def test_update(self):
        """ test update method """

        self.rectangle.update(1, 89, 2)
        self.assertEqual(self.rectangle.width, 89)
        self.assertEqual(self.rectangle.height, 2)
        self.rectangle.update(1, 89, 2, 3, 4)
        self.assertEqual(self.rectangle.y, 4)

    def test_updatekwags(self):
        """ update key worded arguments """

        self.rectangle.update(y=3, width=5, x=4, id=89)
        self.assertEqual(self.rectangle.width, 5)
        self.assertEqual(self.rectangle.y, 3)
        self.assertEqual(self.rectangle.id, 89)

    def test_to_dictionary(self):
        """ test to dictionary method """

        self.rectangle.update(id=89, width=2, height=4, x=5, y=6)
        dic = {'x': 5, 'y': 6, 'id': 89, 'height': 4, 'width': 2}
        dic2 = self.rectangle.to_dictionary()
        self.assertIsInstance(dic2, dict)
        self.assertEqual(dic2, dic)

    def best_to_json(self):
        """ test conversion from pyobj to json obj """

        json_str = "[{\"x\": 3, \"width\": 89, \
        \"id\": 1, \"height\": 2, \"y\": 4}]"
        obj_json = Base.to_json_string([self.rectangle.to_dictionary()])

    def test_save_to_file_read_from_file(self):
        """save object to a file inform of json object """

        jstr = Base.to_json_string([self.rectangle.to_dictionary()])
        with open(self.rectangle.__class__.__name__ + ".json", "w") as file:
            json.dump(jstr, file)
        with open(self.rectangle.__class__.__name__ + ".json", "r") as file2:
            jobj = json.load(file2)
        self.assertEqual(jobj, jstr)


if __name__ == "__main__":
    unittest.main()

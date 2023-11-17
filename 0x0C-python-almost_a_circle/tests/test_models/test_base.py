#!/usr/bin/python3
""" base class test file"""
import unittest
import json
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class Test_base(unittest.TestCase):
    """ test base class """

    def test_base_init(self):
        """test creation of base class instance"""

        base = Base()
        self.assertEqual(base.id, 1)

    def test_increment_for_secod_obj(self):
        """test second incrementating class attribute for subsequent obj"""

        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 2)
        self.assertEqual(base2.id, 3)

    def test_set_id_at_init(self):
        """ set id at initializtion"""

        base3 = Base(98)
        self.assertEqual(base3.id, 98)

    def test_to_json(self):
        """ class attributes in dictionary to json string """

        self.sq = Square(3, id=9)
        self.rect = Rectangle(3, 4, id=9)
        rect_dict = self.rect.to_dictionary()
        sq_dict = self.sq.to_dictionary()
        obj_dict_list = []
        obj_dict_list.append(rect_dict)
        obj_dict_list.append(sq_dict)
        json_str = Base.to_json_string(obj_dict_list)
        self.assertEqual(json.dumps(obj_dict_list), json_str)
        return json_str

    def test_to_json_empty_list(self):
        """ empty list or None to json string """

        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")
        self.assertIsInstance(json_str, str)

    def test_from_json_string(self):
        """ converting from json string to pyoject"""

        json_str = self.test_to_json()
        self.assertIsInstance(json_str, str)
        py_object = Base.from_json_string(json_str)
        self.assertIsInstance(py_object, list)
        self.assertEqual(py_object, json.loads(json_str))

        """ none json str """
        self.assertEqual(Base.from_json_string(None), [])

        """ empty list """

        self.assertEqual(Base.from_json_string("[]"), [])

        """ str obj"""

        self.assertEqual(Base.from_json_string('[{"id": 89}]'), [{"id": 89}])


if __name__ == "__main__":
    unittest.main()

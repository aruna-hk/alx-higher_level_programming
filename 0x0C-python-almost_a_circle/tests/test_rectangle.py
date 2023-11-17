#!/usr/bin/python3
""" class rectangle test case """
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_base(unittest.TestCase):
    """ test base class """


    def test_init_value(self):
        """test instatiation """

        """ init width height """
        rect = Rectangle(1, 2);
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, 4)

    def test_init_w_h_x(self):
        """ test init width height x """

        rect1 = Rectangle(1, 2, 3);
        self.assertEqual(rect1.id, 5)
        self.assertEqual(rect1.width, 1)
        self.assertEqual(rect1.height, 2)
        self.assertEqual(rect1.x, 3)
        self.assertEqual(rect1.y, 0)

    def test_init_w_h_x_y(self):
        """ test init width height x y"""

        rect2 = Rectangle(1, 2, 3, 5);
        self.assertEqual(rect2.id, 6)
        self.assertEqual(rect2.width, 1)
        self.assertEqual(rect2.height, 2)
        self.assertEqual(rect2.x, 3)
        self.assertEqual(rect2.y, 5)


    def test_init_w_h_x_y_id(self):
        """ all attributes initialized """

        rect2 = Rectangle(1, 2, 3, 5, 98);

        self.assertEqual(rect2.id, 98)
        self.assertEqual(rect2.width, 1)
        self.assertEqual(rect2.height, 2)
        self.assertEqual(rect2.x, 3)
        self.assertEqual(rect2.y, 5)

    def test_validate_init(self):
        """test instatiation """

        with self.assertRaises(TypeError):
            rect3 = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            rect3 = Rectangle(1, "2")
        with self.assertRaises(TypeError):
            rect3 = Rectangle(1, 2, "4")
        with self.assertRaises(TypeError):
            rect3 = Rectangle(1, 2, 4, "str")
        with self.assertRaises(ValueError):
            rect3 = Rectangle(-1,5)
        with self.assertRaises(ValueError):
            rect3 = Rectangle(1, -5)
        with self.assertRaises(ValueError):
            rect3 = Rectangle(0, 5)
        with self.assertRaises(ValueError):
            rect3 = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            rect3 = Rectangle(1, 3, 4, -8)

    def test_area(self):
        """test computation of area of rectangle"""

        rect = Rectangle(10, 9, 0, 0, 100)
        area = rect.area()
        self.assertEqual(area, 90) 

    def test_str_(self):
        """ test print of object """

        rect = Rectangle(10, 9, 0, 0, 101)

        x = rect.__str__()
        self.assertEqual(x, "[Rectangle] (101) 0/0 - 10/9")

    def test_update_ags(self):
        """ test updating with variable args"""

        rect = Rectangle(10, 9, 0, 0, 1)
        rect.update(89)
        self.assertEqual(rect.id, 89)
        rect.update(89, 12)
        self.assertEqual(rect.width, 12)
        rect.update(89, 12, 10)
        self.assertEqual(rect.height, 10)
        rect.update(89, 12, 10, 2)
        self.assertEqual(rect.x, 2)
        rect.update(89, 12, 10, 2, 4)
        self.assertEqual(rect.y, 4)

    def test_kwargs(self):
        """ test for key worded update"""

        rect = Rectangle(10, 9, 0, 0, 1)
        rect.update(**{ 'id': 89 })
        self.assertEqual(rect.id, 89)
        rect.update(**{ 'id': 89, 'width': 1 })
        self.assertEqual(rect.width, 1)
        rect.update(**{'id': 89, 'width': 1, 'height': 2 })
        self.assertEqual(rect.height, 2)
        rect.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(rect.x, 3)
        rect.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(rect.y, 4)

    def test_to_dictionary(self):
        """ store object attributes in dictionary"""

        rect = Rectangle(10, 9, 0, 0, 1)

        res_dic = {'id': 1, 'width': 10, 'height': 9, 'x': 0, 'y': 0}
        dic = rect.to_dictionary()
        self.assertIsInstance(dic, dict)
        self.assertEqual(dic, res_dic)


    def test_create(self):
        """test creation of object """

        rect_dict = {'id': 89, 'width': 10, 'height': 4}
        rect_obj = Rectangle.create(**rect_dict)
        self.assertIsInstance(rect_obj, Rectangle)
        self.assertEqual(rect_obj.id, 89) 

        rect_dict = { 'id': 89, 'width': 1, 'height': 2, 'x': 3 }
        rect_obj = Rectangle.create(**rect_dict)
        self.assertIsInstance(rect_obj, Rectangle)
        self.assertEqual(rect_obj.width, 1)
 
        rect_dict = { 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 }
        rect_obj = Rectangle.create(**rect_dict)
        self.assertIsInstance(rect_obj, Rectangle)
        self.assertEqual(rect_obj.height, 2) 

    def test_save_to_file(self):
        """ save object to a file"""

        rect = Rectangle(10, 9, 0, 0, 1)
        dict_rect = rect.to_dictionary()

if __name__ == "__main__":
    unittest.main()

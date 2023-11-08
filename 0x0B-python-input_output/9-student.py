#!/usr/bin/python3
""" class student  json representation """
import json


class Student:
    """ class student attr firstname, lastname, age, to_json"""

    def __init__(self, first_name, last_name, age):
        """ return jason representation of class instance"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ return jason representation of class instance"""

        serializable = __import__('8-class_to_json').class_to_json
        return serializable(self)

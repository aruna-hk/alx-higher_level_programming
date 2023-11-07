#!/usr/bin/python3
""" class student  json representation """
import json


class Student:
    """ class student
    attributes:
    firstname, lastname, to_jso
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ return jason representation of class instance"""

        if attrs is None:
            return self.__dict__
        att = dict()
        for key in self.__dict__:
            if key in attrs:
                att[key] = self.__dict__[key]
        return att

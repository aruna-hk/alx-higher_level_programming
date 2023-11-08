#!/usr/bin/python3

""" class student  json representation """


class Student:
    """ class student attributes: firstname, lastname, to_json"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ return jason representation of class instance"""

        if attrs is None:
            return self.__dict__
        return {key:value for key, value in self.__dict__.items() if key in attrs}

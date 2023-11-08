#!/usr/bin/python3
""" class student  json representation """


class Student:
    """ class student attr firstname, lastname, age, to_json"""

    def __init__(self, first_name, last_name, age):
        """ return jason representation of class instance"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ return oject attributes for json srialization"""

        return self.__dict__

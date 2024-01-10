#!/usr/bin/python3
""" this module contains class student and to-json function
    that return dict representation of obj
"""


class Student:
    """ class student attr firstname, lastname, age, to_json"""

    def __init__(self, first_name, last_name, age):
        """ return jason representation of class instance"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ return oject attributes for json srialization"""

        if attrs is None or type(attrs) is not list:
            return self.__dict__
        else:
            new_dict = {}
            for key in attrs:
                if key in self.__dict__.keys():
                    new_dict[key] = self.__dict__[key]
            return new_dict

    def reload_from_json(self, json):
        """ update values of instance variables"""

        for key in json.keys():
            if key in self.__dict__.keys():
                self.__dict__[key] = json[key]

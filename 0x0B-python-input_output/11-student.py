#!/usr/bin/python3

""" class student  json representation """


class Student:
    """ class student attributes: firstname, lastname, to_json"""

    def __init__(self, first_name, last_name, age):
        """ initialize name and age on instatition"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ return jason representation of class instance"""

        if attrs is None:
            return self.__dict__
        return {k: v for k, v in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json):
        """ reload obect attributes from json file """

        for i in json.keys():
            if i in self.__dict__.keys():
                self.__dict__[i] = json[i]

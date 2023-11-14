#!/usr/bin/python3

""" base class of all classes/object in this package """
import json


class Base:
    """ attribute
            id: manage id object -- object attribute
            __nb_objects - class attribute: keep track of objcts created
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init method initialize id if not none"""

        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ convert to dictionary to json object """

        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save python object using JSON """
       
        with open(cls.__name__+".json", "w") as file:
            file.write('[')
            for i in list_objs:
                json.dump(i.to_dictionary(), file)
            file.write(']')

    @staticmethod
    def from_json_string(json_string):
        """ return list of python object from jason string"""

        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create object from attributes in dictionary """

        if cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls(1, 1)
        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """ load from json file """

        filename = cls.__name__ + ".json"
        with open(filename, "r") as file:
            j = file.read()
            return json.loads(j)
        return []

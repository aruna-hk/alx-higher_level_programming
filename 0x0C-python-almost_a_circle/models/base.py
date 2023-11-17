#!/usr/bin/python3

""" base class of all classes/object in this package """
import json
import csv


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

        with open(cls.__name__ + ".json", "w") as file:
            if list_objs is None or len(list_objs) == 0:
                file.write("[]")
            else:
                list_ob = []
                for i in list_objs:
                    list_ob.append(cls.to_dictionary(i))
                objs = Base.to_json_string(list_ob)
                file.write(objs)

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
        try:
            file = open(filename, "r")
            objlist = []
            pyobj = Base.from_json_string(file.read())
            for i in pyobj:
                objlist.append(cls.create(**i))
            file.close()
        except Exception as e:
            return []
        return objlist

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save python object using csv """

        with open(cls.__name__ + ".csv", "w") as file:
            if cls.__name__ == "Rectangle":
                header = ["id", "width", "height", "x", "y"]
            else:
                header = ["id", "size", "x", "y"]
            lis_t = []
            for i in list_objs:
                lis_t.append(i.to_dictionary())
            info = csv.DictWriter(file, fieldnames=header)
            info.writeheader()
            info.writerows(lis_t)

    @classmethod
    def load_from_file_csv(cls):
        """ Load from a CSV file and create objects """

        filename = cls.__name__ + ".csv"
        try:
            objlist = []
            file = open(filename, "r")
            pyobj = csv.DictReader(file)
            for i in pyobj:
                objlist.append(dict(i))
            ob = []
            for i in range(len(objlist)):
                for k, v in objlist[i].items():
                    objlist[i][k] = int(v)
            for i in objlist:
                ob.append(cls.create(**i))
            return ob
        except Exception as e:
            return []

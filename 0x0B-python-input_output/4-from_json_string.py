#!/usr/bin/python3
""" module - convert json object to python object"""
import json


def from_json_string(my_string):
    """Parse a JSON string and return the corresponding Python object.
        args:
            json string object
    """

    try:
        pobj = json.loads(my_string)
        return pobj
    except Exception as e:
        raise (e)

#!/usr/bin/python3
import json
""" module to convert python object to json object """


def from_json_string(my_str):
    """ convert json object to str object
    args:
        my_str(str)
    """

    return json.loads(my_str)

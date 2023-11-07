#!/usr/bin/python3
import json
""" module to convert python object to json object """


def from_json_string(my_str):
    """ convert json object to str object
    args:
        my_str(str)
    """

    try:
        x = json.loads(my_str)
        return x
    except Exception as e:
        raise ValueError(e)

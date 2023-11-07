#!/usr/bin/python3
""" module to convert string into jason object"""


import json


def to_json_string(my_obj):
    """ args:
           my object - python object
           return jason object
    """

    return (json.dumps(my_obj))

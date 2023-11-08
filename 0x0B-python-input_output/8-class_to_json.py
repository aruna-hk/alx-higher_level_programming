#!/usr/bin/python3
""" return serializable object fr json serialization"""


def class_to_json(obj):
    """ return oject attributes for json srialization"""

    if isinstance(obj, (int, str, bool, list, dict)):
        return obj
    else:
        return class_to_json(obj.__dict__)

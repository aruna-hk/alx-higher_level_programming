#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    if key is None:
        return a_dictionary
    try:
        del a_dictionary[key]
    finally:
        return a_dictionary

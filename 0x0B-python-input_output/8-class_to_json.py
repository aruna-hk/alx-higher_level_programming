#!/usr/bin/python3
""" take object and return its dictionary to e serialized y json"""
import json


def class_to_json(obj):
    """ return object dictioary to e serialized"""

    return obj.__dict__

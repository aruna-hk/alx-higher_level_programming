#!/usr/bin/python3
""" representing python class objct as json object """
import json


def class_to_json(obj):
    """ dumps python class object to json object """

    return json.dumps(obj.__dict__)

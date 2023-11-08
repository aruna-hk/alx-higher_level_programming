#!/usr/bin/python3
""" create jason file """
import json


def load_from_json_file(filename):
    """ create object from jason file"""

    with open(filename, "r", encoding='utf-8') as file:
        return json.loads(file.read())

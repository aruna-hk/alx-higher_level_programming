#!/usr/bin/python3
""" save json object to a file """
import json


def save_to_json_file(my_obj, filename):
    """ save json object in a file """

    with open(filename, "w", encoding='utf-8') as file:
        json.dump(my_obj, file)

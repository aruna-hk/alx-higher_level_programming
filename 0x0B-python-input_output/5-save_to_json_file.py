#!/usr/bin/python3
import json
""" dups json object to a file """


def save_to_json_file(my_obj, filename):
    """ save json object in a file """

    with open(filename, "w", encoding='utf-8') as file:
        json.dump(my_obj, file)

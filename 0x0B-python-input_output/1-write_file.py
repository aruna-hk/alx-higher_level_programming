#!/usr/bin/python3

""" open/create a file for writing"""


def write_file(filename="", text=""):
    """ open/create file for writing"""

    with open(filename, "w", encoding='utf-8') as file:
        return file.write(text)

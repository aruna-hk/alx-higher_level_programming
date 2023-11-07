#!/usr/bin/python3

""" open file to append """


def append_write(filename="", text=""):
    """ open file to append
        args:
            filename(str)
            text(str)
    """

    with open(filename, "a", encoding='utf-8') as file:
        return file.write(text)

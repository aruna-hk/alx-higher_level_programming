#!/usr/bin/python3

""" opening and reading file """


def read_file(filename=''):
    """ read file content """

    with open(filename, "r", encoding='utf-8') as file:
        print(file.read(), end='')

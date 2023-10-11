#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    dict2 = {}
    for key, value in a_dictionary.items():
        dict2[key] = value * 2
    return dict2

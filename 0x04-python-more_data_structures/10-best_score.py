#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxmarks = 0
    for i in a_dictionary:
        if (a_dictionary.get(i) > maxmarks):
            maxmarks = a_dictionary.get(i)
            student = i
    return student

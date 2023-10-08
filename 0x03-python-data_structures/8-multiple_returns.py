#!/usr/bin/python3


def multiple_returns(sentence):
    if (sentence is None):
        return 0, None
    c = sentence[0]
    lenl = len(sentence)
    return lenl, c

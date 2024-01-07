#!/usr/bin/python3

""" module contain function to ident string """


def text_indentation(text):
    """ text indentation function"""

    dell = ['.', '?', ':']
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        if i in dell:
            print(i)
            print('')
            continue
        print(i, end='')

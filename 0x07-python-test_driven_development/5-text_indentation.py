#!/usr/bin/python3

def text_indentation(text):
    if (isinstance(text, str) is False):
        raise TypeError("text must e string")
    for i in text:
        if (i == '.'):
            print('\n')
        if (i == '?'):
            print('\n')
        if (i == ':'):
            print('\n')
        print(i, end='')

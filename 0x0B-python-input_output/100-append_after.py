#!/usr/bin/python3

""" module perform search and insert """


def append_after(filename="", search_string="", new_string=""):
    """ search and insert function """

    with open(filename, mode="r", encoding='utf-8') as file:
        len_ = 0
        content = file.read()
        lines = content.split("\n")
        for line_no in range(len(lines)):
            if (search_string in lines[line_no]):
                idx = lines[line_no].index(search_string)
                lines[line_no] = lines[line_no] + '\n' + new_string
            elif (lines[line_no] != ''):
                lines[line_no] += '\n'

    with open(filename, mode='w', encoding='utf-8') as file:
        for i in lines:
            file.write(i)

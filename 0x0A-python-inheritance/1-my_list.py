#!/usr/bin/python3

""" this module contains class Mylist which inherits list calss """


class MyList(list):
    """ Mylist inherit from sorted class """

    def __init__(self):
        """ init method """

        list.__init__

    def print_sorted(self):
        """ print sorted list """

        print(sorted(self))

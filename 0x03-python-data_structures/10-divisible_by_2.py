#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if (my_list is None):
        return None
    list_l = [(i % 2 == 0) for i in range(len(my_list))]
    return list_l

#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    list_l = [(i % 2 == 0) for i in range(len(my_list))]
    return list_l

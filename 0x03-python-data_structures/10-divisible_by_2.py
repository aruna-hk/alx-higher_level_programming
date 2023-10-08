#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if (my_list is None):
        return None
    list_l = []
    for i in range(len(my_list)):
        if (my_list[i] % 2 == 0):
            list_l.append(True)
        else:
            list_l.append(False)
    return list_l

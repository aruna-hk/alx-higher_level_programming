#!/usr/bin/python3

def weight_average(my_list=[]):
    if ((my_list is None) or (len(my_list) == 0)):
        return 0
    total = 0
    num = 0
    for i in range(len(my_list)):
        total += my_list[i][1] * my_list[i][0]
        num += my_list[i][1]
    return total/num

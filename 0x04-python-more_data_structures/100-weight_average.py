#!/usr/bin/python3

def weight_average(my_list=[]):
    avg = 0
    if my_list is None:
        return 0
    total = 0
    t_weigh = 0
    for i in range(len(my_list)):
        total = total + (my_list[i][0] * my_list[i][1])
        t_weigh = t_weigh + my_list[i][1]
    avg = total / t_weigh
    return avg

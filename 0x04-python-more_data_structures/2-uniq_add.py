#!/usr/bin/python3


def uniq_add(my_list=[]):
    uniq_list = []
    sum_ = 0
    for i in range(len(my_list)):
        if (my_list[i] in uniq_list):
            continue
        sum_ += my_list[i]
        uniq_list.append(my_list[i])
    return (sum_)

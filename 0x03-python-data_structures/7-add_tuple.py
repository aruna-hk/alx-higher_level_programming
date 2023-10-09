#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    lis = []
    if (len(tuple_a) > len(tuple_b)):
        for i in range(len(tuple_a)):
            if(i > (len(tuple_b) - 1)):
                lis.append(tuple_a[i] + 0)
            else:
                lis.append(tuple_a[i] + tuple_b[i])
    elif (len(tuple_a) == len(tuple_b)):
        i = 0
        for i in range(len(tuple_a)):
            lis.append(tuple_a[i] + tuple_b[i])
    else:
        i = 0
        for i in range(len(tuple_b)):
            if (i > (len(tuble_a) - 1)):
                lis.append(tuple_b[i] + 0)
            else:
                lis.appen(tuple_b[i] + tuple_a[i])
    return tuple(lis)

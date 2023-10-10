#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    lis = []
    if (len(tuple_a) > len(tuple_b) and len(tuple_a) >= 2):
        for i in range(2):
            if(i > (len(tuple_b) - 1)):
                lis.append(tuple_a[i] + 0)
            else:
                lis.append(tuple_a[i] + tuple_b[i])
    elif (len(tuple_b) > len(tuple_a) and len(tuple_b) >= 2):
        i = 0
        for i in range(2):
            if (i > (len(tuple_a) - 1)):
                lis.append(tuple_b[i] + 0)
            else:
                lis.append(tuple_b[i] + tuple_a[i])
    elif (len(tuple_a) == len(tuple_b) and len(tuple_a) >= 2):
        i = 0
        for i in range(2):
            lis.append(tuple_a[i] + tuple_b[i])
    else:
        if (len(tuple_a) == len(tuple_b) and len(tuple_a) == 0):
            return (0, 0)
        elif (len(tuple_a) == 1 and len(tuple_b) == 0):
            lis.append(tuple_a[0])
            lis.append(0)
        elif (len(tuple_b) == 1 and len(tuple_a) == 0):
            lis.append(tuple_b[0])
            lis.append(0)
        else:
            lis.append(tuple_a[0] + tuple_b[0])
            lis.append(0)
    return tuple(lis)

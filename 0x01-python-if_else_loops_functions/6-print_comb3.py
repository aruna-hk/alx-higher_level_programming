#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if (j > i):
            print("{}{}".format(i, j), end="")
            if (j + i != 17):
                print("{}".format(", "), end="")
            else:
                print("{}".format(""))

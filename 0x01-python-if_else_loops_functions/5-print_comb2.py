#!/usr/bin/python3
for i in range(100):
    print(i, end="")
    if (i != 99):
        print("{}".format(", "), end="")
    if (i == 99):
        print("{}".format(""))

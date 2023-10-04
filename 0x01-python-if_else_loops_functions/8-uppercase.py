#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        j = ord(str[i])
        if (j < 123 and j > 96):
            char = chr(j - 32)
        else:
            char = str[i]
        print("{}".format(char), end="")
    print("{}".format(""))

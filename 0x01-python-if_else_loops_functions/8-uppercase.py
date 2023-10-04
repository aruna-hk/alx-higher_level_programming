#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        j = ord(str[i])
        if (j < 123 and j > 96):
            print("{}".format(chr(j - 32)), end="")
        else:
            print("{}".format(str[i]), end="")

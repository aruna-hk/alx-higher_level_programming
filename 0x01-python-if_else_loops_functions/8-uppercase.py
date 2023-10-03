#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        j = ord(str[i])
        if (j < 123 or j > 96):
            print(chr(j - 32), end="")
        else:
            print(str[i], end="");
uppercase("Best School 98 Battery street")

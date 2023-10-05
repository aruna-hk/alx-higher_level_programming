#!/usr/bin/python3
import sys


def argsadd():
    n = 0
    if (len(sys.argv) == 1):
        n = 0
    else:
        for i in range(1, len(sys.argv)):
            n = n + int(sys.argv[i])
    print(n)


if __name__ == "__main__":
    argsadd()

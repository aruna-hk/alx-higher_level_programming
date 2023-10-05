#!/usr/bin/python3
import sys


def calculator_():
    if (len(sys.argv) < 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if (len(sys.argv[2]) == 1 and sys.argv[2] == "+"):
        n = int(sys.argv[1]) + int(sys.argv[3])
        print("{} + {} = {}".format(sys.argv[1], sys.argv[3], n))
        return 0
    elif (len(sys.argv[2]) == 1 and sys.argv[2] == "-"):
        n = int(sys.argv[1]) - int(sys.argv[3])
        print("{} + {} = {}".format(sys.argv[1], sys.argv[3], n))
        return 0
    elif (len(sys.argv[2]) == 1 and sys.argv[2] == "*"):
        n = int(sys.argv[1]) * int(sys.argv[3])
        print("{} + {} = {}".format(sys.argv[1], sys.argv[3], n))
        return 0
    elif (len(sys.argv[2]) == 1 and sys.argv[2] == "/"):
        n = int(sys.argv[1]) / int(sys.argv[3])
        print("{} + {} = {}".format(sys.argv[1], sys.argv[3], n))
        return 0
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    calculator_()

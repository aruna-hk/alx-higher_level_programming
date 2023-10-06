#!/usr/bin/python3
import sys
import calculator_1

if (len(sys.argv) != 4):
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
if (len(sys.argv[2]) == 1 and sys.argv[2] == "+"):
    n = calculator_1.add(int(sys.argv[1]), int(sys.argv[3]))
    print("{} + {} = {}".format(sys.argv[1], sys.argv[3], n))
elif (len(sys.argv[2]) == 1 and sys.argv[2] == "-"):
    n = calculator_1.sub(int(sys.argv[1]), int(sys.argv[3]))
    print("{} + {} = {}".format(sys.argv[1], sys.argv[3], n))
elif (len(sys.argv[2]) == 1 and sys.argv[2] == "*"):
    n = calculator_1.mul(int(sys.argv[1]), int(sys.argv[3]))
    print("{} + {} = {}".format(sys.argv[1], sys.argv[3], n))
elif (len(sys.argv[2]) == 1 and sys.argv[2] == "/"):
    n = calculator_1.div(int(sys.argv[1]), int(sys.argv[3]))
    print("{} + {} = {}".format(sys.argv[1], sys.argv[3], n))
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

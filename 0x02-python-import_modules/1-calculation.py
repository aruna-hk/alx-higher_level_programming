#!/usr/bin/python3
import calculator_1


if __name__ == "__main__":
    a = 10
    b = 5
    print(str(a) + " + " + str(b) + " = " + str(calculator_1.add(a, b)))
    print(str(a) + " - " + str(b) + " = " + str(calculator_1.sub(a, b)))
    print(str(a) + " * " + str(b) + " = " + str(calculator_1.mul(a, b)))
    print(str(a) + " / " + str(b) + " = " + str(calculator_1.div(a, b)))

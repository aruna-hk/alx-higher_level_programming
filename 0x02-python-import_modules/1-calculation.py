#!/usr/bin/python3
def calc():
    import calculator_1
    a = 10
    b = 5
    n = calculator_1.add(a, b)
    print(str(a) + " + " + str(b) + " = " + str(n))
    n = calculator_1.sub(a, b)
    print(str(a) + " - " + str(b) + " = " + str(n))
    n = calculator_1.mul(a, b)
    print(str(a) + " * " + str(b) + " = " + str(n))
    n = calculator_1.div(a, b)
    print(str(a) + " / " + str(b) + " = " + str(n))


if __name__ == "__main__":
    calc()

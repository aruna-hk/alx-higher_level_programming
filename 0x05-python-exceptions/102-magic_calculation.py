#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            result += (a + b)
            break
        except Exception:
            if (a > i):
                raise Exception("Too far")
            else:
                result += (a ** b) / i
        finally:
            break
    return result

#!/usr/bin/python3


def roman_to_int(roman_string):
    if (roman_string is None):
        return 0
    romc = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if (type(roman_string) is not str):
        return 0
    roman_string.upper()
    num = 0
    prev = 0
    current = 0
    strlen = len(roman_string)
    for i in range(len(roman_string)):
        if (roman_string[i] in romc):
            current = romc[roman_string[i]]
            if (current > prev):
                num = num - prev + current - prev
            else:
                num = num + current
            prev = current
        else:
            return 0
    return num

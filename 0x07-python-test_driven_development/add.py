#!/usr/bin/python3

""" contain function to add two numbers
    >>> n =  add(1, 3)
    >>> j = sub(1, 3)
"""
def add(a, b):
    """
        >>> n = add(1, 4)
    """
    return (a + b)

def sub(a, b):
    """
        >>> j = sub(1,3);
    """
    return (a - b)
if __name__ == "__main__":
    import doctest
    doctest.testmod();

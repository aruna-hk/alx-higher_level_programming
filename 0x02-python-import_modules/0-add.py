#!/usr/bin/python3
def imp():
    a = 1
    b = 2
    import add_0
    print("{} + {} = {}".format(a, b, add_0.add(a, b)))


if __name__ == "__main__":
    imp()

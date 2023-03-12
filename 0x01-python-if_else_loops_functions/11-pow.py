#!/usr/bin/python3

def pow(a, b):
    if b > 0:
        return pow(a, b)
    elif b == 0:
        return 1
    return 1 / powr(a, b * -1)


def powr(a, b):
    if b < 1:
        return 1
    return a * powr(a, b - 1)


print(pow(2, 3))
print(pow(2, -3))
print(pow(1, 3))
print(pow(1, -3))
print(pow(1, 0))

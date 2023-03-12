#!/usr/bin/python3

def pow(a, b):
    if b < 1:
        return 1
    return a * pow(a, b - 1)

#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a = 0
    b = 0

    if 0 < len(tuple_a):
        a += tuple_a[0]
    if 0 < len(tuple_b):
        a += tuple_b[0]
    if 1 < len(tuple_a):
        b += tuple_a[1]
    if 1 < len(tuple_b):
        b += tuple_b[1]

    return (a, b)

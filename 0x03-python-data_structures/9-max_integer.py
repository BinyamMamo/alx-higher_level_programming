#!/usr/bin/python3

def max_integer(my_list=[]):
    max = my_list[0] if 0 < len(my_list) else "None"
    for x in my_list:
        if x > max:
            max = x
    return max

#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = []
    for x in my_list:
        # x % 2 is 0(False) for odd numbers
        new_list.append(not x % 2)
    return new_list

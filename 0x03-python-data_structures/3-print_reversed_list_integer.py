#!/usr/bin/python3

# This is a comment
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for x in my_list:
        print("{:d}".format(x))

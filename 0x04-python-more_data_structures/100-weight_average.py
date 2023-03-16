#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list is None or not len(my_list):
        return 0
    sum = 0
    div = 0
    for item in my_list:
        sum += item[0] * item[1]
        div += item[1]
    if not div:
        return sum
    return sum / div


# my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
# # = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
# result = weight_average(my_list)
# print("Average: {:0.2f}".format(result))

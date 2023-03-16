#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted = list(a_dictionary.keys())
    state = True
    print(sorted)
    if check_sort(sorted) >= len(sorted) - 1:
        state = False
    while state is True:
        for i in range(0, len(sorted)):
            if i + 1 < len(sorted) and sorted[i] > sorted[i + 1]:
                sorted[i], sorted[i + 1] = sorted[i + 1], sorted[i]
            if check_sort(sorted) >= len(sorted) - 1:
                state = False
                break
            i += 1
    for key in sorted:
        print(f"{key}: ", end="")
        if type(a_dictionary.get(key)) is dict:
            print(a_dictionary.get(key))
        else:
            print(a_dictionary.get(key))


def check_sort(my_list=[]):
    count = 0
    for i in range(len(my_list)):
        if i + 1 < len(my_list) and my_list[i + 1] > my_list[i]:
            count += 1
    return count


# car = {
#     # "manufacturer": "Toyota",
#     "brand": "Ford",
#     # "akefafay": "me",
#     "model": "Mustang",
#     "year": "1964"
# }

# sorter(car)
# todo
#! how to check if a list is empty
# done

# a_dictionary = {'language': "C", 'Number': 89,
#                 'track': "Low level", 'ids': {3, 2, 1}}
# print_sorted_dictionary(a_dictionary)

#!/usr/bin/python3

# print_sorted_dictionary = \
#     __import__('6-print_sorted_dictionary').print_sorted_dictionary


def multiply_by_2(a_dictionary):
    if a_dictionary is None or not len(a_dictionary):
        return None
    copy = a_dictionary.copy()
    for key in copy.keys():
        copy[key] = copy[key] * 2
    return copy


# a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
# print_sorted_dictionary(a_dictionary)
# print("--")
# new_dict = multiply_by_2(a_dictionary)
# print_sorted_dictionary(new_dict)

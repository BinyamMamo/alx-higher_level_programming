#!/usr/bin/python3

# print_sorted_dictionary = \
#     __import__('6-print_sorted_dictionary').print_sorted_dictionary


def multiply_by_2(a_dictionary):
    new_values = list(map(lambda x: x * 2, a_dictionary.values()))
    for key, new_val in zip(a_dictionary.keys(), new_values):
        a_dictionary[key] = new_val
    return a_dictionary


# a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
# print_sorted_dictionary(a_dictionary)
# print("--")
# new_dict = multiply_by_2(a_dictionary)
# print_sorted_dictionary(new_dict)

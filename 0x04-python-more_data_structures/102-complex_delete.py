#!/usr/bin/python3

# print_sorted_dictionary = \
#     __import__('6-print_sorted_dictionary').print_sorted_dictionary


def complex_delete(a_dictionary, value):
    if a_dictionary is None or not len(a_dictionary):
        return a_dictionary
    key = list(a_dictionary.keys())
    for i in range(len(key)):
        if a_dictionary[key[i]] == value:
            del a_dictionary[key[i]]
        i += 1
    return a_dictionary


# a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
# new_dict = complex_delete(None, 'C')
# print_sorted_dictionary(a_dictionary)
# print("--")
# print_sorted_dictionary(new_dict)

# print("--")
# print("--")
# new_dict = complex_delete(a_dictionary, [1, 2, 3])
# print_sorted_dictionary(a_dictionary)
# print("--")
# print_sorted_dictionary(new_dict)

# print("--")
# print("--")
# new_dict = complex_delete(a_dictionary, "Low")
# print_sorted_dictionary(a_dictionary)
# print("--")
# print_sorted_dictionary(new_dict)

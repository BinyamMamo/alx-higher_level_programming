#!/usr/bin/python3

def search_replace(my_list, search, replace):
    copy = my_list.copy()
    for i in range(len(copy)):
        if copy[i] == search:
            copy[i] = replace
    return copy


# my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
# new_list = search_replace(my_list, 2, 89)

# print(new_list)
# print(my_list)

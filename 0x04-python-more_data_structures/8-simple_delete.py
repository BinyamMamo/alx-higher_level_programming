#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if key in a_dictionary.keys():
        del a_dictionary[key]
    return a_dictionary


# car = {
#     # "manufacturer": "Toyota",
#     "brand": "Ford",
#     # "akefafay": "me",
#     "model": "Mustang",
#     "year": "1964"
# }

# print(simple_delete(car, "brandy"))
# print("---")
# print(car)

#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or not len(a_dictionary):
        return None
    max = list(a_dictionary.keys())[0]
    for key in a_dictionary.keys():
        if a_dictionary[key] > a_dictionary[max]:
            max = key
    return max


# a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
# best_key = best_score(a_dictionary)
# print("Best score: {}".format(best_key))

# best_key = best_score(None)
# print("Best score: {}".format(best_key))

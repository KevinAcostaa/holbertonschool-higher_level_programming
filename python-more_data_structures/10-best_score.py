#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == 0:
        return None
    key_max, maxim = list(a_dictionary.items())[0]
    for key, value in a_dictionary.items():
        if value > max:
            maxim = value
            key_max = key
    return key_max

#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dictionary = sorted(a_dictionary)
    for i in sorted_dictionary:
        print(f"{i}: {a_dictionary[i]}")

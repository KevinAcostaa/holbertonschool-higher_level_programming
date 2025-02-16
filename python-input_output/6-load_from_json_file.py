#!/usr/bin/python3
"""
function is declared
"""
import json


def load_from_json_file(filename):
    """
    create obj
    """
    with open(filename, 'r') as file:
        my_obj = json.load(file)
        return my_obj

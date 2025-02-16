#!/usr/bin/python3
"""
function is declared
"""
import json


def save_to_json_file(my_obj, filename):
    """
    object a text
    """
    my_obj_str = json.dumps(my_obj)
    with open(filename, 'w') as file:
        file.write(my_obj_str)

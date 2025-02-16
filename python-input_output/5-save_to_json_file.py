#!/usr/bin/python3
"""
function is declared
"""
import json


def save_to_json_file(my_obj, filename):
    """
    object a text
    """
    if isinstance(my_obj, set):
        my_obj_str = list(my_obj)

    my_obj_str = json.dumps(my_obj)
    with open(filename, 'w') as file:
        try:
            file.write(my_obj_str)
        finally:
            file.close()

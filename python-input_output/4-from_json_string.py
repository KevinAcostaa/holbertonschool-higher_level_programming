#!/usr/bin/python3
"""
function is declared
"""
import json


def from_json_string(my_str):
    """
    string a object
    """
    json_object = json.loads(my_str)
    return json_object

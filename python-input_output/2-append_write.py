#!/usr/bin/python3
"""
function is declared
"""


def append_write(filename="", text=""):
    """
    function
    """
    with open(filename, 'a') as file:
        file.write(text)
    return len(text)

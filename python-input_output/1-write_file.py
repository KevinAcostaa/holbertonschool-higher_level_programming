#!/usr/bin/python3
"""
read_file function is declared
"""


def write_file(filename="", text=""):
    """
    function open and write
    """
    with open(filename, 'w') as file:
        file.write(text)
    return len(text)

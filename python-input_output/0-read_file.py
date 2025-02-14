#!/usr/bin/python3
"""
read_file function is declared
"""


def read_file(filename=""):
    """
    function
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content, end="")

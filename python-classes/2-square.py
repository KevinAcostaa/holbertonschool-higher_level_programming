#!/usr/bin/python3
"""
class Square
"""


class Square:
    """
    class Square
    """
    def __init__(self, size=0):
        """
        init Square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

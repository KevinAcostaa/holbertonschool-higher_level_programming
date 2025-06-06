#!/usr/bin/python3
"""
class Rectangle
"""


class Rectangle():
    """
    class Square
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return self.__height + self.__width + self.__height + self.__width

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ''
        return (('#' * self.width + '\n') * self.height)[:-1]

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

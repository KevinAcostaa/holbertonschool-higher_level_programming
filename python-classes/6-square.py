#!/usr/bin/python3
"""
class Square
"""


class Square():
    """
    class Square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        init Square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        string = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple:
            raise TypeError(f"{string}")
        for i in value:
            if type(i) is not int or i < 0 or len(value) != 2:
                raise ValueError("")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print(" " * self.position[0] + "#" * self.__size)

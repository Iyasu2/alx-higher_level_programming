#!/usr/bin/python3

"""
    This module contains the class square
"""


class Square:
    """
        This is a class that takes as attribute the size of the square.
    """
    def __init__(self, size=0):
        self.size = size

    """
        This is a property getter function
    """
    @property
    def size(self):
        return self.__size

    """
        This is a property setter function
    """
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = value

    """
        This is a method that returns the square of the attribute size.
    """
    def area(self):
        return self.__size ** 2

    """
        This is a method that prints the square of the attribute size.
    """
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()

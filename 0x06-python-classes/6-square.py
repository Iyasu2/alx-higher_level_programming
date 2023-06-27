#!/usr/bin/python3

"""
    This module contains the class square
"""


class Square:
    """
        This is a class with attribute size and position.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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
        This is a property getter function
    """
    @property
    def position(self):
        return self.__position

    """
        This is a property setter function
    """
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
            not all(isinstance(i, int) for i in value) or \
                not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(' ' * self.__position[0], end='')
            print('#' * self.__size)

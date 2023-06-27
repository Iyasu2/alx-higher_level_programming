#!/usr/bin/python3

"""
    This module contains the class square
"""


class Square:
    """
        This is a class that takes as attribute the size of the square.
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

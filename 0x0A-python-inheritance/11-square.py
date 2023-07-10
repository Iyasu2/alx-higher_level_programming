#!/usr/bin/python3
'''
this module contains a
class that inherits from
rectangle
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        '''
        this is instantiation method
        '''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        '''
        returns the area of the square
        '''
        return self.__size * self. __size
    
    def __str__(self):
        '''
        returns the string representation of the square
        '''
        return "[Square] {}/{}".format(self.__size, self.__size)

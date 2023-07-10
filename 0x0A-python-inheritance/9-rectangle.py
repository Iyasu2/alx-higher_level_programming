#!/usr/bin/python3
'''
this module contains a class
Rectangle that inherits from the class
BaseGeometry
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    this is the class Rectangle
    '''
    def __init__(self, width, height):
        '''
        this is an instantiation with method
        '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''
        Return the area of the rectangle
        '''
        return self.__width * self.__height

    def __str__(self):
        '''
        Return a string representation of the rectangle
        '''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

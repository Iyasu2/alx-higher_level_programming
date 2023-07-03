#!/usr/bin/python3

'''
    This is a module which defines a class
    The class is called Rectangle
    it has two methods
'''


class Rectangle:
    '''
        this class has two attributes
    '''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    '''
        this is an init method initializing width
        and height
    '''
    @property
    def width(self):
        return self.__width
    '''
        this is a property getter
    '''
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    '''
        this a property setter setting the width
    '''

    @property
    def height(self):
        return self.__height
    '''
        this gets the attribute height
    '''
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

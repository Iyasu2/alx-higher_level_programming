#!/usr/bin/python3
'''
this module contains a class
Rectangle that inherits from
Base
'''
from models.base import Base


class Rectangle(Base):
    '''
    this is the class Rectangle
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        this is the instantiation method
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''
        getter for the width attribute
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        setter for the width attribute
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        '''
        getter for the height attribute
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        setter for the height attribute
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        '''
        getter for the x attribute
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        setter for the x attribute
        '''
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        '''
        getter for the y attribute
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
        setter for the y attribute
        '''
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

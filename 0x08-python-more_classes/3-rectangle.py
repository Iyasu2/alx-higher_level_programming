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
        '''
            this is an init method initializing width
            and height
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''
            this is a property getter
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
            this a property setter setting the width
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''
            this gets the attribute height
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
            this a property setter setting the height
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        '''
        returns the area by using the width and height
        '''
        return self.height * self.width

    def perimeter(self):
        '''
        returns the parameter using the width and height
        '''
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        '''
        returns a string with the shape of the area using #
        '''
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width] * self.height)

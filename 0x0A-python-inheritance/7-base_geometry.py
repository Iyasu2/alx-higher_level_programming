#!/usr/bin/python3
'''
this module contains
a class with two public
instance methods
'''


class BaseGeometry:
    '''
    this class has 2 methods
    '''
    def area(self):
        '''
        this method raises an exception
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        this method validates value checking if it's an integer
        '''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

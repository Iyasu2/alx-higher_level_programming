#!/usr/bin/python3
'''
this module contains the class
Base that manages id attributes
of other classes
'''


class Base:
    '''
    this is the class Base
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        this is the instantiation method with id as argument
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

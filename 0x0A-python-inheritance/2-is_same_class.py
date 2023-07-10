#!/usr/bin/python3

'''
this module contains a function that 
checks whether an object is an instance
of a specified class
'''
def is_same_class(obj, a_class):
    '''
    returns true if obj is exactly an instance of a_class
    returns false otherwise
    '''
    return type(obj) is a_class

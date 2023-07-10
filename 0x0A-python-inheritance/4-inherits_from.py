#!/usr/bin/python3
'''
this module contains a function that checks if an object
is an instance of a subclass inherited from the
class
'''


def inherits_from(obj, a_class):
    '''
    returns true if obj is an instance of a class inheriting a_class
    returns false otherwise
    '''
    if type(obj) is a_class:
        return False
    if isinstance(obj, a_class):
        return True
    return False

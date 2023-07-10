#!/usr/bin/python3
'''
this module contains a function that checks if an object
is an instance of a class or a subclass inherited from the
class
'''


def is_kind_of_class(obj, a_class):
    '''
    returns true if obj is an instance of a_class
    returns false otherwise
    '''
    if isinstance(obj, a_class):
        return True
    return False

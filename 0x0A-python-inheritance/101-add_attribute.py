#!/usr/bin/python3
'''
this function adds attributes
to an object
if possible
'''


def add_attribute(obj, name, value):
    '''
    Add a new attribute to an object if it's possible
    '''
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)

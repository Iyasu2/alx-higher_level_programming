#!/usr/bin/python3
'''
this module contains a function
class_to_json that returns a dictionary
of all the object's attributes
'''


def class_to_json(obj):
    '''
    this function returns a dictionary of
    obj's attributes
    '''
    return obj.__dict__

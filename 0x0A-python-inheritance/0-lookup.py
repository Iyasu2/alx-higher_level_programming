#!/usr/bin/python3

'''
this function returns the list of available
attributes and methods to a given
object
'''


def lookup(obj):
    '''
    this function looks up inside the object 'obj'
    and returns attributes and methods
    '''
    return [attr for attr in dir(obj)]

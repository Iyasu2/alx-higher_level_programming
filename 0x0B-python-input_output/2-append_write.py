#!/usr/bin/python3
'''
this module contains a function
append_write that appends onto a file
and returns the number of characters added
'''


def append_write(filename="", text=""):
    '''
    appends text onto filename
    '''
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)

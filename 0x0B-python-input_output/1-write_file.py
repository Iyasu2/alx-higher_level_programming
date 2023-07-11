#!/usr/bin/python3
'''
this module contains a function
write_file that writes onto a file
and returns the number of characters written
'''


def write_file(filename="", text=""):
    '''
    writes text onto filename
    '''
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)

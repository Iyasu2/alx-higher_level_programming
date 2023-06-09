#!/usr/bin/python3
'''
this module contains a function
read_file that reads a file
and prints it out
'''


def read_file(filename=""):
    '''
    reads filename and prints it out
    '''
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")

#!/usr/bin/python3
'''
this module contains a function that
appends some text after
each line containing a specific string
'''


def append_after(filename="", search_string="", new_string=""):
    '''
    this is function add new_string to filename after search_string
    '''
    with open(filename, mode='r+', encoding='utf-8') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
        f.truncate()

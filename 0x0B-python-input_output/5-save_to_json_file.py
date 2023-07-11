#!/usr/bin/python3
import json
'''
this module contains
a function that saves an object
onto a file using json
'''

def save_to_json_file(my_obj, filename):
    '''
    this is the function
    '''
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)


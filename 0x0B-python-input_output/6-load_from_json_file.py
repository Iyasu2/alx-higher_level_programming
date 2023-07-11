#!/usr/bin/python3
import json
'''
this module contains
a function that creates an object
from a json file
'''

def load_from_json_file(filename):
    '''
    this is the function
    '''
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)


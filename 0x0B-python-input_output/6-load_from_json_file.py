#!/usr/bin/python3
'''
this module contains
a function that creates an object
from a json file
'''
import json


def load_from_json_file(filename):
    '''
    this is the function
    '''
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)

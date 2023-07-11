#!/usr/bin/python3
import json
'''
this module contains a function
from_json_string that returns an object
from a json representation
'''


def from_json_string(my_str):
    '''
    returns the object version of my_str
    '''
    return json.loads(my_str)

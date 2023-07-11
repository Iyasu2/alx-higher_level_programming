#!/usr/bin/python3
'''
this module contains a function
to_json_string that returns a JSON
representation of an object
'''
import json


def to_json_string(my_obj):
    '''
    returns the JSON representation of my_obj
    '''
    return json.dumps(my_obj)

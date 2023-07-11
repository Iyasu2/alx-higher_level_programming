#!/usr/bin/python3
import json
'''
this module contains a function
to_json_string that returns a JSON
representation of an object
'''


def to_json_string(my_obj):
    '''
    returns the JSON representation of my_obj
    '''
    return json.dumps(my_obj)

#!/usr/bin/python3
'''
this module contains the class
Base that manages id attributes
of other classes
'''
import json


class Base:
    '''
    this is the class Base
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        this is the instantiation method with id as argument
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        changes a dict to a json representation
        '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dicts))

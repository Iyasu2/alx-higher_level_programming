#!/usr/bin/python3
'''
this module contains a class Student
with 3 public instance attributes
and a public instance method
'''


class Student:
    '''
    this is the class Student
    '''
    def __init__(self, first_name, last_name, age):
        '''
        this is the instantiation method
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        this is the public instance method
        that returns the dictionary
        '''
        if attrs is None:
            return self.__dict__
        else:
            return {k: v for k, v in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json):
        '''
        replaces all attributes of the student instance
        '''
        for k, v in json.items():
            setattr(self, k, v)

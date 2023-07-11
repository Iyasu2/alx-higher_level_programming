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

    def to_json(self):
        '''
        this is the public instance method
        that returns the dictionary
        '''
        return self.__dict__

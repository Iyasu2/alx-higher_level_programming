#!/usr/bin/python3
'''
this module contains a class
called MyInt that inherits from
int
'''


class MyInt(int):
    '''
    this is the class MyInt
    '''
    def __eq__(self, other):
        '''
        defines what == does
        '''
        return not super().__eq__(other)

    def __ne__(self, other):
        '''
        defines what != does
        '''
        return not super().__ne__(other)

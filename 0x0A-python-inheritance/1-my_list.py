#!/usr/bin/python3

'''
this module contains a class which inherits
the class list. it also has a method that prints
the sorted version of the list
'''
class MyList(list):
    '''
    this class performs inherits list
    '''
    def print_sorted(self):
        '''
        this method prints the sorted version of the list
        '''
        sorted_list = sorted(self)
        print(sorted_list)

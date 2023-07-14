#!/usr/bion/python3
'''
this module contains a class
square that inherits from the 
class Rectangle
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    this is the class Square
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''
        this is the instantiation method
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''
        this method overrides the str from the parent class
        '''
        return (
            f"[Square] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}"
        )

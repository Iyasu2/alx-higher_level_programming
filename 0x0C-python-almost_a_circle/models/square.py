#!/usr/bin/python3
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

    @property
    def size(self):
        '''
        getter for the size attribute
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''
        setter for the size attribute
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''
        this method updates the square using arguments
        '''
        if args:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''
        this funcion returns dict version of class
        '''
        return {
            "id": self.id,
            "x": self.x,
            "y": self.y,
            "size": self.width,
        }

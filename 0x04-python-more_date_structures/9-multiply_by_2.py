#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new_dictionary = {}
    if a_dictionary is not None:
        for i in list(a_dictionary):
            new_dictionary[i] = a_dictionary[i] * 2
    return new_dictionary

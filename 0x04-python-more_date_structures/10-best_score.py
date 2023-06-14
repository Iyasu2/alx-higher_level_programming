#!/usr/bin/python3


def best_score(a_dictionary):
    best = 0
    if not a_dictionary:
        return None
    for i in list(a_dictionary):
        if a_dictionary[i] > best:
            best = a_dictionary[i]
            key_best = i
    return key_best

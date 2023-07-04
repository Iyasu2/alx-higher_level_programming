#!/usr/bin/python

"""
This is the text_indentation module.
This module takes in 1 argument, text, and
prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of
    these characters: ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_text = text.replace(".", ".\n\n")
    new_text = new_text.replace(":", ":\n\n")
    new_text = new_text.replace("?", "?\n\n")
    print(new_text.strip())

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
    text = text.replace("\n", " ").replace("\r", " ").replace("\\", "")
    for c in ".?:":
        text = text.replace(c, c + "\n\n")

    lines = [line.strip() for line in text.split("\n")]

    for line in lines:
        print(line)

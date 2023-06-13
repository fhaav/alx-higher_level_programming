#!/usr/bin/python3


"""
Module containing the write_file function
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and returns the number of characters
    written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)

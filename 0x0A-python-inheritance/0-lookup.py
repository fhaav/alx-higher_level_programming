#!/usr/bin/python3

"""
Module containing a function called 'lookup'
that returns the attributes of an object.
"""


def lookup(obj):
    """
    Retrieves all the available attributes of the given object.

    Args:
        obj (object): The Python object to retrieve attributes from.

    Returns:
        list: A list of strings representing the attributes of the object.
    """
    return dir(obj)

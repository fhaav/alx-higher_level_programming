#!/usr/bin/python3

"""
Module containing the is_same_class function.
"""


def is_same_class(obj, a_class):
    """
    Checks if the object belongs to the same class as the specified class.
    Returns True if the object is of the same class, False otherwise.
    """
    return type(obj) is a_class

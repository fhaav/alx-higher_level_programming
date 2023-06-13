#!/usr/bin/python3

"""
Module containing the inherits_from function
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited
    (directly or indirectly) from a_class, otherwise False
    """

    for cls in type(obj).__mro__:
        if cls is not a_class and issubclass(cls, a_class):
            return True

    return False

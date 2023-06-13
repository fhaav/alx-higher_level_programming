#!/usr/bin/python3

"""
Module containing add_attribute function
"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj (object): The object to add the attribute to.
        attribute (str): The name of the attribute.
        value (any): The value of the attribute.
    """

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    obj.__setattr__(attribute, value)

#!/usr/bin/python3

"""
Module containing the class_to_json function
"""


def class_to_json(obj):
    """
    Converts an object to a dictionary with a simple
    data structure for JSON serialization.

    Args:
        obj: An instance of a class with serializable attributes.
    """

    return obj.__dict__

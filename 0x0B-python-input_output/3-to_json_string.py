#!/usr/bin/python3

"""
Module containing to_json_string function.
"""


import json


def to_json_string(my_obj):
    """
    Convert an object to a JSON string.

    Args:
        my_obj (object): Object to be serialized.

    Returns:
        str: JSON representation of the object.
    """

    json_str = json.dumps(my_obj)
    return json_str

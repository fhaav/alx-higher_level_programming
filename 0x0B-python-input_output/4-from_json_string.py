#!/usr/bin/python3

"""
Module containing the from_json_string function.
"""


import json


def from_json_string(my_str):
    """
    Convert a JSON string to a Python object.

    Args:
        my_str (str): JSON string to be converted.
    """

    python_obj = json.loads(my_str)
    return python_obj

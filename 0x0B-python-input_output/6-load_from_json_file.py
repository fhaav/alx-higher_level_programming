#!/usr/bin/python3

"""
Module containing the load_from_json_file function.
"""


import json


def load_from_json_file(filename):
    """
    Load json from file and convert to python object

    Args:
        filename (str): Name of the JSON file to load the object from.
    """

    with open(filename, 'r') as file:
        return json.load(file)

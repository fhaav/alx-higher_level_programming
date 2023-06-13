#!/usr/bin/python3


"""
Module containing the save_to_json_file function
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Convert a json string to a python object

    Args:
        my_obj (object): Object to be saved.
        filename (str): Name of the file to save the object to.
    """

    with open(filename, 'w') as file:
        json.dump(my_obj, file)

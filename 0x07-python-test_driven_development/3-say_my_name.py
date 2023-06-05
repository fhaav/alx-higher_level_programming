#!/usr/bin/python3

"""
Module defining a name printing function that prints a string
containing first and last name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the first and last name.

    Args:
        first_name (str): The first name.
        last_name (str): The last name. Defaults to "".

    Raises:
        TypeError: If first_name or last_name is not a string.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

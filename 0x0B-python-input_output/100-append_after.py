#!/usr/bin/python3

"""
Module containing the append_after function
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Appends new_string to a file named filename after the line
    containing search_string.

    Args:
        filename (str): Name of the file.
        search_string (str): The string to search for.
        new_string (str): The string to append after the line.
    """
    lines = []
    with open(filename, "r") as file:
        lines = file.readlines()

        with open(filename, "w") as file:
            for line in lines:
                file.write(line)
                if search_string in line:
                    file.write(new_string)

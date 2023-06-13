#!/usr/bin/python3


"""
Module containing read_file function.
"""


def read_file(filename=""):
    """
    Reads the content of a text file and prints it to stdout

    Args:
        filename (str): The name of the text file to read (default: "")
    """

    with open(filename, encoding="utf-8") as file:
        content = file.read()
        print(content, end="")

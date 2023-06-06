#!/usr/bin/python3

"""
Defines the text_indentation function that indents a string based
on certain characters.
"""


def text_indentation(text):
    """
    Prints the given text with two new lines after each
    occurrence of '.', '?', and ':'

    Args:
        text (str): The text to be indented.

    Raises:
        TypeError: If the input text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    ind_text = ""
    for c in text:
        ind_text += c
        if c in ".?:":
            ind_text = ind_text.strip()
            print(ind_text, end="\n\n")
            ind_text = ""

    if ind_text:
        print(ind_text.strip(), end="")

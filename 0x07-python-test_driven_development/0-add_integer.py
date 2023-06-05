#!/usr/bin/python3

"""Module defining a function for integer addition"""


def add_integer(a, b=98):
    """
    Adds 2 integers.

    Args:
    a (int): The first integer.
    b (int):The second integer. Defaults to 98.

    Raises:
    TypeError: If a or b is not an integer or float.

    Returns:
    It returns an integer: the addition of a and b.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

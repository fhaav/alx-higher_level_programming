#!/usr/bin/python3

"""
Contains the MyInt class
"""


class MyInt(int):
    """
    A class that inherits from int and inverts == and != operators
    """

    def __eq__(self, other):
        """Override the == operator."""
        if isinstance(other, MyInt):
            return super().__ne__(other)
        return False

    def __ne__(self, other):
        """Override the != operator."""
        if isinstance(other, MyInt):
            return super().__eq__(other)

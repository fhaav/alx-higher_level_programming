#!/usr/bin/python3

"""
Contains the MyList class that inherits from list
"""


class MyList(list):
    """
    Represents a custom list that inherits from list
    """

    def print_sorted(self):
        """
        Prints the list in sorted order (ascending sort)
        """
        print(sorted(self))

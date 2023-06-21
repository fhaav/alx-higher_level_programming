#!/usr/bin/python3

"""
Contains the Base class.
"""


class Base:
    """ Base class for managing ID attribute """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance with an ID.

        Args:
            id (int): ID for the instance. Defaults to None.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

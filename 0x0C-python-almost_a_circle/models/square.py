#!/usr/bin/python3

""" Contains the square class module """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ A square class that inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance

        Args:
            id (int): Assignable integer to self.id
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the Square instance
        in the format [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """ Getter method for size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter method for size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Attributes update of an instance in a certain order """

        if args:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Display the dictionary representation of the Square.
        """
        dictionary = {
                'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y
        }
        return dictionary

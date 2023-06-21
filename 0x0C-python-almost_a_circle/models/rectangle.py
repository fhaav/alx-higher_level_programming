#!/usr/bin/python3


""" Contains a class Rectangle """


from models.base import Base


class Rectangle(Base):
    """ A Rectangle class that inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance

        Args:
            id (int): Assignable integer to self.id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter for the width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for the width attribute """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """ Getter for the height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for the height attribute """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """ Getter for the x attribute """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for the x attribute """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """ Getter for the y attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for the y attribute """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
        Calculates the area of the rectangle

        Returns:
            int: area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """
        Prints the rectangle with # symbol base on the width and height
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Displays the string representation of the Rectangle instance
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

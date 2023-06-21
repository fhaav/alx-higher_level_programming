#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Test cases for the Rectangle class """

    def test_default_id(self):
        """ Test creation of a rectangle with default ID """
        r = Rectangle(10, 2)
        self.assertEqual(r.id, 2)

    def test_custom_id(self):
        """ Test creation of a rectangle with custom ID """
        r = Rectangle(10, 2, id=5)
        self.assertEqual(r.id, 5)

    def test_attributes_accessors(self):
        """ Test the attributes accessors of the rectangle """
        r = Rectangle(10, 2, 3, 4, 6)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_attribute_mutators(self):
        """ Test the attribute mutators of the rectangle """
        r = Rectangle(10, 2)
        r.width = 5
        r.height = 3
        r.x = 1
        r.y = 2
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)


if __name__ == '__main__':
    unittest.main()

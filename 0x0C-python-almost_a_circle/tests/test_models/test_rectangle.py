#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle
from models.base import Base


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

        with self.assertRaises(TypeError):
            r.width = "invalid"
        with self.assertRaises(TypeError):
            r.height = "invalid"
        with self.assertRaises(TypeError):
            r.x = "invalid"
        with self.assertRaises(TypeError):
            r.y = "invalid"
        with self.assertRaises(ValueError):
            r.width = 0
        with self.assertRaises(ValueError):
            r.height = -5
        with self.assertRaises(ValueError):
            r.x = -2
        with self.assertRaises(ValueError):
            r.y = -3

    def area_test(self):
        """Test the area method"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def display_test(self):
        """ Test the display method """
        r1 = Rectangle(6, 9, 4, 4)
        expected_output = "\n\n ##\n ##\n ##\n"
        with patch("sys.stdout", new=StringIO()) as output:
            r1.display()
            self.assertEqual(output.getvalue(), expected_output)

        r2 = Rectangle(5, 4, 1, 0)
        expected_output = " ###\n ###\n"
        with patch("sys.stdout", new=StringIO()) as output:
            r2.display()
            self.assertEqual(output.getvalue(), expected_output)

    def stdout_capture(self, method):
        """
        Captures the standard output of a method

        Returns:
            str: The captured stdout
        """
        import io
        from contextlib import redirect_stdout

        f = io.StringIO()
        with redirect_stdout(f):
            method()
        return f.getvalue()

    def representation_of_str_test(self):
        """
        Representation of the test string of the Rectangle instance
        """
        r1 = Rectangle(6, 9, 2, 1, 18)
        self.assertEqual(str(r1), "[Rectangle] (18) 2/1 - 6/9")

        r2 = Rectangle(7, 7, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 7/7")

    def update_test(self):
        """
        Rectangle class update method Test
        """
        r = Rectangle(20, 20, 20, 20)
        r.update(77)
        r.update(77, 2)
        r.update(77, 2, 3)
        r.update(77, 2, 3, 4)
        r.update(77, 2, 3, 4, 5)

        self.assertEqual(str(r), "[Rectangle] (1) 20/20 - 20/20")
        self.assertEqual(str(r), "[Rectangle] (77) 20/20 - 20/20")
        self.assertEqual(str(r), "[Rectangle] (77) 20/20 - 2/20")
        self.assertEqual(str(r), "[Rectangle] (77) 20/20 - 2/3")
        self.assertEqual(str(r), "[Rectangle] (77) 4/20 - 2/3")
        self.assertEqual(str(r), "[Rectangle] (77) 4/5 - 2/3")

    def update_args_test(self):
        r = Rectangle(7, 7)
        r.update(20, 2, 6, 8, 9)
        self.assertEqual(r.id, 20)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 8)
        self.assertEqual(r.y, 9)

    def update_kwargs_test(self):
        r = Rectangle(7, 7)
        r.update(id=20, width=2, height=6, x=8, y=9)
        self.assertEqual(r.id, 20)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 8)
        self.assertEqual(r.y, 9)


if __name__ == '__main__':
    unittest.main()

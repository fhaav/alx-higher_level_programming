#!/usr/bin/python3

"""
Module defining a function "matrix_divided" that divides the elements of
a matrix by a specified number.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix

    Args:
        matrix ([[]]): A list of lists containing integers or floats.
        div (int or float): The number to divide the elements of the matrix by.

    Returns:
        [[]]: A new matrix with elements divided by the divisor.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to zero (0).
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    element_len = 0
    if len(matrix) and isinstance(matrix[0], list):
        element_len = len(matrix[0])

    new_matrix = []
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")

        if element_len != len(row):
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    return new_matrix

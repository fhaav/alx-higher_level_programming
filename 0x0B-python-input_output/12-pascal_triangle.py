#!/usr/bin/python3

"""
Module containing the pascal_triangle function
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle of n rows.

    Args:
        n (int): Number of rows in the triangle.

    Returns:
        list: List of lists representing Pascal's triangle.
    """

    pascal_rows = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                prev_row = pascal_rows[i - 1]
                left_value = prev_row[j - 1]
                right_value = prev_row[j]
                value = left_value + right_value
                row.append(value)
        pascal_rows.append(row)

    return pascal_rows

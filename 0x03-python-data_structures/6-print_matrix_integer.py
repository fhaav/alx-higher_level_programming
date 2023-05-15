#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    matrix_len = len(matrix)
    if matrix_len == 0 or (matrix_len == 1 and len(matrix[0]) == 0):
        print()

    if isinstance(matrix, list):
        for row in matrix:
            if isinstance(row, list):
                for i, num in enumerate(row):
                    if i + 1 == len(row):
                        print("{:d}".format(num))
                    else:
                        print("{:d} ".format(num), end="")

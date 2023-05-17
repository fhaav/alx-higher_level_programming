#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if isinstance(matrix, list) and len(matrix):
        return [[x**2 for x in row] for row in matrix]
    else:
        new_matrix = matrix.copy()
        for i in range(len(matrix)):
            new_matrix[i] = list(map(lambda x: x**2, matrix[i]))
        return new_matrix

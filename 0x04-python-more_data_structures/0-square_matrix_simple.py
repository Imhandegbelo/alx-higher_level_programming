#!/usr/bin/python3
'''
returns the square of all elements in a matrix
'''


def square_matrix_simple(matrix=[]):
    return ([list(map(lambda x: x ** 2, row)) for row in matrix])

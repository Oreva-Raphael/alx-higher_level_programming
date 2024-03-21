#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    row_num = len(matrix)
    col_num = len(matrix[0])
    newelement = []
    new_matrix = []
    for a in range(row_num):
        for b in range(col_num):
            newelement.append(matrix[a][b]**2)
        new_matrix.append(newelement)
        newelement = []
    return new_matrix

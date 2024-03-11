#!/usr/bin/python3
def print_matrix_integer(my_matrix=[[]]):
    num_rows = len(my_matrix)
    num_cols = len(my_matrix[0])

    for row_idx in range(num_rows):
        for col_idx in range(num_cols):
            print("{:d}".format(my_matrix[row_idx][col_idx]), end="")
            if col_idx == num_cols - 1:
                break
            else:
                print(" ", end='')
        print()

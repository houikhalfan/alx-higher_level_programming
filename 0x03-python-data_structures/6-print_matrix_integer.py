#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for i, element in enumerate(row):
                if row:
                    print("{:d}".format(element), end='')
                    if i < len(row) - 1:
                        print(' ', end='')
            print()

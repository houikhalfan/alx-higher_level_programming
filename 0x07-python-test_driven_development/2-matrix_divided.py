#!/usr/bin/python3
"""def mhandlii fiha machakil d error w kan7awal n9assam matrix 3la div"""


def matrix_divided(matrix, div):
    """div matrix with a value"""
    mtx = []
    if isinstance(matrix, list) and all(isinstance(x, list)
                                        and all(isinstance(e, (int, float))
                                                for e in x) for x in matrix):
        row_len = len(matrix[0])
        if all(len(row) == row_len for row in matrix):
            if isinstance(div, (int, float)):
                if div != 0:
                    for i in matrix:
                        new_row = []
                        for j in i:
                            new_e = round(j / div, 2)
                            new_row.append(new_e)
                        mtx.append(new_row)
                else:
                    raise ZeroDivisionError("division by zero")
            else:
                raise TypeError("div must be a number")
        else:
            raise TypeError("Each row of the matrix must have the same size")
    else:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    return mtx

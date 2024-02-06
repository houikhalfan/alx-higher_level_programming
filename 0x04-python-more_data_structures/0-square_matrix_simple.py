#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    s_i = []
    if not matrix:
        return matrix
    for i in matrix:
        if not i:
            return matrix
        s_j = []
        for j in i:
            s_j.append(j ** 2)
        s_i.append(s_j)
    return s_i

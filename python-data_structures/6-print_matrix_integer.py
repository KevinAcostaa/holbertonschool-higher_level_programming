#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            end = ' '
            if j is i[-1]:
                end = ''
            print("{:d}".format(j), end=end)
        print()

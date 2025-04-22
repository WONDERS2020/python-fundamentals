#/usr/bin/python3
""" A function that can print a matrix of integers"""
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            print(col, end='')
        print('')

    print_matrix_integer(matrix)
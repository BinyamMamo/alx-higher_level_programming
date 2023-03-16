#!/usr/bin/python3

# def square_matrix_simple(matrix=[]):
#     copy_matrix = matrix.copy()
#     for x in copy_matrix:
#         i = 0
#         while i < len(x):
#             x[i] = x[i] * x[i]
#             i += 1
#     return copy_matrix

def square_matrix_simple(matrix=[]):
    copy = matrix.copy()
    for i in range(len(copy)):
        copy[i] = list(map(lambda a: a * a, copy[i]))
    return copy


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# new_matrix = square_matrix_simple(matrix)
# print(new_matrix)
# print(matrix)

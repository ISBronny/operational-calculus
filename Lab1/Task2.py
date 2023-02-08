from typing import List

import numpy as np


def find_rows(matrix: np.ndarray):
    for j1 in range(0, matrix.shape[0]):
        for j2 in range(0, matrix.shape[0]):
            if j1 == j2:
                continue
            trig = True
            for i in range(0, matrix.shape[1]):
                if matrix[j1][i] > matrix[j2][i]:
                    trig = False
            if trig:
                yield j1


def find_columns(matrix: np.ndarray):
    for i1 in range(0, matrix.shape[1]):
        for i2 in range(0, matrix.shape[1]):
            if i1 == i2:
                continue
            trig = True
            for j in range(0, matrix.shape[0]):
                if matrix[j][i1] < matrix[j][i2]:
                    trig = False
            if trig:
                yield i1


def simplify(matrix: List[list]):
    matrix = np.array(matrix)

    while True:
        columns = list(find_columns(matrix))
        matrix = np.delete(arr=matrix, obj=columns, axis=1)

        rows = list(find_rows(matrix))
        matrix = np.delete(arr=matrix, obj=rows, axis=0)

        if len(columns) == 0 and len(rows) == 0:
            break

    return matrix


if __name__ == '__main__':
    A = [
        [7, 2, 5, 3, 7],
        [6, 9, 1, 4, 2],
        [2, 4, 0, 1, 9],
        [4, 6, 0, 3, 1]
    ]

    new_A = simplify(A)
    print(new_A)

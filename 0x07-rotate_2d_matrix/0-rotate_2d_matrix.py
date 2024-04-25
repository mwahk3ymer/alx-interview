#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """
    Rotate an n x n 2D matrix 90 degrees clockwise.

    Args:
        matrix (list): A 2D matrix to be rotated in-place.

    Returns:
        None. The matrix is edited in-place.

    """
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

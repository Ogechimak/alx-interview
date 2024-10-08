#!/usr/bin/python3
"""
This function is to generate Pascal's triangle.
"""


def pascal_triangle(n):

    """
    Generate Pascal's triangle of n rows.

    """
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        row.append(1)
        triangle.append(row)

    return triangle

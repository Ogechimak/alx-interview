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

    for _ in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # Each row starts with 1

        # Calculate the middle elements of the new row
        for i in range(1, len(prev_row)):
            new_row.append(prev_row[i-1] + prev_row[i])

        new_row.append(1)  # Each row ends with 1
        triangle.append(new_row)

    return triangle

#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""

def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        row = triangle[-1]
        new_row = [1]
        for i in range(len(row) - 1):
            new_row.append(row[i] + row[i + 1])
        new_row.append(1)
        triangle.append(new_row)
    return triangle

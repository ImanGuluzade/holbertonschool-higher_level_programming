#!/usr/bin/python3
"""
12-pascal_triangle
Module that generates Pascal's triangle.
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle of n.
    
    Args:
        n (int): The number of rows of the Pascal's triangle.

    Returns:
        list: List of lists of integers representing Pascal's triangle.
              Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    # Generate each row based on the previous row
    for i in range(1, n):
        row = [1]  # First element of each row is always 1
        prev_row = triangle[i - 1]
        # Each middle element is sum of two elements above it
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle

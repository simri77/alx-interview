#!/usr/bin/python3
"""Pascal's Triangle """


def pascal_triangle(n):
    """
    Returns an empty list if n <= 0
    returns a list of lists of integers
    representing the Pascal triangle of n
    """
    if n <= 0:
        return []

    triangle = []
    row = []
    p_row = []
    for i in range(0, n+1):
        row = [j > 0 and j < i - 1 and i > 2 and p_row[j - 1] +
               p_row[j] or 1 for j in range(0, 1)]
        p_row = row
        triangle += [row]
    return triangle[1:]

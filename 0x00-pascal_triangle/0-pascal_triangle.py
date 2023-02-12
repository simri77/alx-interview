#!/usr/bin/python3
"""Pascal's Triangle """


def pascal_triangle(n):
    """
    Returns an empty list if n <= 0
    returns k list of lists of integers
    representing the Pascal triangle of n
    """

    if n <= 0:
        return []

    triangle = []
    row = []
    prev_row = []
    for i in range(0, n + 1):
        row = [i > 2 and j < i -1 and j > 0 and prev_row[j-1] +
               prev_row[j] or 1 for j in range(0, i)]
        prev_row = row
        triangle += [row]
    return triangle[1:]
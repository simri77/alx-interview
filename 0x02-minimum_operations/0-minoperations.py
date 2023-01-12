#!/usr/bin/python3
""" Minimum Operations"""
def minOperations(n):
    """
    fewest number of operations needed to result in exactly n H characters in the file.
    """
    if n <= 1:
        return 0
    for i in range(2, n + 1):
        if n % i == 0:
            return minOperations(int(n / i)) + 1
#!/usr/bin/python3
"""
Function that calculates the min operations to copy and paste letters
"""


def minOperations(n: int) -> int:
"""calculates the fewest number of operations
    needed to result in exactly n H characters
    in the file"""

    nOp = 0
    minOp = 2
    while n > 1:
        while n % minOp == 0:
            nOp += minOp
            n /= minOp
        minOp += 1
    return nOp

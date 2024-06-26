#!/usr/bin/python3
"""Pascal's Triangle"""

def pascal_triangle(n):
    """Create a function  that returns a list of lists
    of integers representing the Pascals triangle
    """
    trl = []

    if n > 0:

        for i in range(n):
            # Initialize the row with all 1s
            row = [1] * (i + 1)
        
            # Fill in the elements in between the first and last 1
            for j in range(1, i):
                row[j] = trl[i - 1][j - 1] + trl[i - 1][j]
        
            # Append the row to the triangle
            trl.append(row)

        return trl

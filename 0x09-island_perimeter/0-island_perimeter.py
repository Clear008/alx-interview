#!/usr/bin/python3
"""the perimeter of the island"""


def island_perimeter(grid):
    """function that returns the perimeter of the island """
    perimeter = 0

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:

                perimeter += 4

                if c < cols - 1 and grid[r][c + 1] == 1:
                    perimeter -= 2

                if r < rows - 1 and grid[r + 1][c] == 1:
                    perimeter -= 2

    return perimeter

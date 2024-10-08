#!/usr/bin/python3
""" This module implements a function to calculate and island's perimeter """


def island_perimeter(grid):
    """ Calculates perimeter of island found in grid """
    if not isinstance(grid, list):
        return -1
    i_max = len(grid)
    j_max = len(grid[0])

    per = 0
    for i in range(i_max):
        for j in range(j_max):
            if grid[i][j] == 1:
                if (i == 0) or (grid[i - 1][j] == 0):
                    per += 1
                if (i == i_max - 1) or (grid[i + 1][j] == 0):
                    per += 1
                if (j == 0) or (grid[i][j - 1] == 0):
                    per += 1
                if (j == j_max - 1) or (grid[i][j + 1] == 0):
                    per += 1
    return per

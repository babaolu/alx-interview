#!/usr/bin/python3
""" This module implements a function that creates a Pascal's Triangle """

def pascal_triangle(n):
    """ Creates a Pascal's triangle of size n """
    pascalArray = []
    if n <= 0:
        return pascalArray
    pascalArray.append([1])
    for row in range(n - 1):
        pascalArray.append([0 for x in range(row + 2)])
        for index in range(row + 1):
            pascalArray[row + 1][index] += pascalArray[row][index]
            pascalArray[row + 1][index + 1] += pascalArray[row][index]
    return pascalArray

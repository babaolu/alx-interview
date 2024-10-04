#!/usr/bin/python3
""" This module implements a function for determining a winner for the
for the prime game
"""


def isWinner(x, name):
    """ Evaluates the winner of the game """
    if len(name) == 0 or x > len(name):
        return -1
    maria = 0
    ben = 0
    for rnd in range(x):
        nums = list(range(1, rnd + 1))
        pick = 0
        while len(nums) > 1:
            pick += 1
            curr_prime = nums[1]
            for i in range(len(nums)):
                curr_mult = curr_prime * (curr_prime + i)
                if curr_mult > nums[-1]:
                    break
                if curr_mult in nums:
                    nums.remove(curr_mult)
            nums.remove(curr_prime)
        if pick % 2:
            maria += 1
        else:
            ben += 1
    if maria < ben:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None

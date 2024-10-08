#!/usr/bin/python3
""" Implements function to add least number of coins """
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """ Adds least number of coins """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    if (not coins) or total < coins[-1]:
        return -1
    num_coin = 0
    for coin in coins:
        quotient = total // coin
        if quotient > 0:
            num_coin += quotient
            total %= coin
            if total == 0:
                return num_coin
    return -1

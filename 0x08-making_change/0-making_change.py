#!/usr/bin/python3
"""Determine the fewest number of coins"""


def makeChange(coins, total):
    """Given a pile of coins of different values"""
    t = 0
    coins.sort(reverse=True)

    if total < 0:
        return 0
    for coin in coins:
        if total % coin <= total:
            t += total // coin
            total = total % coin

    return t if total == 0 else -1

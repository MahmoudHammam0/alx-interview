#!/usr/bin/python3
""" Change comes from within module """


def makeChange(coins, total):
    """ fewest number of coins needed to meet a given amount """
    if not coins:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if total == 0:
            return change
    return -1

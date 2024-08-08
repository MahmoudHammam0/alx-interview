#!/usr/bin/python3
""" Prime game module """


def prime_counter(num):
    """ check if is it prime """
    prime_nums = []
    sieve = [True] * (num + 1)
    for n in range(2, num + 1):
        if sieve[n]:
            prime_nums.append(n)
            for multiple in range(n, num + 1, n):
                sieve[multiple] = False
    return prime_nums


def isWinner(x, nums):
    """ returns the winner """
    if x is None or nums is None or x == 0 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    for limit in range(x):
        prime_numbers = prime_counter(nums[limit])
        if len(prime_numbers) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None

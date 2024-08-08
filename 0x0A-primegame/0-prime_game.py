#!/usr/bin/python3
""" Prime game module """

def prime_counter(n):
    """Count the number of prime numbers up to n using the Sieve of Eratosthenes."""
    if n < 2:
        return 0
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return sum(is_prime)

def is_winner(x, nums):
    """Determine the winner of the prime game."""
    if x <= 0 or nums is None or x != len(nums):
        return None

    maria_wins = sum(prime_counter(n) % 2 for n in nums)
    ben_wins = x - maria_wins

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    return None


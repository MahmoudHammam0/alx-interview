#!/usr/bin/python3
""" Prime Game module """


def isWinner(x, nums):
    def sieve(n):
        """ Return a list of primes up to n using the Sieve of Eratosthenes"""
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for start in range(2, int(n**0.5) + 1):
            if is_prime[start]:
                for multiple in range(start * start, n + 1, start):
                    is_prime[multiple] = False
        return [num for num, prime in enumerate(is_prime) if prime]

    def winner(n):
        """ Determine the winner for a given n. """
        if n < 2:
            return "Ben"

        primes = sieve(n)
        primes_set = set(primes)
        available = set(range(1, n + 1))

        turn = 0
        while primes_set:
            current_prime = next((p for p in primes if p in available), None)
            if current_prime is None:
                return "Ben" if turn == 0 else "Maria"
            to_remove = set(range(current_prime, n + 1, current_prime))
            available.difference_update(to_remove)
            primes_set.difference_update(to_remove)
            turn = 1 - turn

        return "Ben" if turn == 0 else "Maria"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if winner(n) == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None

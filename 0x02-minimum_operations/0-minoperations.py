#!/usr/bin/python3
""" Minimum Operations module """


def minOperations(n):
    """ Minimum Operations function """
    if n <= 1:
        return 0
    else:
        i = 2
        op = 0
        while i <= n:
            if n % i == 0:
                op += i
                n = n / i
            else:
                i += 1
        return op

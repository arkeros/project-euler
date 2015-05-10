from math import log
from utils import iter_primes

__author__ = 'rafa'


def algorithm(limit):
    n = 1
    for p in iter_primes():
        if p > limit:
            return n
        exponent = int(log(limit, p))
        n *= p**exponent


def solver():
    """
    2520 is the smallest number that can be divided by each of the numbers from
    1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the
    numbers from 1 to 20?
    """
    assert algorithm(10) == 2520
    return algorithm(20)
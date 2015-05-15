from itertools import takewhile
from utils import list_primes

__author__ = 'rafa'


def algorithm(n):
    primes = takewhile(lambda x: x < n, list_primes(n))
    return sum(primes)


def solver():
    """
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
    """
    assert algorithm(10) == 17
    return algorithm(2000000)
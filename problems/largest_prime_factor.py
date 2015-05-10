from utils import iter_primes, iter_factors

__author__ = 'rafa'


def algorithm(n):
    return max(iter_factors(n))


def solver():
    """
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
    """
    assert algorithm(13195) == 29
    return algorithm(600851475143)
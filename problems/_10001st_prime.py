from utils import nth, iter_primes

__author__ = 'rafa'


def solver():
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
    that the 6th prime is 13.

    What is the 10 001st prime number?
    """
    assert nth(iter_primes(), 6-1) == 13
    return nth(iter_primes(), 10001-1)
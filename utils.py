from itertools import islice, takewhile, count
from math import sqrt

__author__ = 'rafa'

# https://docs.python.org/2/library/itertools.html


def nth(iterable, n, default=None):
    """Returns the nth item or a default value"""
    return next(islice(iterable, n, None), default)


def iter_primes():
    """yields prime numbers"""
    primes = [2]
    yield 2
    n = 3
    while True:
        test_primes = takewhile(lambda x: x <= sqrt(n), primes)
        if all(n % p != 0 for p in test_primes):
            yield n
            primes.append(n)
        n += 2


def list_primes(limit):
    """
    eratostenes sieve

    More efficient than iter_primes when whe know the limit.
    """
    sieve = [False]*2 + [True] * (limit-2)
    n = 2
    while n <= sqrt(limit):
        if sieve[n]:
            yield n
        for m in xrange(n**2, limit, n):  # multiples
            sieve[m] = False  # mark multiples as non prime
        n += 1
    while n < limit:
        if sieve[n]:
            yield n
        n += 1


def iter_factors(n):
    x = n
    primes = iter_primes()
    p = next(primes)
    while x != 1:
        while x % p == 0:  # p divides x
            yield p
            x /= p
        p = next(primes)


def iter_fibonacci():
    a, b = 1, 2
    yield a
    yield b
    while True:
        a, b = b, a+b
        yield b


def iter_triangular_numbers():
    n = 0
    for i in count(1):
        n += i
        yield n


def iter_digits(n, base=10):
    q = n
    while q != 0:
        q, r = divmod(q, base)
        yield r
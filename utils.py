__author__ = 'rafa'


def iter_primes():
    """eratostenes cribe"""
    primes = [2]
    yield 2
    n = 3
    while True:
        if all(n % p for p in primes):
            yield n
            primes.append(n)
        n += 2


def iter_factors(n):
    x = n
    primes = iter_primes()
    p = next(primes)
    while x != 1:
        while x % p == 0:  # p divides x
            yield p
            x /= p
        p = next(primes)


def fibonacci():
    a, b = 1, 2
    yield a
    yield b
    while True:
        a, b = b, a+b
        yield b
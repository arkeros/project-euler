from math import factorial

__author__ = 'rafa'


def nth_permutation(iterable, i):
    """Returns the nth permutation in lexicographic order"""
    pool = list(iterable)
    n = len(pool)
    if n == 1:
        return pool[0],
    else:
        partition = factorial(n-1)
        q, r = divmod(i, partition)
        return (pool.pop(q),) + nth_permutation(pool, r)


def solver():
    """
    A permutation is an ordered arrangement of objects. For example, 3124 is
    one possible permutation of the digits 1, 2, 3 and 4. If all of the
    permutations are listed numerically or alphabetically, we call it
    lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4,
     5, 6, 7, 8 and 9?
    """
    permutation = nth_permutation([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10**6 - 1)
    return "".join(str(d) for d in permutation)
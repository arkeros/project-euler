from utils import iter_digits

__author__ = 'rafa'


def solver():
    """
    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2^1000?
    """
    assert sum(iter_digits(2**15)) == 26
    return sum(iter_digits(2**1000))
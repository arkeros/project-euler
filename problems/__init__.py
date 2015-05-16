from problems import multiples_of_3_and_5, even_fibonacci_numbers, \
    largest_prime_factor, smallest_multiple, sum_square_difference, \
    _10001st_prime, summation_of_primes, highly_divisible_triangular_numer, \
    power_digit_sum, lexicographic_permutations

__author__ = 'rafa'

algorithms_map = {
    1: multiples_of_3_and_5,
    2: even_fibonacci_numbers,
    3: largest_prime_factor,
    5: smallest_multiple,
    6: sum_square_difference,
    7: _10001st_prime,
    10: summation_of_primes,
    # 12: highly_divisible_triangular_numer,
    16: power_digit_sum,
    24: lexicographic_permutations
}


class Problem(object):
    def __init__(self, id):
        self.id = id
        self.solver = algorithms_map[id].solver

    def title(self):
        return self.solver.__module__.rsplit('.')[-1].upper()

    def description(self):
        return self.solver.__doc__

    def solution(self):
        # TODO cache
        return self.solver()

problems = {id: Problem(id) for id in algorithms_map.iterkeys()}
print problems
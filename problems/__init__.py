from problems import multiples_of_3_and_5, even_fibonacci_numbers, \
    largest_prime_factor, smallest_multiple

__author__ = 'rafa'

algorithms_map = {
    1: multiples_of_3_and_5,
    2: even_fibonacci_numbers,
    3: largest_prime_factor,
    5: smallest_multiple
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
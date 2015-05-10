from problems import Problem, problems

__author__ = 'rafa'


def main():
    for id, problem in problems.iteritems():
        print problem.title(), problem.description(), \
            "Solution: {}".format(problem.solution())


main()


from problems import Problem, problems

__author__ = 'rafa'


def main():
    for id, problem in problems.iteritems():
        print id, problem.title()
        print problem.description()
        print "\tSolution: {}".format(problem.solution())


main()


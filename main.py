import logic
import util

def main():
    # number of generations
    l = 20

    # population size
    n = 10

    # length per substring
    k = 4

    # assuming deceptive trap
    d = 1

    # assuming non-deceptive trap
    # d = 2.5

    # fitness functions format:
    # util.count_ones
    # logic.deceptive_tight_trap
    # logic.non_deceptive_tight_trap
    # logic.deceptive_loose_trap
    # logic.non_deceptive_loose_trap
    fit_func = logic.deceptive_tight_trap

    # crossover functions format:
    # logic.select_uniform
    # logic.select_two_point
    cross_func = logic.select_uniform

    logic.init(l, n, fit_func, cross_func, k, d)

main()

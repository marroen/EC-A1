import logic
import util

def main():
    # number of generations
    l = 20                                                         #Yoav         #not needed anymore

    # population size
    n = 10

    # length per substring
    k = 4

    # assuming deceptive trap
    d = 1

    # assuming non-deceptive trap
    # d = 2.5

    # succes or not                                                     #yoav
    s = 0
    m = 0
    found = False
    one_mistake = False

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

    while s != 19:
        logic.init(l, n, fit_func, cross_func, k, d)
        if not found:
            if logic.stop_succes:                                         #what if the first of the 20 is false but the rest is true
                n = (n + m)/2
                if n % 10 != 0:
                    n = n*2
                    s += 1
                    found = True
            if logic.stop_failure:
                m = n
                n = n*2
            if n >= 1280:
                break
        else:
            if logic.stop_succes:
                s += 1
            else:
                if one_mistake:
                    found = False
                    s = 0
                    one_mistake = False
                    n = n*2
                    if n >= 1280:
                        break
                else:
                    one_mistake = True

    if s >= 19:
        print(f"succes with population size{n} ")
    else:
        print("failure")

main()

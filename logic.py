from chromosome import Chromosome
from util import count_ones, multi_fit_func

def init(n, fit_func, cross_func, k, d):
    population = create_random_population(n)
    run(population, fit_func, cross_func, k, d)

def run(init_population, fit_func, cross_func, k, d):
    population = init_population
    for i in range(0, 10):
        print("------------")
        print("generation: ", i)
        print("------------")
        uniform_fam = cross_func(population, fit_func)

        # flatten list
        population = [Chromosome(x) for xs in uniform_fam for x in xs]
        print("population:", population)

def create_random_population(n):
    population = []
    i = 0
    while i <= n:
        population.append(Chromosome())
        i += 1
    return population

def select_uniform(population, fit_func):
    selected = []
    for i in range(0, len(population)-1):
        if (i % 2 == 0):
            fam = population[i].uniform(population[i+1].data)
            winners = fam_comp(fam[0], fam[1], fit_func)
            selected.append(winners)
    return selected

def select_two_point(population, fit_func):
    selected = []
    for i in range(0, len(population)-1):
        if (i % 2 == 0):
            fam = population[i].two_point(population[i+1].data)
            final_fam = fam_comp(fam[0], fam[1], fit_func)
            selected.append(final_fam)
    return selected

def fam_comp(parents, children, fit_func):
    p_fits = multi_fit_func(parents, fit_func)
    c_fits = multi_fit_func(children, fit_func)

    # selects parent(s) only if larger than at least one child,
    # and vice versa (but this is unlikely)
    filtered_ps = [p for p in parents if fit_func(p) > min(c_fits)]
    filtered_cs = [c for c in children if fit_func(c) >= min(p_fits)]

    sorted_ps = sorted(filtered_ps, key=fit_func, reverse=True)
    sorted_cs = sorted(filtered_cs, key=fit_func, reverse=True)

    selected = sorted_cs[:2]
    selected += sorted_ps[:2 - len(selected)]

    for i in range(len(selected)):
        if len(sorted_ps) > 0 and (fit_func(sorted_ps[0])) > fit_func(selected[i]):
            selected[i] = sorted_ps.pop(0)

    return selected

def deceptive_tight_trap(bitstring):
    k = 4
    d = 1
    m = int(len(bitstring)/k - 1)

    fitness = 0
    for j in range(0, m+1):
        substring = bitstring[j*k:j*k+k]
        ones = count_ones(substring)
        fitness += sub(ones, k, d)

    return fitness

def non_deceptive_tight_trap(bitstring):
    k = 4
    d = 2.5
    m = int(len(bitstring)/k - 1)

    fitness = 0
    for j in range(0, m+1):
        substring = bitstring[j*k:j*k+k]
        ones = count_ones(substring)
        fitness += sub(ones, k, d)

    return fitness

def deceptive_loose_trap(bitstring):
    k = 4
    d = 1
    m = int(len(bitstring)/k - 1)

    fitness = 0
    for j in range(0, m+1):
        first = bitstring[j]
        second = bitstring[j+10]
        third = bitstring[j+20]
        fourth = bitstring[j+30]
        substring = [first, second, third, fourth]
        ones = count_ones(substring)
        fitness += sub(ones, k, d)
    return fitness

def non_deceptive_loose_trap(bitstring):
    k = 4
    d = 2.5
    m = int(len(bitstring)/k - 1)

    fitness = 0
    for j in range(0, m+1):
        first = bitstring[j]
        second = bitstring[j+10]
        third = bitstring[j+20]
        fourth = bitstring[j+30]
        substring = [first, second, third, fourth]
        ones = count_ones(substring)
        fitness += sub(ones, k, d)
    return fitness

def sub(ones, k, d):
    if ones == k:
        return k
    else:
        return deceive(k, d, ones)

def deceive(k, d, ones):
    return (k-d) - ((k-d) * ones) / (k-1)

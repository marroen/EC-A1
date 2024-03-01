from chromosome import Chromosome
from util import count_ones, multi_count_ones

def init(n, k, d):
    population = create_random_population(n)
    run(population, k, d)

def run(population, k, d):
  
    for i in range(0, 250):
        tight_fitness = tight_trap(population[0], k, d)
        loose_fitness = loose_trap(population[0], k, d)
        print("first chromosome (tight) fitness: ", tight_fitness)
        print("first chromosome (loose) fitness: ", loose_fitness)

        uniform_fam = select_uniform(population)
        two_point_fam = select_two_point(population)
        print(uniform_fam)

def create_random_population(n):
    population = []
    i = 0
    while i <= n:
        population.append(Chromosome())
        i += 1
    return population

def select_uniform(population):
    selected = []
    for i in range(0, len(population)-2):
        if (i % 2 == 0):
            fam = population[i].uniform(population[i+1].data)
            selected.append(fam_comp(fam[0], fam[1]))
    return selected

def select_two_point(population):
    selected = []
    for i in range(0, len(population)-2):
        if (i % 2 == 0):
            fam = population[i].two_point(population[i+1].data)
            final_fam = fam_comp(fam[0], fam[1])
            selected.append(final_fam)
    return selected

def fam_comp(parents, children):
    p_fits = multi_count_ones(parents)
    c_fits = multi_count_ones(children)

    # selects parent(s) only if larger than at least one child,
    # and vice versa (but this is unlikely)
    filtered_ps = [p for p in parents if count_ones(p) > min(c_fits)]
    filtered_cs = [c for c in children if count_ones(c) >= min(p_fits)]

    sorted_ps = sorted(filtered_ps, key=count_ones, reverse=True)
    sorted_cs = sorted(filtered_cs, key=count_ones, reverse=True)

    selected = sorted_cs[:2]
    selected += sorted_ps[:2 - len(selected)]

    for i in range(len(selected)):
        if len(sorted_ps) > 0 and count_ones(sorted_ps[0]) > count_ones(selected[i]):
            selected[i] = sorted_ps.pop(0)

    return selected

def tight_trap(chromosome, k, d):
    bitstring = chromosome.data
    m = int(len(bitstring)/k - 1)

    fitness = 0
    for j in range(0, m+1):
        substring = bitstring[j*k:j*k+k]
        ones = count_ones(substring)
        fitness += sub(ones, k, d)

    return fitness

def loose_trap(chromosome, k, d):
    bitstring = chromosome.data
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

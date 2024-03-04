from chromosome import Chromosome
from util import count_ones, multi_fit_func
import random

def init(l, n, fit_func, cross_func, k, d):
    global ending
    ending = 0
    global stop_failure
    stop_failure = False
    global stop_succes
    stop_succes = False
    init_population = create_random_population(n)
    run(l, init_population, fit_func, cross_func, k, d)

def stop_succes(self):
    return self.stop_succes  # Getter method

def stop_failure(self):
    return self.stop_succes   # Getter method

def run(l, init_population, fit_func, cross_func, k, d):
    population = init_population
    while not stop_succes and not stop_failure:
    #for i in range(0, l):
        # TODO: shuffle population per i
        random.shuffle(population)
        print("------------")
        print("generation: ")                   #i was here
        print("------------")
        selected = cross_func(population, fit_func)

        # flatten list
        population = [Chromosome(x) for xs in selected for x in xs]
        #print("population:", population)
        for chromosome in population:
            print(chromosome.data)
    # TODO: visualize bitstring(s) 

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
            winners = fam_comp(fam[0], fam[1], fit_func, len(population))
            selected.append(winners)
    return selected

def select_two_point(population, fit_func):
    selected = []
    for i in range(0, len(population)-1):
        if (i % 2 == 0):
            fam = population[i].two_point(population[i+1].data)
            final_fam = fam_comp(fam[0], fam[1], fit_func, len(population))
            selected.append(final_fam)
    return selected

# todo def fam_comp(parents, children, fit_func):
def fam_comp(parents, children, fit_func, population_size):
    global ending
    global stop_failure
    global stop_succes
    p1_fit = fit_func(parents[0])
    p2_fit = fit_func(parents[1])
    c1_fit = fit_func(children[0])
    c2_fit = fit_func(children[1])

    selected = [(parents[0], p1_fit, 0), (parents[1], p2_fit, 0), (children[0], c1_fit, 1), (children[1], c2_fit, 1)]
    selected = sorted(selected, key=lambda x: (x[1], x[2]))
    if count_ones(selected[3][0]) == 40:
        stop_succes = True
    else:
        if selected[3][2] == 1:
            if selected[3][1] == (p1_fit or p2_fit):
                ending += 1
            else:
                ending = 0
        elif selected[3][2] == 0:
            ending += 1
        else:
            ending = 0
        if ending == (population_size/2):                                            #it worksssss
            stop_failure = True
            ending = 0

    selected = [selected[2][0], selected[3][0]]
    return selected

"""def fam_comp(parents, children, fit_func):
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

    #if count_ones(selected[0]) == 40 or count_ones(selected[1]) == 40:             Yoav
        #stop_succes = true
    #else:
        #if children >! parents:
            #ending +=1
        #else:
            #ending = 0
        #if ending == 10:
            #stop_failure = true

    return selected
    
"""

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

from chromosome import Chromosome 
#import random

def init():
    population = create_random_population(10)
    print("first chromosome fitness: ", tight_trap(population[0]))

def create_random_population(n):
    population = []
    i = 0
    while i <= n:
        population.append(Chromosome())
        i += 1
    return population

def tight_trap(chromosome):
    k = 4
    # assuming deceptive trap function
    d = 1
    # assuming non-deceptive trap function
    #d = 2.5

    bitstring = chromosome.data
    m = int(len(bitstring)/k - 1)

    fitness = 0
    for j in range(0, m+1):
        substring = bitstring[j*k:j*k+k]
        ones = count_ones(substring)
        fitness += sub(ones, k, d)

    return fitness

# todo def loose_trap(chromosome):

def count_ones(bitstring):
    return bitstring.count(1)

def sub(ones, k, d):
    if ones == k:
        return k
    else:
        return deceive(k, d, ones)

def deceive(k, d, ones):
    return (k-d) - ((k-d) * ones) / (k-1)

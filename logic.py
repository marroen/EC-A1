from chromosome import Chromosome 
#import random

def init(k, d):
    population = create_random_population(10)
   
    tight_fitness = tight_trap(population[0], k, d)
    loose_fitness = loose_trap(population[0], k, d)
    print("first chromosome (tight) fitness: ", tight_fitness)
    print("first chromosome (loose) fitness: ", loose_fitness)


def create_random_population(n):
    population = []
    i = 0
    while i <= n:
        population.append(Chromosome())
        i += 1
    return population

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


def count_ones(bitstring):
    return bitstring.count(1)

def sub(ones, k, d):
    if ones == k:
        return k
    else:
        return deceive(k, d, ones)

def deceive(k, d, ones):
    return (k-d) - ((k-d) * ones) / (k-1)

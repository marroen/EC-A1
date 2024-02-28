from chromosome import Chromosome 
#import random

def init():
    population = createRandomPopulation(10)
    print("first chromosome fitness: ", tightTrap(population[0]))

def createRandomPopulation(n):
    population = []
    i = 0
    while i <= n:
        population.append(Chromosome())
        i += 1
    return population

def tightTrap(chromosome):
    k = 4
    # assuming deceptive trap function
    d = 1
    # assuming non-deceptive trap function
    #d = 2.5

    bitstring = chromosome.data
    ones = countOnes(bitstring)
    m = int(len(bitstring)/k - 1)

    fitness = 0
    for j in range(0, m+1):
        substring = bitstring[j*k:j*k+k]
        fitness += sub(substring, k, d)

    return fitness

# todo def looseTrap(chromosome):

def countOnes(bitstring):
    return bitstring.count(1)

def sub(bitstring, k, d):
    ones = countOnes(bitstring)
    if ones == k:
        return k
    else:
        return deceive(k, d, ones)

def deceive(k, d, ones):
    return (k-d) - ((k-d) * ones) / (k-1)

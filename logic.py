from chromosome import Chromosome 
#import random

def init():
    print("hi")
    return createRandomPopulation(10)

def createRandomPopulation(n):
    population = []
    i = 0
    while i < n:
        population.append(Chromosome())
        i += 1
    return population

def tightTrap(chromosome):
    k = 4
    ones = countOnes(chromosome)
    m = len(chromosome)/k - 1
    for j in range(0, m):
        sub(chromosome.slice(j*k+1, j*k+k))

# todo def looseTrap(chromosome):

def countOnes(bitstring):
    return bitstring.count(1)

def sub(bitstring):
    ones = countOnes(bitstring)
    if len(bitstring) == 4:
        return 4
    else:
        # todo d = 2.5
        return deceive(4, 1, ones)

def deceive(k, d, ones):
    # todo k - d etc
    k_diff = k - d
    return k_diff - (k_diff*ones) / (k-1)

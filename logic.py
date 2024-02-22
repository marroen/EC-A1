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

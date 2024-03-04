import math

from chromosome import Chromosome
from util import count_ones, multi_fit_func
import random

def init(n, fit_func, cross_func, k, d):
    global ending
    global stop_failure
    global stop_succes
    ending = 0
    stop_failure = False
    stop_succes = False

    init_population = create_random_population(n)
    run(init_population, fit_func, cross_func, k, d)

def stop_succes(self):
    return self.stop_succes  # Getter method

def stop_failure(self):
    return self.stop_succes   # Getter method

def run(init_population, fit_func, cross_func, k, d):
    population = init_population
    generation = 0
    '''error_list = []
    correct_list = []
    prop_list = []
    schema0_list = []
    schema1_list = []
    schema0_fit_average = []
    schema1_fit_average = []
    schema0_fit_sd = []
    schema1_fit_sd = []'''
    while not stop_succes and not stop_failure:
        generation += 1
    #for i in range(0, l):
        # TODO: shuffle population per i - done
        random.shuffle(population)
        #print("------------")
        #print(f"population size: {len(population)}")                   #i was here
        #print("------------")
        selected = cross_func(population, fit_func)
                                                                        #counter numvber of generations - reset after new n - average it in main

        # The part in apostrophe's can be used to get the number of selection errors and correct decisions
        # as well as the proportion of bit-1's
        '''ec = error_correct(population, selected)
        error_list.append(ec[0])
        correct_list.append(ec[1])
        prop_list.append(prop(population))
        schema0_list.append(schemata_count(population)[0])
        schema1_list.append(schemata_count(population)[1])
        schema0_fit_average.append(stats(schemata_fit(population, fit_func)[0])[0])
        schema1_fit_average.append(stats(schemata_fit(population, fit_func)[1])[0])
        schema0_fit_sd.append(stats(schemata_fit(population, fit_func)[0])[1])
        schema1_fit_sd.append(stats(schemata_fit(population, fit_func)[1])[1])'''

        # flatten list
        population = [Chromosome(x) for xs in selected for x in xs]
        '''for chromosome in population:
            print(chromosome.data)'''

    print("\n")
    print("number of generations: ", generation)
    '''print("error list: ", error_list)
    print("correct list: ", correct_list)
    print("prop list: ", prop_list)
    print("schema0 list: ", schema0_list)
    print("schema1 list: ", schema1_list)
    print("schema0 fitness average: ", schema0_fit_average)
    print("schema1 fitness average: ", schema1_fit_average)
    print("schema0 fitness standard deviation: ", schema0_fit_sd)
    print("schema1 fitness standard deviation: ", schema1_fit_sd)'''
    # TODO: visualize bitstring(s) 

def create_random_population(n):
    population = []
    i = 0
    while i < n:                                                                    # i removed the =
        population.append(Chromosome())
        i += 1
    return population

def select_uniform(population, fit_func):
    selected = []
    for i in range(0, len(population)):                                             # i removed the -1
        if (i % 2 == 0):
            fam = population[i].uniform(population[i+1].data)
            winners = fam_comp(fam[0], fam[1], fit_func, len(population))
            selected.append(winners)
    return selected

def select_two_point(population, fit_func):
    selected = []
    for i in range(0, len(population)):                                         # i removed the -1
        if (i % 2 == 0):
            fam = population[i].two_point(population[i+1].data)
            final_fam = fam_comp(fam[0], fam[1], fit_func, len(population))
            selected.append(final_fam)
    return selected

# todo def fam_comp(parents, children, fit_func): - done
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
        else:                                                                       # i dont think it ever enters this else
            ending = 0
        if ending == ((population_size/2)*10):                                            #it worksssss
            stop_failure = True
            ending = 0

    selected = [selected[2][0], selected[3][0]]
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

def prop(population):
    ones = 0
    n = len(population)
    for i in range(n):
        ones += count_ones(population[i].data)
    proportion = ones/(n*40)
    return round(proportion, 2)
# In main, for each generation: print 'prop({generation}) = {prop(population)}

def error_correct(population, selected):
    error = 0
    correct = 0
    for i in range(int(len(population) / 2)):
        for j in range(40):
            if population[2 * i].data[j] != population[2 * i + 1].data[j]:
                if selected[i][0][j] == 0 and selected[i][1][j] == 0:
                    error += 1
                if selected[i][0][j] == 1 and selected[i][1][j] == 1:
                    correct += 1
    return round(error, 2), round(correct,2)

def schemata_count(population):
    schema_0 = 0
    schema_1 = 0
    for i in range(len(population)):
        if population[i].data[0] == 0:
            schema_0 += 1
        if population[i].data[0] == 1:
            schema_1 += 1
    return round(schema_0,2), round(schema_1,2)

def schemata_fit(population, fit_func):
    schema_0_fit = []
    schema_1_fit = []
    for i in range(len(population)):
        if population[i].data[0] == 0:
            schema_0_fit.append(fit_func(population[i].data))
        if population[i].data[0] == 1:
            schema_1_fit.append(fit_func(population[i].data))
    return schema_0_fit, schema_1_fit

def stats(list):
    if len(list) != 0:
        average = sum(list) / len(list)
        summ = 0
        for i in range(len(list)):
            summ += (list[i] - average) ** 2
        variance = summ / len(list)
        standard_deviation = math.sqrt(variance)
    else:
        average = 0
        standard_deviation = 0
    return round(average,2), round(standard_deviation, 2)


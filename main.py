import logic
import util
import matplotlib.pyplot as plt


def main():
    # number of generations
    #l = 20                                                         #Yoav         #not needed anymore

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
    l = 0
    found = False
    one_mistake = False
    error = False
    found = False
    found_first = False

    # fitness functions format:                     Uniform     two_point
    # util.count_ones                               30          50
    # logic.deceptive_tight_trap                    1280        160
    # logic.non_deceptive_tight_trap                160         90
    # logic.deceptive_loose_trap                    1280        1280
    # logic.non_deceptive_loose_trap                200         1280
    fit_func = util.count_ones

    # crossover functions format:
    # logic.select_uniform
    # logic.select_two_point
    cross_func = logic.select_uniform

    while not found and not error:
        logic.init(n, fit_func, cross_func, k, d)
        if logic.stop_failure:
            logic.init(n, fit_func, cross_func, k, d)
            if logic.stop_failure and not found_first:
                m = n
                n = n * 2
                if n > 1280:
                    error = True
            elif logic.stop_failure and found_first:
                if 10 == l - n:
                    n = l
                    found = True
                else:
                    m = n
                    n = (l + n) / 2
            else:
                for i in range(0, 18):
                    logic.init(n, fit_func, cross_func, k, d)
                    if logic.stop_failure and not found_first:
                        m = n
                        n = n * 2
                        if n > 1280:
                            error = True
                            break
                        break
                    elif logic.stop_failure:
                        if 10 == l - n and found_first:
                            n = l
                            found = True
                            break
                        else:
                            m = n
                            n = (l + n) / 2
                            break
                    if i == 17:                                 # klopt 17?
                        found_first = True
                        l = n
                        n = (n + m) / 2
                        if n % 10 != 0:
                            n = l
                            found = True
        else:
            t = 0
            for i in range(0, 19):
                logic.init(n, fit_func, cross_func, k, d)
                if t == 1 and logic.stop_failure:
                    if logic.stop_failure and not found_first:
                        m = n
                        n = n * 2
                        if n > 1280:
                            error = True
                            break
                        break
                    elif logic.stop_failure:
                        if 10 == l - n and found_first:
                            n = l
                            found = True
                            break
                        else:
                            m = n
                            n = (l + n) / 2
                            break
                elif logic.stop_failure:
                    t += 1
                if i == 18:
                    found_first = True
                    l = n
                    n = (n + m) / 2
                    if n % 10 != 0:
                        n = l
                        found = True

    if found:
        print(f"succes with population size {n}")
    else:
        print(f"failure with population size 1280")                          #soms population size bigger than 1280

    '''fitness_average = [20.22, 22.0, 22.83, 24.5, 25.69, 26.14, 27.87, 28.94, 30.0, 31.0, 32.25, 32.88, 34.0, 34.94, 35.88, 37.19, 37.88, 38.22]
    plt.plot(range(1, len(fitness_average) + 1), fitness_average, marker='o', linestyle='-')

    # Set the labels for x and y axes
    plt.xlabel('Index')
    plt.ylabel('Fitness Average')

    # Set the title of the plot
    plt.title('Fitness Average')

    # Display the grid
    plt.grid(True)

    # Show the plot
    plt.show()'''
main()
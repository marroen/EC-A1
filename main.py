import logic
import util
import time

def main():
    #number of generations                          #needed for deliverables 1,2 and 3
    #l = 200

    # population size
    n = 10

    # needed variables
    last_incorrect = 0
    last_correct = 0
    min_population_size = 1280

    error = False
    found = False
    found_first = False
    one_of_twenty = False

    # fitness functions format:
    # util.count_ones
    # logic.deceptive_tight_trap
    # logic.non_deceptive_tight_trap
    # logic.deceptive_loose_trap
    # logic.non_deceptive_loose_trap
    fit_func = logic.non_deceptive_loose_trap

    # crossover functions format:
    # logic.select_uniform
    # logic.select_two_point
    cross_func = logic.select_two_point

    for j in range(0, 5):
        while not found and not error:
            begin_CPU_time = time.process_time()
            num_generations = 0
            amount_of_time = 0
            logic.init(n, fit_func, cross_func)
            if logic.stop_failure:
                logic.init(n, fit_func, cross_func)
                if logic.stop_failure and not found_first:
                    last_incorrect = n
                    n = n * 2
                    if n > 1280:
                        error = True
                elif logic.stop_failure and found_first:
                    if 10 == last_correct - n:
                        n = last_correct
                        found = True
                    else:
                        last_incorrect = n
                        n = (last_correct + n) / 2
                else:
                    num_generations += logic.generation
                    amount_of_time += 1
                    for i in range(0, 18):
                        logic.init(n, fit_func, cross_func)
                        num_generations += logic.generation
                        amount_of_time += 1
                        if logic.stop_failure and not found_first:
                            last_incorrect = n
                            n = n * 2
                            if n > 1280:
                                error = True
                                break
                            else:
                                break
                        elif logic.stop_failure:
                            if 10 == last_correct - n and found_first:
                                n = last_correct
                                found = True
                                break
                            else:
                                last_incorrect = n
                                n = (last_correct + n) / 2
                                break
                        if i == 17:
                            found_first = True
                            last_correct = n
                            n = (n + last_incorrect) / 2
                            if n % 10 != 0:
                                n = last_correct
                                found = True
                            last_correct_CPU = time.process_time() - begin_CPU_time
                            last_num_generations = num_generations
                            last_amount_of_time = amount_of_time
            else:
                num_generations += logic.generation
                amount_of_time += 1
                t = 0
                for i in range(0, 19):
                    logic.init(n, fit_func, cross_func)
                    if not logic.stop_failure:
                        num_generations += logic.generation
                        amount_of_time += 1
                    if t == 1 and logic.stop_failure:
                        if logic.stop_failure and not found_first:
                            last_incorrect = n
                            n = n * 2
                            if n > 1280:
                                error = True
                                break
                            else:
                                break
                        elif logic.stop_failure:
                            if 10 == last_correct - n and found_first:
                                n = last_correct
                                found = True
                                break
                            else:
                                last_incorrect = n
                                n = (last_correct + n) / 2
                                break
                    elif logic.stop_failure:
                        t += 1
                    if i == 18:
                        found_first = True
                        last_correct = n
                        n = (n + last_incorrect) / 2
                        if n % 10 != 0:
                            n = last_correct
                            found = True
                        last_correct_CPU = time.process_time() - begin_CPU_time
                        last_num_generations = num_generations
                        last_amount_of_time = amount_of_time

        if n < min_population_size and not error:
            min_population_size = n
            average_num_generations = last_num_generations/last_amount_of_time
            average_CPU_time = last_correct_CPU/last_amount_of_time

        if error and not one_of_twenty:
            one_of_twenty = True
            error = False
            if j == 4:
                found = True

        if error and one_of_twenty:
            break

        if j != 4:
            n = 10
            last_incorrect = 0
            last_correct = 0
            found = False
            found_first = False

        last_num_generations = 0
        last_amount_of_time = 0
        last_correct_CPU = 0

    if found and min_population_size < 1280:
        print("\n")
        print(f"minimal population size: {min_population_size}")
        print(f"average number generations: {round(average_num_generations)}")
        print(f"average number fitness function evaluations: {round(average_num_generations)*2*min_population_size}")
        print(f"average CPU time: {average_CPU_time}")
    else:
        print(f"failure with population size 1280")

    #needed for deliverables 1,2 and 3
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

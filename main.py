import logic
import util

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
    fit_func = logic.non_deceptive_loose_trap

    # crossover functions format:
    # logic.select_uniform
    # logic.select_two_point
    cross_func = logic.select_two_point

    while not found and not error:
        logic.init(n, fit_func, cross_func, k, d)
        if logic.stop_failure:
            logic.init(n, fit_func, cross_func, k, d)
            if logic.stop_failure and not found_first:
                m = n
                n = n * 2
                if n >= 1280:
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
                        if n >= 1280:
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
                        if n >= 1280:
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
        print(f"failure with population size {n}")                          #soms population size bigger than 1280

main()

"""
while s < 20:
    logic.init(n, fit_func, cross_func, k, d)
        if logic.stop_succes:                                               # what if the first of the 20 is false but the rest is true
            t = 0 
            for i in range (0,19)
                logic.init(n, fit_func, cross_func, k, d)
                if t = 1 and logic.stop_failure:
                    m = n
                    n = n * 2
                    if n >= 1280:
                        s = 21
                    break
                elif logic.stop_failure
                    t += 1
                if i == 18:
                    n = (n + m) / 2
                    if n % 10 != 0:
                        n = n * 2
                        s = 20
        else:
            if logic.stop_failure:
                m = n
                n = n * 2
                if n >= 1280:
                    s = 21
    else:
        
                    
                    
            n = (n + m) / 2
            if n % 10 != 0:
                n = n * 2
                s += 1
                found = True
        if logic.stop_failure:
            m = n
            n = n * 2
        if n >= 1280:
            break
    else:
        if logic.stop_succes:
            s += 1
        else:
            if one_mistake:
                found = False
                s = 0
                one_mistake = False
                n = n * 2                                       #fouuuuuuttt
                if n >= 1280:
                    break
            else:
                one_mistake = True
                s += 1
                
                
    while not found and not error:
        logic.init(n, fit_func, cross_func, k, d)
        if logic.stop_failure:
            logic.init(n, fit_func, cross_func, k, d)
            if logic.stop_failure and not found_first:
                m = n
                n = n * 2
                if n >= 1280:
                    error = True
            elif logic.stop_failure and found_first:
                if l != 0:
                    if 10 <= l - n:
                        n = l
                        found = True
                    else:
                        m = n
                        n = (l + n) / 2
            else:
                for i in range(0, 18):
                    logic.init(n, fit_func, cross_func, k, d)
                    if logic.stop_failure:
                        m = n
                        n = (l + n) / 2                     #wat als 10?
                        break
                    if i == 17:                             # klopt 17?
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
                        if n >= 1280:
                            error = True
                            break
                    elif logic.stop_failure and found_first:
                        if l != 0:
                            if 10 <= l - n:
                                n = l
                                found = True
                            else:
                                m = n
                                n = (l + n) / 2
                elif logic.stop_failure:
                    t += 1
                if i == 18:
                    found_first = True
                    l = n
                    n = (n + m) / 2
                    if n % 10 != 0:
                        n = l
                        found = True
         

    


 
"""

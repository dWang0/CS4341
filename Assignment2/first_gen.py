from Population import *
from random import randint


def first_gen(possible_list, num_pop,goal):
    """

    :type possible_list: List of Integers
    """
    response = []
    ## This is done to resolve the scoping probles in Python
    for i in range(0,num_pop):
        response.append(Population([]))
    i = 0
    while i < num_pop:
        a_pop = []

        ## Create a population based off random numbers from the list
        for j in range(len(possible_list)):
            a_pop.append(possible_list[randint(0,len(possible_list)-1)])

        ## If the population is an 'unfit' population, e.g. it's greater than the goal
        ## Discard it and start anew.
        test = Population(a_pop)
        test.evalPop(fge,goal)

        if (test.getRatings() == 0):
            continue
        else:

            response[i].children=a_pop
        i = i+1

    return response

# a = first_gen([1,2,3,4,5],10)
# print a

def fge(list,goal):
    # print(list,sum(list),goal)
    if (sum(list) > goal):
        return 0
    else:
        return 1
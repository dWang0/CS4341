from Population import *
from random import randint
from crossover import split_list


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



def poptwofg(possible_list, num_pop):
    """

    :param possible_list: List of default values for the population
    :param num_pop: number of populations in a generation.
    :return: The first generation
    """
    response = []
    ## This is done to resolve the scoping probles in Python
    for i in range(0,num_pop):
        response.append(Poptwo([]))
    i = 0
    while i < num_pop:
        a_pop = []

        ## Create a population based off random numbers from the list
        for j in range(len(possible_list)):
            a_pop.append(possible_list[randint(0,len(possible_list)-1)])

        ## If the population is an 'unfit' population, e.g. it's greater than the goal
        ## Discard it and start anew.
        b1,b2,b3 = split_list(a_pop,3)
        test = Poptwo(b1,b2,b3)
        test.evalPop(fge2,None)

        if (test.getRatings() == 0):
            continue
        else:
            response[i].setPop(b1,b2,b3)
        i = i+1

    return response

def fge2(b1,b2,b3,goal):
    """
    checks if bin 1 has an even number of negative numbers

    checks if bin1, bin2, or bin3 are all no longer than 10.

    :param b1: bin1 of pop
    :param b2: bin 2 of pop
    :param b3: bin 3 of pop
    :param goal: irrelevant
    :return:
    """
    num_neg = 0;
    for val in b1:
        if val < 0:
            num_neg = num_neg+1
    if(num_neg % 2) == 1:
        return 0
    if (len(b1) > 10) and (len(b2) > 10) and (len(b3) > 10):
        return 0
    else:
        return 1

from Population import *
from random import randint


def first_gen(possible_list, num_pop):
    """

    :type possible_list: List of Integers
    """
    response = []
    ## This is done to resolve the scoping probles in Python
    for i in range(0,num_pop):
        response.append(Population([]))

    for i in range(0,num_pop,1):
        a_pop = []
        for j in range(len(possible_list)):
            a_pop.append(possible_list[randint(0,len(possible_list)-1)])
        response[i].children=a_pop

    return response

# a = first_gen([1,2,3,4,5],10)
# print a

__author__ = 'Ray'

#
def pickPeople(list_of_pop, num_pops):
    """
    Given a list of population, return the list of populations with the highest ratings
    (the most fit populations) repaces the weakest link with the strongest

    :param list_of_pop: Takes in a generation
    :param num_pops: the number of populations in the generation to carry forward

    :return:The selected generation for mating
    """
    sorted_pop = []
    i = 0
    ## Sorts the population by the best pop to worst pop
    for i in range(len(list_of_pop)):
        temp,index = getBestPop(list_of_pop)
        sorted_pop.append(temp)
        list_of_pop.pop(index)
    ## Caps the number of pops to 1:
    ## If you are supposed to pop more people in the list, then only remove one person
    if num_pops >= len(sorted_pop):
        num_pops = len(sorted_pop)

    best_pops = []

    i = 0
    ## Get the first part of the list: length of list_of_pop - num_pops
    for i in range(0,num_pops,1):
        best_pops.append(sorted_pop[i])

    ## Fill the rest of the list.
    if i == len(sorted_pop):
        return best_pops
    else:
        for i in range(num_pops,len(sorted_pop),1):
            best_pops.append(sorted_pop[0])

        return best_pops


def getWorstPop(list_of_pop):
    worst = list_of_pop[0]
    index = 0

    for pop,i in zip(list_of_pop,range(len(list_of_pop))):
        if(pop.getRatings() < worst.getRatings()):
            worst = pop
            index = i

    return worst,index

def getBestPop(list_of_pop):
    index = 0
    best = list_of_pop[0]

    for pop,i in zip(list_of_pop,range(len(list_of_pop))):
        if(pop.getRatings() > best.getRatings()):
            best = pop
            index = i
    return best,index






########## Evaluation Functions ##################
def pop_eval_one( pop_list, goal):
    pop_sum = 0;
    for person in pop_list:
        if person >= goal:
            return 0
        pop_sum = pop_sum + person
    if pop_sum > goal:
        return 0
    rating = (float(pop_sum)/int(goal))*100
    return int(rating)


def eval_pop(pop_list,goal):
    for pop in pop_list:
        pop.evalPop(pop_eval_one, goal)
    return pop_list
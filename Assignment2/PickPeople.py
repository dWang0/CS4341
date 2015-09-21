__author__ = 'Ray'

#Given a list of population, return the list of populations with the highest ratings
#(the most fit populations) repaces the weakest link with the strongest
def pickPeople(list_of_pop, num_pops):
    sorted_pop = []
    i = 0
    ## Sorts the population by the best pop to worst pop
    for i in range(len(list_of_pop)):
        temp,index = getBestPop(list_of_pop)
        sorted_pop.append(temp)
        list_of_pop.pop(index)
    ## Caps the number of pops
    ## Idk what this is right now, but I think this contributes to a problem
    if num_pops >= len(sorted_pop):
        num_pops = len(sorted_pop)

    best_pops = []

    i = 0
    ## Get the first part of the list: length of list_of_pop - num_pops
    for i in range(0,num_pops,1):
        best_pops.append(sorted_pop[i])

    ## Fill the rest of the list.
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
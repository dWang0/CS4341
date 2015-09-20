__author__ = 'Ray'

#Given a list of population, return the list of populations with the highest ratings
#(the most fit populations) repaces the weakest link with the strongest
def pickPeople(list_of_pop, num_pops):
    best_pops = [list_of_pop[0]]

    for pop in list_of_pop:
        for current_best_pop in best_pops:
            if(pop.getRatings() > current_best_pop.getRatings()):
                if(len(best_pops) == num_pops):
                    worst = getWorstPop(best_pops)
                    #replace the worst best pop with the current pop
                    best_pops.remove(worst)
                    best_pops.append(pop)

                else:
                    best_pops.append(pop)

    best = getBestPop(list_of_pop)
    while(len(best_pops) <= len(list_of_pop)):
        best_pops.append(best)

    return best_pops

def getWorstPop(list_of_pop):
    worst = list_of_pop[0]

    for pop in list_of_pop:
        if(pop.getRatings() < worst.getRatings()):
            worst = pop

    return worst

def getBestPop(list_of_pop):
    best = list_of_pop[0]

    for pop in list_of_pop:
        if(pop.getRatings() < best.getRatings()):
            best = pop

    return best






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
__author__ = 'troyhughes'

#param: index: the population to skip
def mutation(pop_list,default_list,goal,index):
    for i in range(len(pop_list)):
        if (i == index):
            continue
        else:
            pop_list[i].mutate(default_list,goal)

    return pop_list
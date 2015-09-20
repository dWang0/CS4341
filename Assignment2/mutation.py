__author__ = 'troyhughes'

def mutation(pop_list,default_list,goal):
    for pop in pop_list:
        pop.mutate(default_list,goal)

    return pop_list
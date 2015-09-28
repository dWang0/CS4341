from GeneticAlgorithm1 import *
from first_gen import *
from Population import *
from crossover import *
from PickPeople import *
from mutation import *
from time import *
__author__ = 'troyhughes'


def run_p2(input_sring,TIME=20,GENERATION_SIZE=10,GENERATION_REMOVE=1):
    # GENERATION_SIZE = 4
    # GENERATION_REMOVE = 1
    # MAX_GENERATION = 30



    response = readcsv_float(input_sring)
    # print response
    goal = response.pop(0)
    # print goal,response

    f_gen = poptwofg(response,GENERATION_SIZE)
    # print f_gen

    best_pop = None
    future_gen = []
    future_gen.extend(f_gen)

    tstart = time()
    NUM_GEN = 0
    DIFF = time()-tstart
    while (DIFF) < TIME:
        NUM_GEN = NUM_GEN + 1
        future_gen = eval_pop(future_gen,goal,pop_eval_two)
        # print"Your future gen is: "
        # for pop in future_gen:
        #     print pop

        num_picked = GENERATION_SIZE-GENERATION_REMOVE              ## Get the number of populations to take
        future_gen = pickPeople(future_gen, num_picked)             ## Set the genration to the 'num_picked' populations, with the removed pop replaced with the top pop
        # print "Your You picked: "
        # for pop in future_gen:
        #     print pop


        future_gen = crosspop2(future_gen, set(response))
        # print"Your crossover gen is: "
        # for pop in future_gen:
        #     print pop

        future_gen = mutation(future_gen,response,goal,None)
        # print"Your fixed crossover gen is: "
        # for pop in future_gen:
        #     print pop

        future_gen = eval_pop(future_gen,goal,pop_eval_two)
        # print"Your eval fixed crossover gen is: "
        # for pop in future_gen:
        #     print pop



        best_pop,index = getBestPop(future_gen)
        DIFF = time()-tstart

    print "You have finished, here is your population: "
    print best_pop
    best_pop.score()
    print "It took "+str(NUM_GEN)+ "generations."
    print "And it required "+str(DIFF)+" seconds"
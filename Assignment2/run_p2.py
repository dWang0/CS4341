from GeneticAlgorithm1 import *
from first_gen import *
from Population import *
from crossover import *
from PickPeople import *
from mutation import *
__author__ = 'troyhughes'


def run_p2(input_sring,MAX_GENERATION=30,GENERATION_SIZE=10,GENERATION_REMOVE=1):
    # GENERATION_SIZE = 4
    # GENERATION_REMOVE = 1
    # MAX_GENERATION = 30



    response = readcsv(input_sring)
    # print response
    goal = response.pop(0)
    # print goal,response

    f_gen = poptwofg(response,GENERATION_SIZE)
    print f_gen

    best_pop = None
    future_gen = []
    future_gen.extend(f_gen)

    # for NUM_GEN in range(MAX_GENERATION):
    #     future_gen = eval_pop(future_gen,goal)
    #     # print("Your future gen is: ",future_gen)
    #
    #     num_picked = GENERATION_SIZE-GENERATION_REMOVE              ## Get the number of populations to take
    #     future_gen = pickPeople(future_gen, num_picked)             ## Set the genration to the 'num_picked' populations, with the removed pop replaced with the top pop
    #     # print ("Your You picked: ",future_gen)
    #
    #     future_gen = crossover(future_gen, None)
    #     # print("Your crossover gen is: ",future_gen)
    #
    #     future_gen = mutation(future_gen, response, goal, 0)
    #     # print ("Your mutated gen is: ",future_gen)
    #
    #     future_gen = eval_pop(future_gen,goal)
    #     # print ("Your Re-Evaluated gen is: ",future_gen)
    #
    #     best_pop,index = getBestPop(future_gen)
    #     if best_pop.getRatings() == 100:
    #         break
    #
    # print "You have finished, here is your population: "
    # print best_pop
    # print "It took "+str(NUM_GEN)+ "generations."
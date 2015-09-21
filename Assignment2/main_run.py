from GeneticAlgorithm1 import *
from first_gen import *
from Population import *
from crossover import *
from PickPeople import *
from mutation import *

GENERATION_SIZE = 10



response = readcsv("list1.txt")
print response
goal = response.pop(0)
print goal,response

f_gen = first_gen(response,GENERATION_SIZE, goal)
print f_gen

future_gen = []
future_gen = f_gen
for i in range(10):
    future_gen = eval_pop(future_gen,goal)
    print "Your first evaluated generation:"
    print future_gen
    #this variable is the number of "best fit population we want to pick for the next gen
    num_picked = 9
    future_gen = pickPeople(future_gen, num_picked)
    print "Your You picked:"
    print future_gen
    future_gen = mutation(future_gen,response,goal)
    print "Your mutated people: "
    print future_gen
    best, index = getBestPop(future_gen)
    #if on the the next generation have a rating of 100, stahhhp
    if(best.getRatings() == 100):
        print ("One of the babies meets the goal. We will stop here, generation: ", i)
        break

    print("-------")
    raw_input("Enter to continue")
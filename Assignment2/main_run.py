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
    future_gen = pickPeople(future_gen, GENERATION_SIZE)
    print "Your You picked:"
    print future_gen
    future_gen = mutation(future_gen,response,goal)
    print "Your mutated people: "
    print future_gen

    print("-------")
    raw_input("Enter to continue")
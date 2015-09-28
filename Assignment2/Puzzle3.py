from Piece import Piece
from random import randint
from mutation import *
from PickPeople import *

##constraints
# tower is a list of Piece
#tower of size 0 or 1 is not a legal tower
def isLegal(tower):
    if len(tower) <= 0:
        return 0

    #conditions for a legal tower
    for i in range(0, len(tower)):
        thisPiece = tower[i]

        if i == 0:
            if thisPiece.getType() == 'door':
                continue
            else:
                return False
        else:
            if thisPiece.getType() != 'wall' and i != len(tower) - 1:
                return False
            else:
                lastPiece = tower[i-1]
                if thisPiece.getWidth() > lastPiece.getWidth():
                    return False
                else:
                    if thisPiece.getStrength() <= len(tower) - 1 - i:
                        return False
                    else:
                        if i == len(tower) - 1 and thisPiece.getType() != 'lookout':
                            return False
                        else:
                            continue

    return True

#this population consists of a tower, which is a list of pieces, and a rating
class Popthree:

    def __init__(self, tower=[]):
        self.children = tower
        self.rating = None


    def __hash__(self):
        return hash(self.children) * hash(13) + hash(5)

    def __str__(self):
        return "Tower: " + str(self.children) + "Rating: " + str(self.rating)

    def __repr__(self):
        return self.__str__()

    def getTower(self):
        return self.children

    def getRatings(self):
        return self.rating

    def setRating(self, rating):
        self.rating = rating

    def setPop(self,tower):
        self.children = tower

    def getCost(self):
        sumCost = 0
        for piece in self.children:
            sumCost = sumCost + piece.getCost()
        return sumCost




## NOT TWEEKED FOR PUZZLE 3 YET
    def mutate(self,default_list,goal):

        """

        :param default_list: List of possible poptwo values
        :param goal: Goal value for the program.
        :return: True if a valid mutation occurs.
                False if an invalud mutation occurs.
        """
        starting = [] ; starting.extend(self.children) ## Make a value copy of children, not a referenced copy
        working = [] ; working.extend(self.children)
        switch = randint(0,len(working)-1)

        ## Mutate into legal
        used = []
        for i in range(len(default_list)):
            new_index = randint(0,len(default_list)-1)
            while new_index in used:
                new_index = randint(0,len(default_list)-1)

            rand = randint(0,2)
            if rand == 0:
                working[switch] = default_list[new_index]
                used.append(new_index)
            elif rand == 1:
                working.insert(switch, default_list[new_index])
                used.append(new_index)
            else:
                working.remove(working[randint(0,len(working) - 1)])

            if(isLegal(working)):
                self.children = working
                return True
        return False






def popthreefg(possible_list, num_pop):

    list_of_towers = []

    while len(list_of_towers) < num_pop:

        ##Randomly generate a tower length <= to the possible pieces
        tower_length = randint(2, len(possible_list) - 1)

        used = []
        a_tower = []


        ##randomly assign pieces to be appended to a tower
        i = 0
        index = randint(0, len(possible_list) - 1)
        for i in range (0, tower_length):
            while index in used:
                index = randint(0, len(possible_list) - 1)
            a_tower.append(possible_list[index])
            used.append(index)
            index = randint(0, tower_length)

        if(isLegal(a_tower)):
            tower = Popthree(a_tower)
            list_of_towers.append(tower)

    return list_of_towers

def pop_eval3(list_of_pop):
    for pop in list_of_pop:
        rating = 10 + (len(pop.children) ** 2) - pop.getCost()
        pop.setRating(rating)


    ##main##
def puzzle3():
    door = Piece('door',5,5,2)
    door2 = Piece('door',3,3,10)
    wall1 = Piece('wall',5,5,1)
    wall2 = Piece('wall',4,5,1)
    wall3 = Piece('wall',3,5,2)
    wall4 = Piece('wall',1,2,3)
    wall5 = Piece('wall',1,10,0)
    lookout = Piece('lookout',3,1,2)
    lookout2 = Piece('lookout',1,1,1)
    #pieces = [door, wall1, wall2, wall3, lookout, wall4, wall5, wall5, wall5, wall5, door2]
    pieces = [door, wall5, wall5, wall5, wall5, wall5, wall5, wall5, wall5, wall5, lookout2]



    #legal towers
    tower1 = [door, wall1, wall2, wall3, lookout]
    tower2 = [door, wall1, lookout]

    #illegal towers
    tower3 = [lookout, door, wall1]
    tower4 = [door, wall2, wall3]
    tower5 = [door, wall2, wall3, wall1, lookout]

    listoftowers = [tower1, tower2, tower3, tower4, tower5]

    GENERATIONS = 10

    for i in range(0, GENERATIONS):
        if i == 0:
            gen3 = popthreefg(pieces, 10)
            pop_eval3(gen3)
            print "First gen:"
            print gen3

        gen3 = pickPeople(gen3, 4)
        pop_eval3(gen3)
        best, i = getBestPop(gen3)
        print "You picked:"
        print gen3

        #mutate but keep the best2
        keep = [gen3[0], gen3[1]]
        new_babies = popthreefg(pieces, len(gen3) - 2)
        keep.extend(new_babies)

        gen3 = keep

        #gen3 = mutation(gen3, pieces, best.getRatings(),0)
        pop_eval3(gen3)
        print "Mutated gen:"
        print gen3


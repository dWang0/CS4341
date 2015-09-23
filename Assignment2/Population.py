from first_gen import *
from random import randint

#This class represents a population that will undergo genetic algorithm
class Population:
    children = []
    ratings = []

    def __init__(self, children=[]):
        self.children = children
        self.ratings = None

    def __hash__(self):
        return hash(self.children) + hash(self.ratings) * hash(13)

    def __str__(self):
        return "Rating: "+str(self.ratings)+" members: "+str(self.children)
    def __repr__(self):
        return self.__str__()

    def getChildren(self):
        return self.children

    def getRatings(self):
        return self.ratings

    def evalPop(self, function, goal):
        self.ratings = function(self.children,goal)

    def mutate(self,default_list,goal):
        """

        :param default_list: List of possible population values
        :param goal: Goal value for the program.
        :return: True if a valid mutation occurs.
                False if an invalud mutation occurs.
        """
        starting = [] ; starting.extend(self.children) ## Make a value copy of children, not a referenced copy
        working = [] ; working.extend(self.children)
        switch = randint(0,len(starting)-1)

        ## Mutate into legal
        used = []
        for i in range(len(default_list)):
            new_index = randint(0,len(default_list)-1)
            while new_index in used:
                new_index = randint(0,len(default_list)-1)
            used.append(new_index)
            working[switch] = default_list[new_index]
            if (sum(working) < goal):
                self.children = working
                return True
        return False








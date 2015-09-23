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

class Poptwo:

    def __init__(self, bin1=[],bin2=[],bin3=[]):
        self.bin1 = bin1
        self.bin2 = bin2
        self.bin3 = bin3
        self.all = []
        self.all.extend(bin1); self.all.extend(bin2); self.all.extend(bin3)
        self.rating = None


    def __hash__(self):
        return hash(self.bin1) + hash(self.bin3) * hash(13)

    def __str__(self):
        return "Bin1: "+str(self.bin1)+" Bin2: "+str(self.bin2)+" Bin3: "+str(self.bin3)
    def __repr__(self):
        return self.__str__()

    def getBin(self,which_bin):
        if which_bin == 0: return self.bin1,self.bin2,self.bin3
        elif which_bin == 1: return self.bin1
        elif which_bin == 2: return self.bin2
        elif which_bin == 3: return self.bin3
        else: print "Error, improper value passed to Poptwo.bins"

    def getRating(self):
        return self.rating

    def setPop(self,bin1,bin2,bin3):
        self.bin1 = bin1
        self.bin2 = bin2
        self.bin3 = bin3
        self.all = []
        self.all.extend(bin1); self.all.extend(bin2); self.all.extend(bin3)


    ## Not Fixed
    def evalPop(self, function,goal):
        self.rating = function(self.bin1,self.bin2,self.bin3,goal)

    ## Not Fixed
    def mutate(self,default_list,goal):
        """

        :param default_list: List of possible poptwo values
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







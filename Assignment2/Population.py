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
        self.all = set(self.all)
        self.ratings = None


    def __hash__(self):
        return hash(self.bin1) + hash(self.bin3) * hash(13)

    def __str__(self):
        if self.ratings < 0:
            print "fukkkk"
        return "Rating: "+str(float(self.ratings))+" Bin1: "+str(self.bin1)+" Bin2: "+str(self.bin2)+" Bin3: "+str(self.bin3)
    def __repr__(self):
        return self.__str__()

    def getBin(self,which_bin):
        if which_bin == -1: return self.all
        elif which_bin == 0: return self.bin1,self.bin2,self.bin3
        elif which_bin == 1: return self.bin1
        elif which_bin == 2: return self.bin2
        elif which_bin == 3: return self.bin3
        else: print "Error, improper value passed to Poptwo.bins"

    def getRatings(self):
        return self.ratings

    def setPop(self,bin1,bin2,bin3):
        self.bin1 = bin1
        self.bin2 = bin2
        self.bin3 = bin3
        self.all = []
        self.all.extend(bin1); self.all.extend(bin2); self.all.extend(bin3)
        self.all = set(self.all)

    def getAll(self):
        all_list = []
        all_list.extend(self.all)
        return all_list

    def evalPop(self, function,goal):
        self.ratings = 0
        self.ratings = function(self.bin1,self.bin2,self.bin3,goal)
        # if self.ratings < 0:
        #     print "Here i am!"


    def score(self):
        b1_rate = self.bin1[0]*self.bin1[1]
        for b in range(2,len(self.bin1),1):
            b1_rate = b1_rate * self.bin1[b]
        b2_rate = sum(self.bin2)
        print "Bin 1 Score: "+str(b1_rate)
        print "Bin 2 Score: "+str(b2_rate)

    def valid(self):
        if len(self.bin1) > 10 or len(self.bin2) > 10 or len(self.bin3) > 10:
            return False
        neg_counter = 0
        for val in self.bin1:
            if val < 0:
                neg_counter = neg_counter+1
        if neg_counter % 2 != 0:
            return False
        return True


    ## Not Fixed
    def mutate(self,default_list,goal):
        """

        :param default_list: List of possible poptwo values
        :param goal: Goal value for the program.
        :return: True if a valid mutation occurs.
                False if an invalud mutation occurs.
        """

        neg_counter = 0
        for val in self.bin1:
            if val < 0:
                neg_counter = neg_counter+1
        if (neg_counter %2) == 0:
            return self
        # else:
        #     print 'here I am'
        fixed = False
        for v1,i in zip(self.bin1,range(0,len(self.bin1))):           ## Find the first netative value
            if v1 < 0:
                for v2,j in zip(self.bin3,range(0,len(self.bin3))):
                    if v2 > 0:
                        temp = self.bin3[j]
                        self.bin3[j] = self.bin1[i]
                        self.bin1[i] = temp
                        fixed = True
                        break;
                break;
        if fixed:
            return self

        for v1,i in zip(self.bin1,range(0,len(self.bin1))):           ## Find the first netative value
            if v1 < 0:
                for v2,j in zip(self.bin2,range(0,len(self.bin2))):
                    if v2 > 0:
                        temp = self.bin2[j]
                        self.bin2[j] = self.bin2[i]
                        self.bin1[i] = temp
                        fixed = True
                        break;
                break;
        return self







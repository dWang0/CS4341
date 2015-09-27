from Piece import Piece
from random import randint

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
                return 1
        else:
            if thisPiece.getType() != 'wall' and i != len(tower) - 1:
                return 2
            else:
                lastPiece = tower[i-1]
                if thisPiece.getWidth() > lastPiece.getWidth():
                    return 3
                else:
                    if thisPiece.getStrength() <= len(tower) - 1 - i:
                        return 4
                    else:
                        if i == len(tower) - 1 and thisPiece.getType() != 'lookout':
                            return False
                        else:
                            continue

    return True

class Popthree:

    def __init__(self, towers=[]):
        self.towers = towers
        self.rating = None


    def __hash__(self):
        return hash(self.towers) * hash(13) + hash(5)

    def __str__(self):
        return "Towers: " + str(self.towers)
    def __repr__(self):
        return self.__str__()

    def getTowers(self):
        return self.towers

    def getRating(self):
        return self.rating

    def setPop(self,towers):
        self.towers = towers


    ## For this, the function should evaluate a tower and it's pieces
    ##The goal should be a tower that uses all of it's pieces
    ##Calculating rating might be a bit trickier, because its 1-+height^2 - cost
    ##which means in some cases, shorter towers could have higher score bc of cost
    def evalPop(self, function,goal):
        self.rating = function(self.towers,goal)

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






    ##main##
def puzzle3():
    door = Piece('door',5,5,2)
    wall1 = Piece('wall',5,5,1)
    wall2 = Piece('wall',4,5,1)
    wall3 = Piece('wall',3,5,2)
    lookout = Piece('lookout',3,1,2)

    #legal towers
    tower1 = [door, wall1, wall2, wall3, lookout]
    tower2 = [door, wall1, lookout]

    #illegal towers
    tower3 = [lookout, door, wall1]
    tower4 = [door, wall2, wall3]
    tower5 = [door, wall2, wall3, wall1, lookout]

    listoftowers = [tower1, tower2, tower3, tower4, tower5]


    p3 = Popthree(listoftowers)

    print p3


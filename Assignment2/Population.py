#This class represents a population that will undergo genetic algorithm
class Population:
    children = []
    ratings = []

    def __init__(self, children=[], ratings=[]):
        self.children = []
        self.ratings = None

    def __hash__(self):
        return hash(self.children) + hash(self.ratings) * hash(13)

#How to represent a generation? for printing purpose
    #def __str__(self)

    def getChildren(self):
        return self.children

    def getRatings(self):
        return self.ratings

    def evalPop(self, function, goal):
        self.ratings = function(self.children,goal)






#This class represents a population that will undergo genetic algorithm
class Population:
    children = []
    ratings = []

    def __init__(self, children=[], ratings=[]):
        self.children = []
        self.ratings = []

    def __hash__(self):
        return hash(self._x) + hash(self._y) * hash(13)

#How to represent a generation? for printing purpose
    #def __str__(self)

    def getChildren(self):
        return self.children

    def getRatings(self):
        return self.ratings


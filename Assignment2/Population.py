#This class represents a population that will undergo genetic algorithm
class Population:
    children = []
    ratings = []

    def __init__(self, children=[]):
        self.children = []
        self.ratings = None

    def __hash__(self):
        return hash(self.children) + hash(self.ratings) * hash(13)

    def __str__(self):
        return str(self.children)
    def __repr__(self):
        return self.__str__()

    def getChildren(self):
        return self.children

    def getRatings(self):
        return self.ratings

    def evalPop(self, function, goal):
        self.ratings = function(self.children,goal)






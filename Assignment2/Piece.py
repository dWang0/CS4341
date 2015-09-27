class Piece:

    def __init__(self, piecetype, width, strength, cost):
        self. piecetype = piecetype
        self.width = width
        self.strength = strength
        self.cost = cost

    def __str__(self):
        return str(self.piecetype) + " " + str(self.width) + " " + str(self.strength) + " " + str(self.cost)
    def __repr__(self):
        return self.__str__()

    def getType(self):
        return self.piecetype

    def getWidth(self):
        return self.width

    def getStrength(self):
        return self.strength

    def getCost(self):
        return self.cost
        
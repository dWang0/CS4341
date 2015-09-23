class Piece:

    def __init__(self, piecetype, width, strength, cost):
        self. piecetype = piecetype
        self.width = width
        self.strength = strength
        self.cost = cost

    def getType(self):
        return self.piecetype

    def getWidth(self):
        return self.width

    def getStrength(self):
        return self.strength

    def getCost(self):
        return self.cost
        
from Piece import Piece

##constraints
# tower is a list of Piece
#tower of size 0 or 1 is not a legal tower
def isLegal(tower):
    if len(tower) <= 0:
        return False

    #conditions for a legal tower
    for i in range(0, len(tower)):
        thisPiece = tower[i]
        lastPiece = tower[i-1]
        if (i == 0) and (thisPiece.getType() == 'door'):
            continue
        else:
            if (i == len(tower) - 1) and (thisPiece.getType() != 'lookout'):
                return 2
            if thisPiece.getType != 'wall':
                return 3
            if thisPiece.getWidth() > lastPiece.getWidth():
                return 4
            if thisPiece.getStrength() < len(tower) - i:
                return 5
        return True


##main##
door = Piece('door',5,3,2)
wall1 = Piece('wall',5,5,1)
wall2 = Piece('wall',4,3,1)
wall3 = Piece('wall',3,3,2)
lookout = Piece('lookout',3,1,2)

#legal towers
tower1 = [door, wall1, wall2, wall3, lookout]
tower2 = [door, wall1, lookout]

#illegal towers
tower3 = [lookout, door, wall1]
tower4 = [door, wall2, wall3]
tower5 = [door, wall2, wall3, wall1, lookout]

listoftowers = [tower1, tower2, tower3, tower4, tower5]


for t in listoftowers:
    print isLegal(t)

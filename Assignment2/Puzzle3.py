from Piece import Piece

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


##main##
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


for t in listoftowers:
    print isLegal(t)

